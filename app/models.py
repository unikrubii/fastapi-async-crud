from tortoise.models import Model
from tortoise import fields
from tortoise.contrib.pydantic import pydantic_model_creator

class Item(Model):
    id = fields.IntField(primary_key=True)
    name = fields.TextField()
    description = fields.TextField()

    def __str__(self):
        return f'Item [{self.id}]: {self.name} - {self.description}'

Item_Pydantic = pydantic_model_creator(Item, name='Item')
ItemIn_Pydantic = pydantic_model_creator(Item, name='ItemIn', exclude_readonly=True)
ItemOut_Pydantic = pydantic_model_creator(Item, name='ItemOut', include=['id'])
