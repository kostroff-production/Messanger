from django.urls import path, re_path
from . import consumers


websocket_urlpatterns = [
    re_path(r'^ws/requestMessage/(?P<pk>\w+)/$', consumers.AsyncMessageConsumer.as_asgi()),
    re_path(r'^ws/getMessages/(?P<pk>\w+)/$', consumers.AsyncGetMessagesConsumer.as_asgi()),
    re_path('^ws/add/photo/(?P<name>\w+)/$', consumers.AsyncAddPhotoConsumer.as_asgi()),
    path('ws/add/video/', consumers.AsyncAddVideoConsumer.as_asgi()),
    path('ws/friend/', consumers.AsyncAddFriendConsumer.as_asgi()),
    path('ws/permission/', consumers.AsyncPermissionConsumer.as_asgi()),
    path('ws/connect/', consumers.AsyncConnectConsumer.as_asgi()),
    path('ws/person/', consumers.AsyncPersonConsumer.as_asgi()),
    path('ws/register/', consumers.RegisterConsumer.as_asgi())
]
