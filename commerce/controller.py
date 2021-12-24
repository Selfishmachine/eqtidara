from typing import List

from django.shortcuts import get_object_or_404
from ninja import Router
from pydantic import UUID4
from django.contrib.auth import get_user_model

from account.authorization import GlobalAuth
from commerce.models import unit, Label, Merchant, Vendor, Category, Item
from commerce.schema import unitOut, unitCreate, MessageOut, LabelOut, MerchantOut, CategoryOut, VendorOut


commerce_controller = Router(tags=['products'])
order_controller = Router(tags=['order'])
User = get_user_model()



'''
/api/resource/{id}/

/api/resource?id=&name=&age=

{
    JSON
}
'''


@commerce_controller.get('unit', response={
    200: List[unitOut],
})
def list_units(request):
    products = unit.objects.all()
    # products = products.filter(name='tshirt')
    return products


@commerce_controller.get('unit/{id}', response={
    200: unitOut
})
def retriver_unit(request, id):
    return get_object_or_404(unit, id=id)


@commerce_controller.post('unit', auth=GlobalAuth(), response={
    201: unitOut,
    400: MessageOut
})
def create_unit(request, payload: unitCreate):
    try:
        product = unit.objects.create(**payload.dict(), is_active=True)
    except:
        return 400, {'detail': 'something wrong happened!'}

    return 201, product


@commerce_controller.put('product/{id}', auth=GlobalAuth(), )
def update_employee(request, id, payload: unitCreate):
    product = get_object_or_404(unit, id=id)
    for attr, value in payload.dict().items():
        setattr(product, attr, value)
    product.save()
    return {"success": True}


@commerce_controller.delete('product/{id}', auth=GlobalAuth(), )
def delete_unit(request, id):
    product = get_object_or_404(unit, id=id)
    product.delete()

    return {"success": True}


# create all crud operations for Label, Merchant, Vendor, Category

@commerce_controller.get('Label', response={
    200: List[LabelOut],
})
def list_label(request):
    label = Label.objects.all()
    # label = Label.filter(name='tshirt')
    return label


@commerce_controller.get('Label/{id}', response={
    200: LabelOut
})
def retrieve_Label(request, id):
    return get_object_or_404(Label, id=id)


@commerce_controller.post('Label', auth=GlobalAuth(), response={
    201: LabelOut,
    400: MessageOut
})
def create_Label(request, payload: LabelOut):
    try:
        label = Label.objects.create(**payload.dict())
    except:
        return 400, {'detail': 'something wrong happened!'}

    return 201, label


@commerce_controller.put('Label/{id}', auth=GlobalAuth(), )
def Label_employee(request, id, payload: LabelOut):
    label = get_object_or_404(Label, id=id)
    for attr, value in payload.dict().items():
        setattr(label, attr, value)
    label.save()
    return {"success": True}


@commerce_controller.delete('Label/{id}', auth=GlobalAuth(), )
def delete_label(request, id):
    label = get_object_or_404(Label, id=id)
    label.delete()

    return {"success": True}


# create all crud operations for Label, Merchant, Vendor, Category

@commerce_controller.get('Merchants', response={
    200: List[MerchantOut],
})
def list_Merchants(request):
    merchants = Merchant.objects.all()
    return merchants


@commerce_controller.get('Merchants/{id}', response={
    200: MerchantOut
})
def retrieve_Merchant(request, id):
    return get_object_or_404(Merchant, id=id)


@commerce_controller.post('Merchants', auth=GlobalAuth(), response={
    201: MerchantOut,
    400: MessageOut
})
def create_Merchant(request, payload: MerchantOut):
    try:
        merchant = Merchant.objects.create(**payload.dict())
    except:
        return 400, {'detail': 'something wrong happened!'}

    return 201, merchant


@commerce_controller.put('Merchant/{id}', auth=GlobalAuth(), )
def Merchant_employee(request, id, payload: MerchantOut):
    merchant = get_object_or_404(Merchant, id=id)
    for attr, value in payload.dict().items():
        setattr(merchant, attr, value)
    merchant.save()
    return {"success": True}


@commerce_controller.delete('merchant/{id}', auth=GlobalAuth(), )
def delete_merchant(request, id):
    merchant = get_object_or_404(Merchant, id=id)
    merchant.delete()

    return {"success": True}


# create all crud operations for Label, Merchant, Vendor, Category

@commerce_controller.get('Vendor', response={
    200: List[VendorOut],
})
def list_Vendors(request):
    vendors = Vendor.objects.all()
    return vendors


@commerce_controller.get('Vendors/{id}', response={
    200: VendorOut
})
def retrieve_Vendor(request, id):
    return get_object_or_404(Vendor, id=id)


@commerce_controller.post('Vendors', auth=GlobalAuth(), response={
    201: VendorOut,
    400: MessageOut
})
def create_Vendor(request, payload: VendorOut):
    try:
        vendor = Vendor.objects.create(**payload.dict())
    except:
        return 400, {'detail': 'something wrong happened!'}

    return 201, vendor


@commerce_controller.put('Vendor/{id}', auth=GlobalAuth(), )
def Vendor_employee(request, id, payload: VendorOut):
    vendor = get_object_or_404(Vendor, id=id)
    for attr, value in payload.dict().items():
        setattr(vendor, attr, value)
    vendor.save()
    return {"success": True}


@commerce_controller.delete('Vendor/{id}', auth=GlobalAuth(), )
def delete_Vendor(request, id):
    vendor = get_object_or_404(Vendor, id=id)
    vendor.delete()

    return {"success": True}


# create all crud operations for Label, Merchant, Vendor, Category

@commerce_controller.get('Categorys', response={
    200: List[CategoryOut],
})
def list_Categorys(request):
    categorys = Category.objects.all()
    # Categorys = Categorys.filter(name='tshirt')
    return categorys


@commerce_controller.get('Categorys/{id}', response={
    200: CategoryOut
})
def retrieve_Category(request, id):
    return get_object_or_404(Category, id=id)


@commerce_controller.post('Categorys', auth=GlobalAuth(), response={
    201: CategoryOut,
    400: MessageOut
})
def create_Category(request, payload: CategoryOut):
    try:
        category = Category.objects.create(**payload.dict(), is_active=True)
    except:
        return 400, {'detail': 'something wrong happened!'}

    return 201, category


@commerce_controller.put('Category/{id}', auth=GlobalAuth(), )
def Category_employee(request, id, payload: CategoryOut):
    category = get_object_or_404(Category, id=id)
    for attr, value in payload.dict().items():
        setattr(category, attr, value)
    category.save()
    return {"success": True}


@commerce_controller.delete('Category/{id}', auth=GlobalAuth())
def delete_Category(request, id):
    category = get_object_or_404(Category, id=id)
    category.delete()

    return {"success": True}


