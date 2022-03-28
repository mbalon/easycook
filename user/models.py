from django.db.models import CASCADE, Model, OneToOneField, TextField, ForeignKey, DateField
from django.contrib.auth.models import User

from easycook.recipe.models import Recipe


class Profile(Model):
    """ This class is used to create accounts on site"""
    user = OneToOneField(User, on_delete=CASCADE)
    biography = TextField(null=True)


class Comment(Model):
    """ This class is used to create recipe comment"""
    user = ForeignKey(Profile)
    recipe = ForeignKey(Recipe)
    content = TextField()
    date = DateField()
