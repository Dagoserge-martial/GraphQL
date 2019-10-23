import graphene
from graphene_django import DjangoObjectType
from .models import *
from graphene_django.filter import DjangoFilterConnectionField
from graphql_relay.node.node import from_global_id

class VilleNode(DjangoObjectType):
    class Meta:
        model = Ville
        filter_fields = ['name']
        interfaces = (graphene.relay.Node,)

class TitreNode(DjangoObjectType):
    class Meta:
        model = Titre
        filter_fields = ['name']
        interfaces = (graphene.relay.Node,)

class EmployeNode(DjangoObjectType):
    class Meta:
        model = Employe
        filter_fields = { 
              'name': ['exact', 'icontains', 'istartswith'],
              'ville': ['exact'],
              'titre': ['exact'],
              'ville__name': ['exact'],
              'titre__name': ['exact'],
            }
        interfaces = (graphene.relay.Node,)

class CreateTitre(graphene.relay.ClientIDMutation):
    titre = graphene.Field(TitreNode)

    class Input:
        name = graphene.String()

    def mutate_and_get_payload(root, info, **input):
        titre = Titre(
            name=input.get('name')
        )
        titre.save()
        return CreateTitre(titre=titre)

class CreateVille(graphene.relay.ClientIDMutation):
    ville = graphene.Field(VilleNode)

    class Input:
        name = graphene.String()

    def mutate_and_get_payload(root, info, **input):
        ville = Ville(
            name=input.get('name')
        )
        ville.save()
        return CreateVille(ville=ville)

class CreateEmploye(graphene.relay.ClientIDMutation):
    employe = graphene.Field(EmployeNode)

    class Input:
        name = graphene.String()
        ville = graphene.String()
        titre = graphene.String()

    def mutate_and_get_payload(root, info, **input):
        employe = Employe(
            name=input.get('name'),
            ville = Ville.objects.get(name=input.get('ville')),
            titre = Titre.objects.get(name=input.get('titre')) 
        )
        employe.save()
        return CreateEmploye(employe=employe)

class UpdateEmploye(graphene.relay.ClientIDMutation):
    employe = graphene.Field(EmployeNode)

    class Input:
        id = graphene.String()
        name = graphene.String()
        ville = graphene.String()
        titre = graphene.String()
        
    def mutate_and_get_payload(root, info, **input):
        employe = Employe.objects.get(
            pk=from_global_id(input.get('id'))[1])
        employe.name = input.get('name'),
        # employe.ville = Ville.objects.get(ville=input.get('ville')),
        # employe.titre = Titre.objects.get(name=input.get('titre'))
        employe.save()

        return UpdateEmploye(employe=employe)

class DeleteEmploye(graphene.relay.ClientIDMutation):
    employe = graphene.Field(EmployeNode)

    class Input:
        id = graphene.String()
        
    def mutate_and_get_payload(root, info, **input):
        employe = Employe.objects.get(
            pk=from_global_id(input.get('id'))[1])
        employe.delete()

        return DeleteEmploye(employe=employe)

class Query(object):
    ville = graphene.relay.Node.Field(VilleNode)
    all_villes = DjangoFilterConnectionField(VilleNode)

    titre = graphene.relay.Node.Field(TitreNode)
    all_titres = DjangoFilterConnectionField(TitreNode)

    employe = graphene.relay.Node.Field(EmployeNode)
    all_employes = DjangoFilterConnectionField(EmployeNode)

class Mutation(graphene.AbstractType):
    create_titre = CreateTitre.Field()
    create_ville = CreateVille.Field()
    create_employe = CreateEmploye.Field()
    update_employe = UpdateEmploye.Field()
    delete_employe = DeleteEmploye.Field()
