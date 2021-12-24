from typing import List

from ninja import ModelSchema, Schema
from ninja.orm import create_schema
from pydantic import UUID4

from commerce.models import unit, Merchant


class MessageOut(Schema):
    detail: str
class unitCreate(Schema):
    name:str
    discription:str
    image:str
    size:int
    price:int
    vendor:str
    room:int
    bathroom:int


class imageOut(Schema):

      imageOut:str

class UUIDSchema(Schema):
    id: UUID4


# ProductSchemaOut = create_schema(Product, depth=2)

class VendorOut(UUIDSchema):
    name: str
    image: str


class LabelOut(UUIDSchema):
    name: str


class MerchantOut(ModelSchema):
    class Config:
        model = Merchant
        model_fields = ['id', 'name']


class CategoryOut(UUIDSchema):
    name: str
    description: str
    image: str
    children: List['CategoryOut'] = None


CategoryOut.update_forward_refs()


class unitOut(ModelSchema):
    vendor: VendorOut
    label: LabelOut
    merchant: MerchantOut
    category: CategoryOut

    class Config:
        model = unit
        model_fields = ['id',
                        'name',
                        'description',
                        'room',
                        'price',
                        'garden',
                        'vendor',
                        'category',
                        'label',
                        'merchant',

                        ]


# class ProductManualSchemaOut(Schema):
#     pass


class CitySchema(Schema):
    name: str


class CitiesOut(CitySchema, UUIDSchema):
    pass



