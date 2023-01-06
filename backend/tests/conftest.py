import pytest_asyncio
from channels.testing import WebsocketCommunicator
from channels.routing import URLRouter
from django.urls import re_path
from chat import consumers


class User:
    def __init__(self):
        self.id = 0


@pytest_asyncio.fixture
async def person_consumer():
    communicator = WebsocketCommunicator(consumers.AsyncPersonConsumer.as_asgi(), 'ws/person/')
    communicator.scope['user'] = User()
    connected, subprotocol = await communicator.connect()
    print('connected person {}'.format(connected))
    yield connected
    await communicator.disconnect()


@pytest_asyncio.fixture
async def message_consumer_communicator():
    application = URLRouter([
        re_path(r'^ws/requestMessage/(?P<pk>\w+)/$', consumers.AsyncMessageConsumer.as_asgi())
    ])
    communicator = WebsocketCommunicator(application, 'ws/requestMessage/1/')
    yield communicator


@pytest_asyncio.fixture
async def message_consumer_connect(message_consumer_communicator):
    connected, subprotocol = await message_consumer_communicator.connect()
    print('connected message {}'.format(connected))
    yield connected


@pytest_asyncio.fixture
async def message_consumer_response(message_consumer_communicator):
    await message_consumer_communicator.send_json_to({'action': 'test', 'message': 'test message'})
    response = await message_consumer_communicator.receive_json_from()
    print('response message {}'.format(response))
    yield response
    await message_consumer_communicator.disconnect()
