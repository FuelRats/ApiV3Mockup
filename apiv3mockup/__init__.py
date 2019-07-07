from pyramid.config import Configurator
import pyramid_jsonapi
from . import models


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    config.include('pyramid_jinja2')
    config.include('.models')
    config.include('.routes')
    config.scan()
    pj = pyramid_jsonapi.PyramidJSONAPI(config, models)
    pj.create_jsonapi_using_magic_and_pixie_dust()
    return config.make_wsgi_app()
