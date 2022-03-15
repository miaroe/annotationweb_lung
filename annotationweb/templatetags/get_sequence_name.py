import os.path

from django import template

register = template.Library()

@register.filter
def get_sequence_name(image_sequence_format):
    """ Get the sequence name from an ImageSequence format string """
    path = os.path.dirname(image_sequence_format)
    sequence_dir = os.path.basename(path)
    return sequence_dir
