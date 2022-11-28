from django.db import models
from django.db.models import Q
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager, UserManager
from time import time
from django.utils import timezone
from django.utils.text import slugify
from django.conf import settings
from django.urls import reverse
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.humanize.templatetags.humanize import naturaltime
from django.utils.translation import ugettext_lazy as _



# Create your models here.
def gen_slug(s):
    slug = slugify(s, allow_unicode=True)
    return slug + str(int(time()))


# суб классы мы будем создавать через абстрактную модель, от которой они все будут наследоваться,
# в дальнейшем это упростит задачу по установке связей между моделями, связывать будем через GenericForeignKey
class AbstractModel(models.Model):
    slug = models.SlugField(max_length=150) # здесь уже уникальность слага не так важна и в некоторых случаях может даже усложнить формирование поиска моделей
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE) # устанавливаем тип модели родителя для нашего саб класса
    object_id = models.PositiveIntegerField() # саб модель так же идентифицируется по айди ее родителя(модели, которой она будет принадлежать)
    content_objects = GenericForeignKey('content_type', 'object_id') # связывем ключи для генерации внешнего ключа, который будет принадлежать родителю

    class Meta:
        abstract = True # подтверждаем, что класс абстрактный


# указываем место хранения наших файлов
# для сортировки и уникальности под каждого юзера указываем слаги объекта юзера и тип данных, который он сохраняет
def user_directory_path_photo(instance, filename):
    return 'user_{0}/{1}/{2}'.format(instance, 'photo', filename)

def user_directory_path_video(instance, filename):
    return 'user_{0}/{1}/{2}'.format(instance, 'video', filename)


class Photo(AbstractModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=False, null=False)
    descriptionPhoto = models.TextField(blank=True, null=True)
    date_pub = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(upload_to=user_directory_path_photo)
    avatar = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('photo_comment_url', kwargs={'id': self.id})


class Video(AbstractModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=False, null=False)
    date_pub = models.DateTimeField(auto_now_add=True)
    title_video = models.CharField(blank=True, max_length=250)
    video = models.FileField(
        upload_to=user_directory_path_video,
        blank=True,
        null=True
    )

    def get_absolute_url(self):
        return reverse('video_comment_url', kwargs={'id': self.id})


class ChatManager(models.Manager):
    use_for_related_fields = True

    # проверяем сообщения в чате на непрочитанность
    def unread_chat(self, user=None):
        qs = self.get_queryset().exclude(last_message__isnull=True).filter(members__id=user).filter(last_message__is_read=False)
        try:
            return qs.exclude(last_message__author=user)
        except TypeError:
            pass

class Chat(models.Model):
    DIALOG = 'D'
    CHAT = 'C'
    CHAT_TYPE_CHOICES = (
        (DIALOG, 'Диалог'),
        (CHAT, 'Чат')
    )

    slug = models.SlugField(max_length=150, blank=False, unique=True) # в чатах слаг обязательно должен быть уникален
    type = models.CharField(
        max_length=1,
        choices=CHAT_TYPE_CHOICES,
        default=CHAT # так же устанавливаем значение по умолчанию, что в дальнейшей облегчит работу при формировании чата
    )
    name = models.CharField(max_length=150, blank=True, null=True)
    members = models.ManyToManyField(settings.AUTH_USER_MODEL, verbose_name='Участник') # модель участников многие для многих, потому что участников явно может быть больше двух и в дальнейшем это ускорит поиск модели чата
    last_message = models.ForeignKey(
        'Message', # так как модель сообщения пока не объявлена указываем ее в строчной варианте
        related_name='last_message',
        on_delete=models.SET_NULL, # удаление должно быть не каскаждым иначе при удалении одного сообщения, оно потянет за собой все которые были в чате и сам чат
        blank=True,
        null=True # атрибут важен так как объект модели может содержать "ничего"
    )

    photo = GenericRelation(Photo, related_name='фото')
    video = GenericRelation(Video, related_name='видео')

    objects = ChatManager() # дополнительный объект модели с кастомными методами под кокретные задачи

    class Meta:
        ordering = ['-last_message'] # чаты выводим по последнему написано сообщению и в начале новые, потом старые

    # описывает метод сохраниения модели, в котором генерируем уникальный слаг, в дальнейшем данный метод будет применен и к другим моделям
    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = gen_slug(time())
        super().save(*args, **kwargs)

    # так же дополнительно можем вызывать модель с ее содежимым через юрл адрес, в котором хотим отобразить данные модели и продолжить работу с ней
    def get_absolute_url(self):
        return reverse('message_url', kwargs={'chat_id': self.pk})

class Message(models.Model):
    slug_message = models.SlugField(max_length=150, blank=False, unique=True)
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, verbose_name='чат') # в данном случае указываем каскадное удаление, потому что если удалиться чат то и сообщения его нам не нужны
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='автор') # автор регестрируется исходя из пользователя создавшего сообщение
    message = models.TextField('Сообщение')
    date_pub = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now_add=True) # по митмо даты формирования создадим и дату обновления
    is_read = models.BooleanField(default=False, verbose_name='прочтено') # добавим проверку на не прочитанность
    is_update = models.BooleanField(default=False, verbose_name='обновлено') # и обновление

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug_message = gen_slug(time())
        super().save(*args, **kwargs)

    # для вызова метода обновления модели сообщения указываем модели на какой юрл делать вызов
    def update_message_url(self):
        return reverse('update_message_url')

    class Meta:
        ordering = ['date_pub'] # сортировку производим исходя из даты создания

    def __str__(self):
        return self.message # указываем строчное значение модели, по которому будем определять модели в нашей админ панели например, именем модели будет текст его сообщения


# модель приватности страницы пользователя
class Permission(models.Model):
    # модель привязывает к одному пользователю и в дальнейшем только обновляется, не плодя копии
    slug = models.SlugField(max_length=150, unique=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=False, null=False)

    # текстовые атрибуты будут нужны для сверки значений приватности
    # возможно как полное скрытие страницы так и отдельного контента на странице
    # так же реализовано сокрытие от некоторых друзей
    # так как модель не плодится то атрибуты модели хранящие юзеров, имеют значение многие ко многим

    message_ban = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='глобальный_бан', blank=True)
    txt_message_ban = models.TextField(blank=True, verbose_name='статус_приватности')
    HidFriend = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='бан_для_некоторых_друзей', blank=True)

    def get_create_permission(self):
        return reverse('create_permission_url')

    def get_update_permission(self):
        return reverse('update_permission_url', kwargs={'slug': self.slug})

    def __str__(self):
        return "%s" % (self.user.name)


class FriendManager(models.Manager):
    use_for_related_fields = True

    def search(self, object_id=None, query=None):
        qs = self.get_queryset()
        if query:
            or_lookup = (Q(friends__first_name=query) | Q(friends__last_name=query) | Q(friends__middle_name=query))
            qs = qs.filter(object_id=object_id).filter(or_lookup)

        return qs

class Friend(AbstractModel):
    # модель друга имеет по мимо основного атирибута друг еще и "возможный друг", и "ожидает дружбы"
    # потому что подтверждение дружбы происходит двухсторонее и данные атрибуты служат для создания предварительных моделей дружбы между пользователями
    friends = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='Друзья', blank=True, null=True, on_delete=models.CASCADE)
    possible_friends = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='Возможные_друзья', blank=True, null=True, on_delete=models.CASCADE)
    waiting_confirmations = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='Ожидание_подтвержденя', blank=True, null=True, on_delete=models.CASCADE)

    objects = FriendManager()

    def create_friend_url(self):
        return reverse('create_friend_url')


class CheckedKeys(models.Model):
    user_id = models.IntegerField(unique=True, verbose_name='пользователь')
    key = models.IntegerField(verbose_name='ключ')
    thread = models.BigIntegerField(verbose_name='поток')


class CustomAccountManager(BaseUserManager, models.Manager):
    use_for_related_fields = True

    # переписываем процесс создания обычного пользователя
    def create_user(self, login, password): # в качестве логина по умолчанию принимаем емаил
        user = self.model(login=login, password=password)
        user.set_password(password)
        user.is_active = True
        user.is_staff = False
        user.is_superuser = False
        user.save(using=self._db)
        return user

    def create_superuser(self, login, password): # аналогично меняем логин и для суперпользователя
        user = self.model(login=login, password=password)
        user.set_password(password)
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

    def get_by_natural_key(self, username): # указываем что имя юзера нужно сверять по емайлу
        return self.get(login=username)

class Person(AbstractBaseUser, PermissionsMixin):
    STYLE_CHOICES = (
        (0, 'day'),
        (1, 'night'),
        (2, 'warm')
    )

    slug = models.SlugField(max_length=150, unique=True, blank=True)
    login = models.CharField(max_length=30, unique=True, verbose_name='логин')
    name = models.CharField(max_length=60, verbose_name='ФИО', blank=False)
    quote = models.CharField(max_length=150, blank=True, verbose_name='статус')
    email = models.EmailField(blank=True, null=True, unique=True, verbose_name='email')
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    last_online = models.DateTimeField(blank=True, null=True)
    avatar = models.ForeignKey(Photo, on_delete=models.SET_NULL, null=True, blank=True, related_name='аватар')
    style = models.CharField(max_length=1, choices=STYLE_CHOICES, default=0)

    friends = GenericRelation(Friend, related_name='Друзья')

    REQUIRED_FIELDS = []
    USERNAME_FIELD = 'login'

    objects = CustomAccountManager()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = gen_slug(time())
        super().save(*args, **kwargs)

    def get_short_name(self):
        return self.login

    def natural_key(self):
        return self.login

    def last_avatar(self):
        return Photo.objects.filter(user=self.id, avatar=True).last()

    def get_absolute_url(self):
        return reverse('base_url', kwargs={'pk': self.pk})

    def is_online(self):
        if self.last_online:
            return (timezone.now() - self.last_online) < timezone.timedelta(minutes=5)
        return False

    # Если пользователь посещал сайт не более 5 минут назад,
    def get_online_info(self):
        if self.is_online():
            # то возвращаем информацию, что он онлайн
            return 'Online'
        if self.last_online:
            # иначе пишем сообщение о последнем посещении и переводим ее
            return _('Last visit {}').format(naturaltime(self.last_online))
            # так как мы добавили информацию о посещении пользователем сайта не сразу
            # то для некоторых пользователей инфомации о посещении может и не быть, вернём информацию, что последнее посещение неизвестно
        return 'Неизвестно'

    def __str__(self):
        return self.login
