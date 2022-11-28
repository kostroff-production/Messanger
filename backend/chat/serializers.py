from rest_framework import serializers
from .models import Person, Friend, Photo, Video, Chat, Message, Permission

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth.models import update_last_login
from rest_framework_simplejwt.settings import api_settings


class TokenSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)

        refresh = self.get_token(self.user)

        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)
        data['user_id'] = str(self.user.id)

        if api_settings.UPDATE_LAST_LOGIN:
            update_last_login(None, self.user)

        return data


# для конкретных задач создаем формы сериализации наших моделей, оформление схоже с обычной modelForm
class PersonSerializers(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__' # описываем, что нужно сериализовать для дальнейшего использования полученных данных
        depth = 1


class FriendSerializers(serializers.ModelSerializer):
    class Meta:
        model = Friend
        fields = ['pk', 'friends', 'possible_friends', 'waiting_confirmations']
        depth = 2 # данный параметр позволяет нам сделать углубление в атрибут модели сериализации, модель друга содержит в себе модель юзера данные которого мы хотим использователя


class PhotoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ['id', 'photo']


class VideoSerializes(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ['id', 'video']


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'
        depth = 3


class ChatSerializers(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = ['id', 'name', 'members', 'last_message']
        depth = 3 # в данном случае нам нужно углубиться на три уровня, по мимо данных последнего сообщения, мы еще сможем получить данные юзера написавшего его


class PossibleFriendSerializers(serializers.ModelSerializer):
    class Meta:
        model = Friend
        fields = ['id', 'possible_friends']
        depth = 2


class WaitingConfirmationFriendSerializers(serializers.ModelSerializer):
    class Meta:
        model = Friend
        fields = ['waiting_confirmations']
        depth = 1


class PermissionSerializers(serializers.ModelSerializer):
    class Meta:
        model = Permission
        exclude = ('slug', 'user')
        depth = 1

