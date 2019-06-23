from operator import attrgetter

import graphene
import requests
from fastapi import FastAPI
from starlette.graphql import GraphQLApp

from scheme import *
from utils import json2obj

ENDPOINT = 'https://storage.googleapis.com/development-data/recruitment/pokemons.json'
obj = json2obj(requests.get(url=ENDPOINT).text)


class Query(ObjectType):
    pokemons = List(Pokemon, first=Int(), asc=Boolean(), desc=Boolean())
    pokemon = Field(Pokemon, id=String(), name=String())

    def resolve_pokemon(self, info, id=None, name=None, **kwargs):
        answer = obj.pokemons
        if name:
            for pkm in answer:
                if pkm.name == name:
                    answer = pkm
        elif id:
            for pkm in answer:
                if pkm.id == id:
                    answer = pkm
        return answer

    def resolve_pokemons(self, info, first=None, asc=None, desc=None, **kwargs):
        answer = obj.pokemons
        if first:
            answer = answer[:first]
        if asc:
            answer = sorted(answer, key=attrgetter('name'))
        if desc:
            answer = sorted(answer, key=attrgetter('name'), reverse=True)
        return answer


app = FastAPI()
app.add_route("/", GraphQLApp(schema=graphene.Schema(query=Query)))
