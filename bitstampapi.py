import httplib2
import urllib
import json

class   bitstampapi:

    def __init__(self):
        self.key = ''
        self.secret = ''
        self.signature = ''
        self.uri = 'https://www.bitstamp.net/api'

    def public_request(self, method, body={}):
        h = httplib2.Http()
        resp, content = h.request(self.uri + '/' + method + '/', 'GET', body=urllib.parse.urlencode(body));
        if resp['status'] == '200':
            data = json.loads(content.decode())
            return(data)
        print('[ERROR]: http request failed => ' + resp['status'])
        return(None)

    def ticker(self):
        data = self.public_request('ticker');
        if data:
            return(data)
        return(None)

    def order_book(self, group=1):
        body = {}
        body['group'] = group
        data = self.public_request('order_book', body)
        if data:
            return(data)
        return(None)
