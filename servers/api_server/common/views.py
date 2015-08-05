from flask_restful import reqparse, Resource, abort
from neomodel.exception import DoesNotExist
from api_server.authentication import requires_auth


class BaseView(Resource):
    model = None
    fields = {}
    input_fields = None

    def _parse_arguments(self):
        fields = self.input_fields or self.fields

        parser = reqparse.RequestParser(bundle_errors=True)

        for name, info in fields.iteritems():
            argument_data = {
                'name': name
                , 'type': info.get('type', str)
                , 'required': info.get('required', False)
                , 'dest': info.get('dest', None)  # Nome da chave criada no objeto
                , 'default': info.get('default', None)
                , 'help': info.get('help', None)
                , 'choices': info.get('choices', None)  # Define lista de valores validos
                , 'case_sensitive': info.get('case_sensitive', True)
                , 'trim': info.get('trim', True)
                , 'store_missing': info.get('store_missing', True)
            }

            parser.add_argument(**argument_data)
        return parser.parse_args()

    def serialize(self, node):
        return {field: getattr(node, field) for field in self.fields}

class BaseListView(BaseView):
    @requires_auth
    def get(self):
        return [self.serialize(node) for node in self.model.nodes]

    @requires_auth
    def post(self):
        args = self._parse_arguments()
        node = self.model(**args).save()

        return self.serialize(node), 201


class BaseDetailView(BaseView):
    @requires_auth
    def patch(self, pk):
        args = self._parse_arguments()
        pk_field = self.model.pk_field  # 'name'

        try:
            node = self.model.nodes.get(**{pk_field: pk})  # {'name': pk}

        except DoesNotExist:
            abort(404)

        for field, value in args.items():
            setattr(node, field, value)
        node.save()
        return self.serialize(node)

    @requires_auth
    def get(self, pk):
        pk_field = self.model.pk_field  # 'name'

        try:
            node = self.model.nodes.get(**{pk_field: pk})  # {'name': pk}
        except DoesNotExist:
            abort(404)

        return {field: getattr(node, field) for field in self.fields}

    @requires_auth
    def delete(self, pk):
        pk_field = self.model.pk_field  # 'name'

        try:
            node = self.model.nodes.get(**{pk_field: pk})  # {'name': pk}
        except DoesNotExist:
            abort(404)

        node.delete()
        return {field: getattr(node, field) for field in self.fields}
