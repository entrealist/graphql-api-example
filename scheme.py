from graphene import ObjectType, String, Field, Int, List, Boolean



class Evolutions(ObjectType):
    id = String()
    number = String()
    name = String()
    maxCP = Int()
    maxHP = Int()
    image = String()
    types = List(String)


class Special(ObjectType):
    name = String()
    damage = Int()


class Fast(ObjectType):
    name = String()
    damage = Int()


class Attacks(ObjectType):
    fast = List(Fast)
    special = List(Special)


class Pokemon(ObjectType):
    id = String()
    number = String()
    name = String()
    maxCP = Int()
    maxHP = Int()
    image = String()
    types = List(String)
    attacks = Field(Attacks)
    evolutions = List(Evolutions)


class RootType(ObjectType):
    pokemons = Field(Pokemon)