import neomodel as nm
from server.common.views import BaseView
from flask_restful import abort


""" MODEL """
class ParentModel(nm.StructuredNode):
    name = nm.StringProperty(unique_index=True)
    age = nm.IntegerProperty()
    # partner = nm.RelationshipFrom('ParentModel', 'PARTNER', cardinality=nm.One)


""" VIEWS """
class ParentListView(BaseView):
    model = ParentModel
    fields = {
        'name': {'required': True}
        , 'age': {'type': int, 'required': True}
    }

    def get(self):
        all_parents = []

        for parent in ParentModel.nodes:
            # Isso é o tipo de coisa que a gente faria um serializador :)
            all_parents.append({'name': parent.name, 'age':parent.age})

        return all_parents

    def post(self):
        args = self._parse_arguments()
        node = self.model(**args).save()
        return {'name': node.name, 'age':node.age}, 201

class ParentDetailView(ParentListView):
    def get(self, name):

        parent = ParentModel.nodes.get(name=name)

        if not parent:
            abort(404)

        return {'name': parent.name, 'age':parent.age}