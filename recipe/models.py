from django.db.models import (
    Model,
    CharField,
    IntegerField,
    TextField,
    ImageField,
    ForeignKey,
    CASCADE,
    DO_NOTHING
)

from easycook.user.models import Profile


class FoodType(Model):
    """ This class is used to describe type of ingredient e.x. vegetables, meat"""

    name = CharField(max_length=20)

    def __str__(self):
        return self.name


class Ingredient(Model):
    """ This class is used to describe ingredients use in recipe e.x. carrot, bread"""

    name = CharField(max_length=30, unique=True)
    kcal = IntegerField()
    type = ForeignKey(FoodType, on_delete=CASCADE)

    def __str__(self):
        return self.name


class Recipe(Model):
    """ This class is used to describe recipe """

    name = CharField(max_length=40, unique=True)
    description = TextField()
    time_to_prepare = CharField(max_length=15)
    picture = ImageField(null=True)
    author = ForeignKey(Profile, on_delete=DO_NOTHING)

    def __str__(self):
        return self.name


class Composition(Model):
    """ This class join ingredients list with recipe """

    ingredient = ForeignKey(Ingredient, on_delete=CASCADE)
    recipe = ForeignKey(Recipe, on_delete=CASCADE)
    quantity = CharField(max_length=40, default=0)
