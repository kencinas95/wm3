from django import template
from common.models.item import Item, ItemImage

register = template.Library()


@register.simple_tag
def item_image_path(item: Item) -> str:
    image: ItemImage = item.itemimage_set.filter(thumbnail=1)[0]
    return image.path.url


