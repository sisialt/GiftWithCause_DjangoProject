from django import forms
from django.core.exceptions import ValidationError

from GiftWithCause_DjangoProject.gifts.models import Gift


class GiftBaseForm(forms.ModelForm):
    class Meta:
        model = Gift
        exclude = ('creator', )

        labels = {
            'title': 'Title:',
            'image': 'Gift Image URL:',
            'description': 'Description:',
            'price': 'Price:',
        }

        error_messages = {
            'title': {
                'required': 'Title field is required!'
            },
            'image': {
                'required': 'Image URL field is required!'
            },
            'description': {
                'required': 'Description field is required!'
            },
            'price': {
                'required': 'Price field is required!'
            },
        }

    def clean_title(self):
        title = self.cleaned_data.get("title")
        if len(title) < 3:
            raise ValidationError("Title must be at least 3 characters long.")
        return title

    def clean_description(self):
        description = self.cleaned_data.get("description")
        if len(description) < 30:
            raise ValidationError("Description must be at least 30 characters long.")
        return description


class GiftCreateForm(GiftBaseForm):
    pass


class GiftEditForm(GiftBaseForm):
    pass


class GiftDeleteForm(GiftBaseForm):
    class Meta(GiftBaseForm.Meta):
        widgets = {
            'title': forms.TextInput(attrs={"readonly": "readonly"}),
            'image': forms.TextInput(attrs={"readonly": "readonly"}),
            'description': forms.TextInput(attrs={"readonly": "readonly"}),
            'price': forms.TextInput(attrs={"readonly": "readonly"}),
        }
