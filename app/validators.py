from django.core.exceptions import ValidationError
from django.utils.html import strip_tags

def starting_with_space_input(textfield):
    cleaned_data = strip_tags(textfield)
    if cleaned_data == "":
        raise ValidationError("Please fill in this field")