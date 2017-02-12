import falcon

class ThingsResource(object):
    def on_get(self, req, resp):
        '''Handles GET requests'''
        resp.status = falcon.HTTP_200
        resp.body = ('\n2thing awe most'
                    'above me and \n'
                    '\n'
                    '   ~ ABC\n\n')
app = falcon.API()
things = ThingsResource()
app.add_route('/things', things)
