from django import forms
from GiftWithCause_DjangoProject.gift_searches.models import GiftSearch


class GiftSearchBaseForm(forms.ModelForm):
    class Meta:
        model = GiftSearch
        exclude = ('user', )

        labels = {
            'title': 'Title:',
            'image': 'Gift Image URL:',
            'up_to_price': 'Price:',
        }

        error_messages = {
            'title': {
                'required': 'Title field is required!'
            },
        }


class GiftSearchCreateForm(GiftSearchBaseForm):
    pass


class GiftSearchEditForm(GiftSearchBaseForm):
    pass


class GiftSearchDeleteForm(GiftSearchBaseForm):
    class Meta(GiftSearchBaseForm.Meta):
        widgets = {
            'title': forms.TextInput(attrs={"readonly": "readonly"}),
            'image': forms.TextInput(attrs={"readonly": "readonly"}),
            'up_to_price': forms.TextInput(attrs={"readonly": "readonly"}),
        }
