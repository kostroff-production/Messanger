import pytest

def test_person_consumer(person_consumer):
    assert person_consumer

@pytest.mark.filterwarnings("ignore:DeprecationWarning")
def test_message_consumer(message_consumer_connect, message_consumer_response):
    assert message_consumer_connect
    yield
    assert message_consumer_response == {'type': 'send_json', 'data': 'test message'}