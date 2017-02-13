import falcon
import images

api = application = falcon.API()

images = images.Resource('./assets')
api.add_route('/images', images)
