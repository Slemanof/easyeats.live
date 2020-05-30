import requests
import requests_mock


def test_simple(requests_mock):
    requests_mock.get('https://developers.zomato.com/api/v2.1/', text='data')
    assert 'data' == requests.get('https://developers.zomato.com/api/v2.1/').text
