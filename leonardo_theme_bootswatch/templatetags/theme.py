import random

from django import template
from django.conf import settings
from leonardo.module.media.models import Folder, Image

register = template.Library()


@register.assignment_tag
def get_random_background():
    folder, created = Folder.objects.get_or_create(name=getattr(settings,
                                                                'THEME_BACKGROUND_FOLDER',
                                                                'backgrounds'))
    images = folder.media_file_files.instance_of(Image)
    if images:
        return random.choice(images)
