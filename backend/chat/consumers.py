import os
import re
from backend.settings import BASE_DIR
from time import timezone
from . import models
from .serializers import ChatSerializers, MessageSerializer, PhotoSerializers, VideoSerializes, PermissionSerializers

from django.contrib.contenttypes.models import ContentType

from channels.db import database_sync_to_async
from channels.generic.websocket import AsyncJsonWebsocketConsumer
from channels.consumer import AsyncConsumer

from django.utils import timezone
import json


class AsyncPersonConsumer(AsyncJsonWebsocketConsumer):

    async def connect(self):
        self.group = 'user_' + str(self.scope['user'].id)
        await self.channel_layer.group_add(
            self.group,
            self.channel_name
        )
        await self.accept()

    async def receive_json(self, content, **kwargs):
        data = content['users']

        chat = await self.create_chat(data)
        data_chat = {
            "group": "chat",
            "user_id": str(self.scope['user'].id),
            "data": chat
        }
        await self.channel_layer.group_send(
            self.group,
            {
                "type": "send_json",
                "data": data_chat
            }
        )
        for user in data:
            await self.channel_layer.group_send(
                'user_' + user,
                {
                    "type": "send_json",
                    "data": data_chat
                }
            )

    @database_sync_to_async
    def create_chat(self, users):
        person = self.scope['user']
        if len(users) == 1:
            # далее мы проверяем наличие действующего диалога с этим юзером, нам не нужно плодить однотипные диалоги
            chat = models.Chat.objects.filter(
                members=person, type=models.Chat.DIALOG  # указываем тип беседы, в данном случае диалог
            ).filter(
                members=users[0]
            )
            if chat:  # выполняем проверку есть уже чат с персонажем или нет
                serializer_chat = ChatSerializers(chat, many=True)
            elif chat.count() == 0:  # если наш query set пуст то создаем диалог
                new_chat = models.Chat.objects.create()  # создавать будет через метод create для модели
                new_chat.type = new_chat.DIALOG  # обязательно указываем тип, по дефолту у нас чат
                # добавляем участников и сохраняем
                new_chat.members.add(person)
                new_chat.members.add(users[0])
                new_chat.save()
                serializer_chat = ChatSerializers(new_chat)
            return serializer_chat.data
        else:  # если же пришел список участников
            new_chat = models.Chat.objects.create()  # аналогично с диалогом создаем и чат
            new_chat.members.add(person)
            for user in users:  # так как мы не можем через add добавить сразу "пачку" пользователей, добавим их перебором через массив
                new_chat.members.add(user)
            new_chat.save()
            serializer_chat = ChatSerializers(new_chat)
            return serializer_chat.data


class AsyncMessageConsumer(AsyncJsonWebsocketConsumer):

    async def connect(self):
        self.chat_id = self.scope['url_route']['kwargs']['pk']
        self.group = 'chat_' + self.chat_id
        await self.channel_layer.group_add(
            self.group,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, code):
        await self.channel_layer.group_discard(
            self.group,
            self.channel_name
        )

    async def receive_json(self, data, **kwargs):
        action = data['action']
        text = data['message']

        if action == 'create_message':
            func = 'message_active'
            new_message = await self.create_message(text)
        elif action == 'create_message_file':
            func = 'message_active'
            new_message = await self.create_message(text)
            if data['img'] != '':
                await self.update_photo(data['img'])
            if data['video'] != '':
                await self.update_video(data['video'])
        elif action == 'update_message':
            slug = data['slug_message']
            func = 'update_message_active'
            new_message = await self.update_message(slug_message=slug, message=text)
        elif action == 'update_message_file':
            slug = data['slug_message']
            func = 'update_message_active'
            new_message = await self.update_message(slug_message=slug, message=text)
            if data['img'] != '':
                await self.update_photo(data['img'])
            if data['video'] != '':
                await self.update_video(data['video'])
        elif action == 'delete_message':
            func = 'delete_message_active'
            new_message = await self.delete_message(slug_message=text)
        elif action == 'change_chat_name':
            func = 'send_json'
            new_message = {"id": int(self.chat_id), "name": text}
            await self.change_name_chat(text)
        elif action == 'delete_photo':
            func = 'delete_photo_active'
            await self.delete_photo(text)
            new_message = {"id": text}
        elif action == 'delete_video':
            func = 'delete_video_active'
            await self.delete_video(text)
            new_message = {"id": text}
        elif action == 'test':
            func = 'send_json'
            new_message = text
            await self.channel_layer.group_send(
                self.group,
                {
                    'type': func,
                    'data': new_message
                }
            )
            return

        await self.channel_layer.group_send(
            self.group,
            {
                'type': func,
                'data': new_message
            }
        )

        members = await database_sync_to_async(self.get_members)()
        for member in members:
            user_group = 'user_' + member
            await self.channel_layer.group_send(
                user_group,
                {
                    "type": "send_json",
                    "data": {
                        "group": "message",
                        "action": func,
                        "data": new_message
                    }
                }
            )

    async def message_active(self, message):
        await self.send_json(message)

    async def update_message_active(self, message):
        await self.send_json(message)

    async def delete_message_active(self, message):
        await self.send_json(message)

    async def delete_photo_active(self, message):
        await self.send_json(message)

    async def delete_video_active(self, message):
        await self.send_json(message)

    def get_members(self):
        members = models.Chat.objects.get(id=self.chat_id).members.all()
        arr = []
        for member in members:
            if member != self.scope['user']:
                arr.append(str(member.id))
        return arr

    @database_sync_to_async
    def create_message(self, message):
        new_message = models.Message.objects.create(
            chat_id=self.chat_id,
            author=self.scope['user'],
            message=message
        )
        chat = models.Chat.objects.get(id=self.chat_id)
        chat.last_message = new_message
        chat.save()
        serializer = ChatSerializers(chat)
        return serializer.data

    @database_sync_to_async
    def update_message(self, slug_message, message):
        update_message = models.Message.objects.get(slug_message=slug_message)

        if update_message.message != message:
            update_message.message = message
            update_message.is_update = True
            update_message.date_update = timezone.datetime.now()
            update_message.save()
            serializer = MessageSerializer(update_message)
            return serializer.data
        return {'message': 'False'}

    @database_sync_to_async
    def delete_message(self, slug_message):
        message = models.Message.objects.get(slug_message=slug_message)
        message_id = message.id
        if message.chat.last_message:
            last_message = message.chat.last_message.id
        else:
            last_message = 0
        message.delete()
        return {
            'id': message_id,
            'chat_id': int(self.chat_id),
            'last_message': last_message
        }

    @database_sync_to_async
    def update_photo(self, photo):
        arrPhoto = photo.split(',')

        for photo_id in arrPhoto:
            models.Photo.objects.filter(id=photo_id).update(object_id=self.chat_id)

    @database_sync_to_async
    def delete_photo(self, photo_id):
        try:
            models.Photo.objects.get(id=photo_id).delete()
        except models.Photo.DoesNotExist:
            pass

    @database_sync_to_async
    def update_video(self, video):
        arrVideo = video.split(',')

        for video_id in arrVideo:
            models.Video.objects.filter(id=video_id).update(object_id=self.chat_id)

    @database_sync_to_async
    def delete_video(self, video_id):
        try:
            models.Video.objects.get(id=video_id).delete()
        except models.Video.DoesNotExist:
            pass

    @database_sync_to_async
    def change_name_chat(self, name):
        chat = models.Chat.objects.get(id=self.chat_id)
        if len(name) > 149:
            chat.name = name[:150]
        else:
            chat.name = name
        chat.save()


class AsyncGetMessagesConsumer(AsyncConsumer):

    async def websocket_connect(self, message):
        await self.send({
            "type": "websocket.accept",
        })

    async def websocket_receive(self, message):
        quantity = json.loads(message['text'])
        messages = await self.get_messages(quantity)
        await self.send({
            "type": "websocket.send",
            "text": json.dumps(messages)
        })

    @database_sync_to_async
    def get_messages(self, quantity):
        chat_id = self.scope['url_route']['kwargs']['pk']
        start = int(quantity['quantity_start'])
        finish = int(quantity['quantity_finish'])
        messages = models.Message.objects.filter(chat=chat_id).reverse()[start:finish]
        serializer = MessageSerializer(messages, many=True)
        return serializer.data


def create_dir(new_dir):
    try:
        os.makedirs(new_dir)
    except OSError:
        print(f"Директория {new_dir} уже есть")


class AsyncAddPhotoConsumer(AsyncJsonWebsocketConsumer):

    async def connect(self):
        self.name = self.scope['url_route']['kwargs']['name']
        self.group = 'photo_' + self.name + str(self.scope['user'].id)
        await self.channel_layer.group_add(
            self.group,
            self.channel_name
        )
        await self.accept()

    async def receive(self, text_data=None, bytes_data=None, **kwargs):
        path = await self.add_photo(bytes_data)
        await self.channel_layer.group_send(
            self.group,
            {
                "type": "send_json",
                "data": path
            }
        )

    async def add_photo(self, bytes_photo):
        user = self.scope['user']

        date = str(timezone.datetime.date(timezone.datetime.now()))
        time = str(timezone.datetime.time(timezone.datetime.now()))
        time = re.sub(':', '_', time)
        time = re.sub('\.\d+', '.jpg', time)
        filename = date + '/' + time

        path_to_file = models.user_directory_path_photo(user, filename)
        new_dir = str(BASE_DIR) + '/media/' + re.sub('\w+.jpg', '', path_to_file)
        create_dir(new_dir)

        with open('media/' + path_to_file, "wb") as f:
            f.write(bytes_photo)

        if self.name == 'message':
            photo = await self.create_photo(path_to_file)
        elif self.name == 'setting':
            photo = await self.update_avatar(path_to_file)
        return [photo.id, path_to_file]

    @database_sync_to_async
    def create_photo(self, src):
        user = self.scope['user']
        content_type = ContentType.objects.get_for_model(models.Chat)

        return models.Photo.objects.create(
            slug=user.slug,
            object_id=0,
            content_type=content_type,
            user=user,
            descriptionPhoto=''.join(re.findall('(\w+).jpg', src)),
            photo=src
        )

    @database_sync_to_async
    def update_avatar(self, src):
        content_type = ContentType.objects.get_for_model(self.scope['user'])
        return models.Photo.objects.create(
            slug=self.scope['user'].slug,
            object_id=str(self.scope['user'].id),
            content_type=content_type,
            user=self.scope['user'],
            descriptionPhoto=''.join(re.findall('(\w+).jpg', src)),
            photo=src,
            avatar=True
        )


class AsyncAddVideoConsumer(AsyncConsumer):

    async def websocket_connect(self, message):
        await self.send({
            "type": "websocket.accept"
        })

    async def websocket_receive(self, message):
        bytes_video = message['bytes']
        path = await self.add_video(bytes_video)
        await self.send({
            "type": "websocket.send",
            "text": json.dumps(path)
        })

    async def add_video(self, bytes_video):
        user = self.scope['user']

        date = str(timezone.datetime.date(timezone.datetime.now()))
        time = str(timezone.datetime.time(timezone.datetime.now()))
        time = re.sub(':', '_', time)
        time = re.sub('\.\d+', '.mp4', time)
        filename = date + '/' + time

        path_to_file = models.user_directory_path_video(user, filename)
        new_dir = str(BASE_DIR) + '/media/' + re.sub('\w+.mp4', '', path_to_file)
        create_dir(new_dir)

        with open('media/' + path_to_file, 'wb') as f:
            f.write(bytes_video)

        video = await self.create_video(path_to_file)
        return [video.id, path_to_file]

    @database_sync_to_async
    def create_video(self, src):
        user = self.scope['user']
        content_type = ContentType.objects.get_for_model(models.Chat)

        return models.Video.objects.create(
            slug=user.slug,
            object_id=0,
            content_type=content_type,
            user=user,
            title_video=''.join(re.findall('(\w+).mp4', src)),
            video=src
        )


class AsyncAddFriendConsumer(AsyncJsonWebsocketConsumer):

    async def connect(self):
        self.my_group = 'my_group' + str(self.scope['user'].id)
        await self.channel_layer.group_add(
            self.my_group,
            self.channel_name
        )
        await self.accept()

    async def receive_json(self, content, **kwargs):
        action = content['action']

        if action == 'create_friend':
            user_id = content['possible_friend']
            await self.create_friend(user_id)
            data = {
                'action': action,
                'possible_friend': user_id
            }
        elif action == 'confirmation_friend':
            user_id = content['friend_id']
            await self.confirmation_friend(user_id)
            data = {
                'action': action,
                'friend_id': user_id,
            }
        elif action == 'delete_friend':
            user_id = content['friend']
            await self.delete_friend(user_id)
            data = {
                'action': action,
                'friend': user_id
            }

        await self.channel_layer.group_send(
            self.my_group,
            {
                'type': 'send_json',
                'data': data
        })

        self.user_group = 'user_' + user_id
        data_user = {
            'group': 'friend',
            'action': action,
            'friend_id': str(self.scope['user'].id)
        }
        await self.channel_layer.group_send(
            self.user_group,
            {
                'type': 'send_json',
                'data': data_user
            }
        )

    @database_sync_to_async
    def create_friend(self, possible_friend):
        user_obj = models.Person.objects.get(id=possible_friend)
        content_type = ContentType.objects.get_for_model(user_obj)

        # при отправке запроса на дружбу сразу же мы не указываем пользователя как друга
        # мы ждем от него подтверждения, чито он тоже хочет с нами дружить
        models.Friend.objects.create(
            slug=user_obj.slug,
            content_type=content_type,
            object_id=user_obj.pk,
            possible_friends=self.scope['user']
        )
        models.Friend.objects.create(
            slug=self.scope['user'].slug,
            content_type=content_type,
            object_id=self.scope['user'].id,
            waiting_confirmations=user_obj
        )

    @database_sync_to_async
    def confirmation_friend(self, user_waiting):
        obj_user_waiting = models.Person.objects.get(id=user_waiting)  # извлекаем модель юзера подавшего заявку
        user_confirmation = models.Person.objects.get(id=self.scope['user'].id)  # извлекаем нашу модель юзера

        models.Friend.objects.update_or_create(
            object_id=self.scope['user'].id,
            possible_friends = obj_user_waiting,
            defaults={'friends': obj_user_waiting, 'possible_friends': None}
        )

        models.Friend.objects.update_or_create(
            object_id=user_waiting,
            waiting_confirmations=user_confirmation,
            defaults={'friends': user_confirmation, 'waiting_confirmations': None}
        )

        try:
            permission = models.Permission.objects.get(slug__exact=obj_user_waiting.slug)
            if permission.txt_message_ban == 'Доступно только друзьям':
                permission.message_ban.clear()
                friends = models.Friend.objects.filter(slug__exact=obj_user_waiting.slug, possible_friends=None,
                                                       waiting_confirmations=None)
                for friend in friends:
                    permission.message_ban.add(
                        friend.friends)
        except models.Permission.DoesNotExist:
            pass

        try:
            permission = models.Permission.objects.get(slug__exact=self.scope['user'].slug)
            if permission.txt_message_ban == 'Доступно только друзьям':
                permission.message_ban.clear()
                friends = models.Friend.objects.filter(slug__exact=self.scope['user'].slug, possible_friends=None, waiting_confirmations=None)
                for friend in friends:
                    permission.message_ban.add(
                        friend.friends)
        except models.Permission.DoesNotExist:
            pass

    @database_sync_to_async
    def delete_friend(self, friend_id):
        friend = models.Person.objects.get(id=friend_id)
        try:
            my_model_friend = models.Friend.objects.get(object_id=self.scope['user'].id,
                                                        friends=friend)  # забираем объект
            my_model_friend.delete()  # удаляем свою модель

            friend_model_friend = models.Friend.objects.get(object_id=friend_id,
                                                            friends=self.scope['user'])  # забираем модель друга
            friend_model_friend.delete()

        except models.Friend.DoesNotExist:  # если именно дружбы нет, а все на стадии заявки, то обрабатываем исключение
            my_model_friend = models.Friend.objects.get(object_id=self.scope['user'].id,
                                                        possible_friends=friend)
            my_model_friend.delete()

            friend_model_friend = models.Friend.objects.get(object_id=friend_id,
                                                         waiting_confirmations=self.scope['user'])  # и ищем модель где юзер ожидает ответа от нас
            friend_model_friend.delete()

        try:
            permission = models.Permission.objects.get(slug__exact=friend.slug)
            if permission.txt_message_ban == 'Доступно только друзьям':
                permission.message_ban.clear()
                friends = models.Friend.objects.filter(slug__exact=friend.slug, possible_friends=None,
                                                       waiting_confirmations=None)
                for friend in friends:
                    permission.message_ban.add(
                        friend.friends)
        except models.Permission.DoesNotExist:
            pass

        try:
            permission = models.Permission.objects.get(slug__exact=self.scope['user'].slug)
            if permission.txt_message_ban == 'Доступно только друзьям':
                permission.message_ban.clear()
                friends = models.Friend.objects.filter(slug__exact=self.scope['user'].slug, possible_friends=None,
                                                       waiting_confirmations=None)
                for friend in friends:
                    permission.message_ban.add(
                        friend.friends)
        except models.Permission.DoesNotExist:
            pass


class AsyncPermissionConsumer(AsyncConsumer):

    async def websocket_connect(self, message):
        await self.send({
            "type": "websocket.accept"
        })

    async def websocket_receive(self, message):
        data = message['text']
        input_data = json.loads(data)
        action = input_data['action']

        if action == 'permission':
            await self.permission(input_data['slug'], input_data['txt_message_ban'], input_data['FriendHid'])
        elif action == 'person':
            await self.person(input_data['slug'], input_data['field'], input_data['text'])

        await self.send({
            "type": "websocket.send",
            "text": action
        })
        
        await self.channel_layer.group_send(
            'user_' + str(self.scope['user'].id),
            {
                "type": "send_json",
                "data": {
                    "group": "settings",
                    "data": input_data
                }
            }
        )

    @database_sync_to_async
    def person(self, slug, field, text):
        if field == 'name':
            models.Person.objects.filter(slug__exact=slug).update(name=text)
        elif field == 'email':
            models.Person.objects.filter(slug__exact=slug).update(email=text)
        elif field == 'quote':
            models.Person.objects.filter(slug__exact=slug).update(quote=text)
        elif field == 'avatar':
            photo = models.Photo.objects.get(id=text)
            models.Person.objects.update_or_create(
                slug=slug,
                defaults={'avatar': photo}
            )
        elif field == 'style':
            models.Person.objects.filter(slug__exact=slug).update(style=text)

    @database_sync_to_async
    def permission(self, slug, txt_message_ban, FriendHid):
        objFriend = models.Friend.objects.filter(slug=slug)  # предварительно извлекаем свои модели друзей
        friends = []
        for obj in objFriend:
            if obj.friends != None:
                friends.append(obj.friends.id)  # записываем отдельно всех имеющихся друзей

        listIdFriend = []
        x = 0
        if FriendHid:
            while x < len(FriendHid):
                s_int = ''
                a = FriendHid[x]
                while '0' <= a <= '9':
                    s_int += a
                    x += 1
                    if x < len(FriendHid):
                        a = FriendHid[x]
                    else:
                        break
                x += 1
                if s_int != '':
                    listIdFriend.append(int(s_int))

        # модель ограничения должна быть уникальна, поэтому выполним проверку на ее наличие
        try:
            permission = models.Permission.objects.get(slug=slug)
        except models.Permission.DoesNotExist:
            permission = models.Permission.objects.create(
                slug=slug,
                user=self.scope['user']
            )

        # далее описание ограничений под различный контент похожи, отличает их только нейминг атрибутов
        # принцип DRY тут применить проблематично, так как тогда потеряется уникальность конкретной области ограничения контента
        # поэтому описываем каждый тип ограничения отдельно
        if txt_message_ban == 'Доступно всем':
            permission.message_ban.clear()  # если мы хотим открыть для всех, то юзеров в атрибуте быть не должно
            permission.txt_message_ban = 'Доступно всем'  # обновляем статус текущего ограничения, что бы потом корректно подгружать его в настройках профиля
        elif txt_message_ban == 'Не беспокоить':
            permission.message_ban.clear()
            permission.txt_message_ban = 'Не беспокоить'
            permission.message_ban.add(self.scope['user'])  # если скрываем от всех, то добовляем только себя
        elif txt_message_ban == 'Доступно только друзьям':
            permission.txt_message_ban = 'Доступно только друзьям'
            permission.message_ban.clear()
            # для того что бы наложить ограничения на всех кроме друзей нам и нужны были наши квери сеты моделей друзей
            # из которых мы благополучно извлекли айпи юзеров, которым и предоставим доступ к просмотру в шаблоне
            for friend in friends:
                permission.message_ban.add(
                    friend)  # тут все просто, методом перебора по одному добавляем их в наш список
        elif txt_message_ban == 'Скрыть от некоторых друзей':
            # если мы хотим скрыть от некоторых друзей и например у нас стоит видимость только для друзей, то нам нужно
            # убрать видимость для тех друзей кому доступ запрещен
            permission.HidFriend.clear()
            for friend in listIdFriend:
                permission.HidFriend.add(friend)  # добовляем друзей которых надо исключить в отдельный атрибут
        elif txt_message_ban == None and len(listIdFriend) != 0:  # если мы хотим открыть доступ для одного из ранее попавших под ограничения друзей
            permission.HidFriend.remove(listIdFriend[0])  # мы просто удаляем его из списка

        permission.save()


class AsyncConnectConsumer(AsyncJsonWebsocketConsumer):

    async def connect(self):
        self.group = 'connect_' + str(self.scope['user'].id)
        await self.channel_layer.group_add(
            self.group,
            self.channel_name
        )
        await self.accept()

    async def receive_json(self, content, **kwargs):
        chat_id = content['chat_id']
        data = await self.get_chat_data(chat_id)
        await self.channel_layer.group_send(
            self.group,
            {
                "type": "send_json",
                "data": data
            }
        )

    @database_sync_to_async
    def get_chat_data(self, chat_id):
        chat = models.Chat.objects.get(id=chat_id)
        chat.message_set.filter(is_read=False).exclude(author=self.scope['user']).update(is_read=True)
        content_type = ContentType.objects.get_for_model(chat)
        chat_serializer = ChatSerializers(chat)

        messages = models.Message.objects.filter(chat=chat_id).reverse()[:10]
        message_serializer = MessageSerializer(messages, many=True)

        photo = models.Photo.objects.filter(content_type=content_type, object_id=chat_id)
        photo_serializer = PhotoSerializers(photo, many=True)

        video = models.Video.objects.filter(content_type=content_type, object_id=chat_id)
        video_serializer = VideoSerializes(video, many=True)

        if len(chat.members.all()) == 2:
            query_member = chat.members.exclude(id=self.scope['user'].id)
            for member in query_member:
                permission = models.Permission.objects.filter(slug__iexact=member.slug)
                permission_serializer = PermissionSerializers(permission, many=True).data
        else:
            permission_serializer = []

        return {
                'chat': chat_serializer.data,
                'photo': photo_serializer.data,
                'video': video_serializer.data,
                'message': message_serializer.data,
                'permission': permission_serializer
            }

    
class RegisterConsumer(AsyncConsumer):

    async def websocket_connect(self, message):
        await self.send({
            "type": "websocket.accept"
        })

    async def websocket_receive(self, message):
        data = message['text']
        person = json.loads(data)

        users = await self.person_list(person['text']['slug'])
        for user_id in users:
            await self.channel_layer.group_send(
                'user_' + str(user_id),
                {
                    "type": "send_json",
                    "data": {
                        "group": "new_person",
                        "data": person
                    }
                }
            )

    @database_sync_to_async
    def person_list(self, slug):
        users = models.Person.objects.all().exclude(slug__exact=slug)
        arr = []
        for user in users:
            arr.append(user.id)
        return arr


