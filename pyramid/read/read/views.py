from pyramid.view import view_config
from pyramid.response import Response

class ReadViews:
    def __init__(self, request):
        self.request = request

    @view_config(route_name='reads', renderer='json')
    def reads(self):
        value = "{'AAAA':'BBBBBBBBB,CCCC,DDDD,EEEE,FFFF,GGGGGGGG'}"
        response = Response(body=value, status=200, content_type='application/json', charset='UTF-8')
        return value
