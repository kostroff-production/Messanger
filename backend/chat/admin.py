from django.contrib import admin
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from . import models


class AdminFormModelPerson(forms.ModelForm):
    class Meta:
        model = models.Person
        fields = [
            'login', 'password', 'groups', 'user_permissions', 'slug',
            'name', 'email', 'avatar', 'quote',
            'is_superuser', 'is_staff', 'is_active',
            'last_login', 'last_online', 'style'
        ]


class AdminMessageForm(forms.ModelForm):
    message = forms.CharField(label='Сообщение', widget=CKEditorUploadingWidget())

    class Meta:
        model = models.Message
        fields = '__all__'


class AdminPhotoForm(forms.ModelForm):
    class Meta:
        models = models.Photo
        fields = '__all__'


@admin.register(models.Person)
class ModelPerson(admin.ModelAdmin):
    list_display = ('login', 'name', 'last_online')
    list_filter = ('login', 'name', 'last_online')
    search_fields = ('login', 'name', 'email')
    save_on_top = True
    form = AdminFormModelPerson


@admin.register(models.Chat)
class ModelChat(admin.ModelAdmin):
    list_display = ('name', 'last_message', 'type')
    save_as = True
    save_on_top = True


@admin.register(models.Message)
class ModelMessage(admin.ModelAdmin):
    list_display = ('message', 'chat', 'author', 'date_pub')
    list_filter = ('author', 'date_pub')
    search_fields = ('message', 'author', 'date_pub')
    save_as = True
    save_on_top = True
    form = AdminMessageForm


@admin.register(models.Photo)
class ModelPhoto(admin.ModelAdmin):
    list_display = ('descriptionPhoto', 'date_pub', 'photo', 'user')
    search_fields = ('user', 'descriptionPhoto', 'date_pub')
    list_filter = ('user', 'date_pub', 'avatar')
    form = AdminPhotoForm


@admin.register(models.Video)
class ModelVideo(admin.ModelAdmin):
    list_display = ('title_video', 'date_pub', 'video', 'user')
    search_fields = ('title_video', 'date_pub')


admin.site.register(models.Friend)
admin.site.register(models.Permission)
admin.site.register(models.CheckedKeys)
