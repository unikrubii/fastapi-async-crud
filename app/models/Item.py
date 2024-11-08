from tortoise.models import Model
from tortoise import fields

class Item(Model):
    id = fields.IntField(primary_key=True)
    name = fields.TextField()
    description = fields.TextField()

    def __str__(self):
        return self.name
