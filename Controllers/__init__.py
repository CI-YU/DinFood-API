from flask_restplus import Api

from .user import ns as ns1
from .example import ns as ns2
api = Api(
    title='My Title',
    version='1.0',
    description='A description',
    # All API metadatas
)

api.add_namespace(ns1)
api.add_namespace(ns2)