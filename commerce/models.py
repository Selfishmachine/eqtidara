import uuid

from PIL import Image
from django.contrib.auth import get_user_model
from django.db import models

from eqdja.utils.models import Entity

User = get_user_model()


class unit(Entity):
    name = models.CharField(verbose_name='name', max_length=255)
    description = models.TextField('description', null=True, blank=True)
    phone = models.CharField('phone',max_length=12)
    unit_image=models.ImageField(null=True ,blank=True,upload_to="images/")
    size = models.FloatField('size', null=True, blank=True)
    location=models.TextField('location', null=True, blank=True)
    room = models.IntegerField()
    bathroom = models.IntegerField()
    garden = models.BooleanField()
    price = models.DecimalField('price', max_digits=10, decimal_places=2)
    vendor = models.ForeignKey('commerce.Vendor', verbose_name='vendor', related_name='unit',
                               on_delete=models.SET_NULL,
                               null=True, blank=True)
    category = models.ForeignKey('commerce.Category', verbose_name='category', related_name='products',
                                 null=True,
                                 blank=True,
                                 on_delete=models.SET_NULL)
    merchant = models.ForeignKey('commerce.Merchant', verbose_name='merchant', related_name='products',
                                 null=True,
                                 blank=True,
                                 on_delete=models.SET_NULL)
    is_featured = models.BooleanField('is featured')
    is_active = models.BooleanField('is active')
    label = models.ForeignKey('commerce.Label', verbose_name='label', related_name='products', null=True, blank=True,
                              on_delete=models.CASCADE)


    def __str__(self):
        return self.name





class Category(Entity):
    parent = models.ForeignKey('self', verbose_name='parent', related_name='children',
                               null=True,
                               blank=True,
                               on_delete=models.CASCADE)
    name = models.CharField('name', max_length=255)
    description = models.TextField('description')
    image = models.ImageField('image', upload_to='category/')
    is_active = models.BooleanField('is active')

    created = models.DateField(editable=False, auto_now_add=True)
    updated = models.DateTimeField(editable=False, auto_now=True)

    def __str__(self):
        if self.parent:
            return f'-   {self.name}'
        return f'{self.name}'

    class Meta:
        verbose_name_plural = 'Categories'
        verbose_name = 'Category'

    @property
    def children(self):
        return self.children





class Merchant(Entity):
    name = models.CharField('name', max_length=255)

    def __str__(self):
        return self.name


class ProductImage(Entity):
    image = models.ImageField('image', upload_to='product/')
    is_default_image = models.BooleanField('is default image')
    product = models.ForeignKey('commerce.unit', verbose_name='product', related_name='images',
                                on_delete=models.CASCADE)

    def __str__(self):
        return str(self.product.name)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)
        if img.height > 500 or img.width > 500:
            output_size = (500, 500)
            img.thumbnail(output_size)
            img.save(self.image.path)
            # print(self.image.path)


class Label(Entity):
    name = models.CharField('name', max_length=255)

    class Meta:
        verbose_name = 'label'
        verbose_name_plural = 'labels'

    def __str__(self):
        return self.name


class Vendor(Entity):
    name = models.CharField('name', max_length=255)
    image = models.ImageField('image', upload_to='vendor/')

    def __str__(self):
        return self.name

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)
        if img.height > 500 or img.width > 500:
            output_size = (500, 500)
            img.thumbnail(output_size)
            img.save(self.image.path)
            # print(self.image.path)


class City(Entity):
    name = models.CharField('city', max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'city'
        verbose_name_plural = 'cities'


class Address(Entity):
    user = models.ForeignKey(User, verbose_name='user', related_name='address',
                             on_delete=models.CASCADE)
    work_address = models.BooleanField('work address', null=True, blank=True)
    address1 = models.CharField('address1', max_length=255)
    address2 = models.CharField('address2', null=True, blank=True, max_length=255)
    city = models.ForeignKey(City, related_name='addresses', on_delete=models.CASCADE)
    phone = models.CharField('phone', max_length=255)

    def __str__(self):
        return f'{self.user.first_name} - {self.address1} - {self.address2} - {self.phone}'


class Item:
    pass