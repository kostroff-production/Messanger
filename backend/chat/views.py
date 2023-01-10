from rest_framework.response import Response
from rest_framework import generics, permissions, viewsets
from rest_framework import filters
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import (
    Person, Chat, Friend, Permission, CheckedKeys
)

from .serializers import (
    PersonSerializers, FriendSerializers,
    ChatSerializers, PermissionSerializers,
    TokenSerializer
)
from rest_framework_simplejwt.views import TokenObtainPairView

from django.core.mail import send_mail

import threading
import random
import logging
# импортирум встроенный модуль логирования и дополняем его сообщениями
logger = logging.getLogger('django')


class TokenObtainPairAdvanced(TokenObtainPairView):
    serializer_class = TokenSerializer


class RegisterView(generics.CreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializers
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        serializer_data = self.serializer_class(data=request.data)
        if serializer_data.is_valid():
            data = serializer_data.validated_data
            obj = Person.objects.create_user(
                login=data['login'],
                password=data['password']
            )
            obj.name = data['name']
            obj.save()
            return Response({'user': True, 'person': self.serializer_class(obj).data})
        else:
            return Response({'user': False})


class BaseViewPerson(generics.RetrieveAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializers
    authentication_classes = (JWTAuthentication, SessionAuthentication, BasicAuthentication)
    permission_classes = (permissions.IsAuthenticated,)
    data_ctx = None

    def retrieve(self, request, *args, **kwargs):
        person = self.get_object()
        person_serializer = self.serializer_class(person)

        try:
            permission = Permission.objects.get(slug__exact=person.slug)
            permission_serializer = PermissionSerializers(permission).data
        except Permission.DoesNotExist:
            permission_serializer = {"id": None}

        chats = Chat.objects.filter(members__in=[person])
        chats_serializer = ChatSerializers(chats, many=True)
        unread_chats = Chat.objects.filter(members__id=person.id).filter(last_message__is_read=False).exclude(last_message__isnull=True).exclude(last_message__author=person).count()

        friends = Friend.objects.filter(slug__exact=person.slug)
        friends_serializer = FriendSerializers(friends, many=True)
        count_possible = Friend.objects.filter(slug__exact=person.slug, friends=None, waiting_confirmations=None).count()

        users = Person.objects.all().exclude(slug__exact=person.slug)
        users_serializer = PersonSerializers(users, many=True)

        data = {
            'person': person_serializer.data,
            'permission': permission_serializer,
            'unread_chats': unread_chats,
            'chats': chats_serializer.data,
            'friends': friends_serializer.data,
            'count_possible': count_possible,
            'users': users_serializer.data
        }
        return Response(data)


class UsersListView(generics.ListAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializers
    authentication_classes = (JWTAuthentication, SessionAuthentication, BasicAuthentication)
    permission_classes = (permissions.IsAuthenticated,)
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']


class PasswordRecoveryViewSet(viewsets.ViewSet):
    permission_classes = (permissions.AllowAny,)

    def check_email(self, post):

        try:
            user = Person.objects.get(email=post.data['email'])
            key = random.randint(1000, 10000)
            mess = 'Временный ключ для восстановления пароля ' + str(key) + '\n' + \
                   'Ключ активен 5 минут. \n' \
                   'Для повторной отправки откройте раздел смены пароля и повторите действия. \n' \
                   '________________ \n \n' \
                   'Не отвечайте на это письмо, оно создано автоматически.'

            try:
                check_key = CheckedKeys.objects.get(user_id=user.id)
                check_key.key = key

                for thread in threading.enumerate():
                    if thread.ident == check_key.thread:
                        thread.cancel()
                        break

                timer = threading.Timer(350.0, self.remove_key, kwargs={'email': post.data['email']})
                timer.start()

                check_key.thread = timer.ident
                check_key.save()

                send_mail(
                    subject='Смена пароля',
                    message=mess,
                    from_email=config['email']['address'],
                    recipient_list=[post.data['email']]
                )

                return Response(data=True)

            except CheckedKeys.DoesNotExist:
                timer = threading.Timer(350.0, self.remove_key, kwargs={'email': post.data['email']})
                timer.start()

                CheckedKeys.objects.create(
                    user_id=user.id,
                    key=key,
                    thread=timer.ident
                )

                send_mail(
                    subject='Смена пароля',
                    message=mess,
                    from_email='KostrovProductionServer@yandex.ru',
                    recipient_list=[post.data['email']]
                )

                return Response(data=True)

        except Person.DoesNotExist:
            return Response(data=False)

    def check_key(self, post):
        user = Person.objects.get(email=post.data['email'])

        try:
            checked_key = CheckedKeys.objects.get(user_id=user.id)
            if checked_key.key == int(post.data['key']):
                self.remove_key(post.data['email'])
                return Response(data=True)
            else:
                return Response(data=False)
        except CheckedKeys.DoesNotExist:
            return Response(data=False)

    def password_recovery(self, post):
        user = Person.objects.get(email=post.data['email'])
        user.set_password(post.data['password'])
        user.save()
        return Response(data=True)

    def remove_key(self, email):
        user = Person.objects.get(email=email)
        checked_key = CheckedKeys.objects.get(user_id=user.id)

        for thread in threading.enumerate():
            if thread.ident == checked_key.thread:
                thread.cancel()
                break
        checked_key.delete()


