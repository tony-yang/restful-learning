from pyramid.view import view_config

class ReadViews:
    def __init__(self, request):
        self.request = request

    @view_config(route_name='reads', renderer='json')
    def reads(self):
        value = "{'AAAA':'BBBBBBBBB,CCCC,DDDD,EEEE,FFFF,GGGGGGGG'}"
        return value
