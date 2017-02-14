from pyramid.config import Configurator

def main(global_config, **settings):
    config = Configurator(settings=settings)
    config.add_route('strings', '/strings/{name}')
    config.scan('.views')
    return config.make_wsgi_app()
