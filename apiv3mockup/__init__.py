from pyramid.config import Configurator
import pyramid_jsonapi
from . import models
import alchemyjsonschema
from sqlalchemy.dialects.postgresql import UUID, JSONB

alchemyjsonschema.default_column_to_schema.update(
    {
        UUID: "string",
        JSONB: "string"
    }
)


def verify_secret(view, obj):
    return obj


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
    pj.append_callback_set_to_all_views(
        'access_control_serialised_objects')
    pj.metadata.JSONSchema.build_definitions()
    return config.make_wsgi_app()
