class Planet:
    def __init__(self, id, name, description, signs_of_life=None):
        self.id = id
        self.name = name
        self.description = description
        self.signs_of_life = signs_of_life

planets = [
    Planet(1, "HD 189773b", "rains glass side ways", False),
    Planet(2, "K2-18b", "where a swim may vaporise you", False),
    Planet(3, "WASP-107 b", "the puffy marshmallow planet", True)
]

