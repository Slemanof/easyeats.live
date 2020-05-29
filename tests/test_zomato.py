import responses
import requests

@responses.activate
def test_simple():
    responses.add(responses.GET, 'https://developers.zomato.com/api/v2.1/',
                  json={'error': 'not found'}, status=404)

    resp = requests.get('https://developers.zomato.com/api/v2.1/%27')

    assert resp.json() == {"error": "not found"}

    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == 'https://developers.zomato.com/api/v2.1/'
    assert responses.calls[0].response.text == '{"error": "not found"}'