import graphene
from graphene.test import Client

from main import Query

client = Client(schema=graphene.Schema(query=Query))


def test_get_first_n_pokemons():
    executed = client.execute('''{ pokemons(first:5) { name } }''')
    assert executed == {
        "data": {
            "pokemons": [
                {
                    "name": "Bulbasaur"
                },
                {
                    "name": "Ivysaur"
                },
                {
                    "name": "Venusaur"
                },
                {
                    "name": "Charmander"
                },
                {
                    "name": "Charmeleon"
                }]
        }
    }


def test_pokemon_sort_asc():
    executed = client.execute('''{pokemons(asc:true, first: 3) { name } }''')
    assert executed == {
        "data": {
            "pokemons": [
                {
                    "name": "Bulbasaur"
                },
                {
                    "name": "Ivysaur"
                },
                {
                    "name": "Venusaur"
                }
            ]
        }
    }

def test_pokemon_sort_desc():
    executed = client.execute('''{pokemons(desc:true, first: 3) { name } }''')
    assert executed == {
        "data": {
            "pokemons": [
                {
                    "name": "Venusaur"
                },
                {
                    "name": "Ivysaur"
                },
                {
                    "name": "Bulbasaur"
                }
            ]
        }
    }

def test_get_pokemon_by_name():
    executed = client.execute('''{ pokemon(name:"Ivysaur") { name }}''')
    assert executed == {
        "data": {
            "pokemon": {
                "name": "Ivysaur"
            }
        }
    }


def test_get_pokemon_by_id():
    executed = client.execute('''{ pokemon(id:"UG9rZW1vbjowNzk=") { id }}''')
    assert executed == {
        "data": {
            "pokemon": {
                "id": "UG9rZW1vbjowNzk="
            }
        }
    }
