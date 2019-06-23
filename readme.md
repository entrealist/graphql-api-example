# GraphQL Pockemons API Example

A simple example of fetching from remote source and GraphQL API implementation
_

### Requirements
- Python 3.6
- Virtualenv
- FastAPI 
- Scarlette
- Graphene
- Uvicorn

### Installation

Clone project to your environment, then dive into project folder

```pip3 install -r requirements.txt```

### How to run:
```
uvicorn main:app --reload
```
Visit http://127.0.0.1:8000 to GraphiQL Dashboard

#### Queries usage:
In dashboard press ```CTRL + SPACE``` to see all possible fields.
Press ```CTRL + ENTER``` to make query.

Pokemons
```GraphQl
{
  pokemons(asc: true, first: 2) {
    name
    id
    number
    maxCP
    maxHP
    image
    types
    attacks {
      fast {
        name
        damage
      }
      special {
        name
        damage
      }
    }
    evolutions {
      id
      number
      name
      maxCP
      maxHP
      image
      types
    }
  }
}

```

Pokemon
```GraphQl
{
  pokemon(name: "Pikachu") {
    name
    id
    number
    maxCP
    maxHP
    image
    types
  }
}

```
