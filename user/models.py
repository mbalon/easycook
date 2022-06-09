from django.db.models import CASCADE, Model, OneToOneField, TextField, ForeignKey, DateField
from django.contrib.auth.models import User



class Profile(Model):
    """ This class is used to create accounts on site """
    user = OneToOneField(User, on_delete=CASCADE)
    biography = TextField(null=True)


class Comment(Model):
    """ This class is used to create recipe comment """
    user = ForeignKey(Profile, on_delete=CASCADE)
    recipe = ForeignKey('recipe.Recipe', on_delete=CASCADE)
    content = TextField()
    date = DateField()
