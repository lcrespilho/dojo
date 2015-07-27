from flask_restful import reqparse
from flask_restful import Resource

class BaseView(Resource):
    fields = {}

    def _parse_arguments(self):
        fields = self.fields

        parser = reqparse.RequestParser(bundle_errors=True)

        for name, info in fields.iteritems():
            argument_data = {
                'name': name
                , 'type': info.get('type', str)
                , 'required': info.get('required', False)
                , 'dest': info.get('dest', None) # Nome da chave criada no objeto
                , 'default': info.get('default', None)
                , 'help': info.get('help', None)
                , 'choices': info.get('choices', None) # Define lista de valores validos
                , 'case_sensitive': info.get('choices', False)
                , 'trim': info.get('trim', True)
                , 'store_missing': info.get('store_missing', True)
            }

            parser.add_argument(**argument_data)
        return parser.parse_args()
