from django import forms
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
