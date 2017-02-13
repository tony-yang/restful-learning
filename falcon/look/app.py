import falcon
import images

api = application = falcon.API()

storage_path = './assets'

image_collection = images.Collection(storage_path)
image = images.Item(storage_path)

api.add_route('/images', images_collection)
api.add_route('/images/{name}', image)
