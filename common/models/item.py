from django.db import models
from django.core.validators import MinValueValidator


__all__ = [
    'OriginCategory',
    'Origin',
    'ItemCategory',
    'Item',
    'ItemImage',
    'Stock'
]


class OriginCategory(models.Model):
    """
    Origin category model.

    Each origin must have a category.
    """
    code = models.CharField(max_length=10, unique=True, primary_key=True, null=False, blank=False)
    description = models.CharField(max_length=25)

    class Meta:
        db_table = "wm_item_origin_category"
        managed = False


class Origin(models.Model):
    """
    Origin model.

    Each item must have an origin.
    """
    id: int = models.AutoField(primary_key=True)
    category = models.ForeignKey(OriginCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=150, unique=True)

    class Meta:
        db_table = "wm_item_origin"
        managed = False


class ItemCategory(models.Model):
    """
    Item category model.

    Each item must have a category.
    """
    code = models.CharField(max_length=25, primary_key=True, unique=True, null=False, blank=False)
    description = models.CharField(max_length=50, unique=True, null=False, blank=False)

    class Meta:
        db_table = 'wm_item_category'
        managed = False
        ordering = ['-code']


class Item(models.Model):
    """
    Item model.
    """
    id: int = models.AutoField(primary_key=True)
    category = models.ForeignKey(ItemCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    price = models.DecimalField(decimal_places=2, max_digits=10, validators=[MinValueValidator(1.0)])
    highlighted = models.BooleanField(default=True)
    views = models.PositiveIntegerField(default=0)
    sales = models.PositiveIntegerField(default=0)
    creation_date = models.DateField(auto_now_add=True)
    origin = models.ForeignKey(Origin, on_delete=models.CASCADE)

    class Meta:
        db_table = 'wm_item'
        managed = False
        ordering = ['-id']

    @staticmethod
    def item_image_directory(instance, filename: str) -> str:
        """
        Path to the upload storage for images.

        :param instance: ItemImage instance
        :param filename: filename to be saved
        :return: upload to path
        """
        return f"/item/{instance.item.id}/{filename}"


class ItemImage(models.Model):
    """
    Item linked image model.

    Each item must have at least one linked image.
    """
    item: Item = models.ForeignKey(Item, on_delete=models.CASCADE)
    thumbnail = models.BooleanField()
    path = models.FileField(upload_to=Item.item_image_directory)
    mime_type = models.CharField(max_length=50)

    class Meta:
        db_table = 'wm_item_image'
        managed = False


class Stock(models.Model):
    """
    Item stock model.

    Stock of items.
    """
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    stock = models.PositiveIntegerField()
    update_date = models.DateField(auto_now_add=True)
    last_buy_date = models.DateTimeField()

    class Meta:
        db_table = 'wm_item_stock'
        managed = False

