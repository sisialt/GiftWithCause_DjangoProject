from django import forms
from django.core.exceptions import ValidationError

from GiftWithCause_DjangoProject.gift_searches.models import GiftSearch


class GiftSearchBaseForm(forms.ModelForm):
    class Meta:
        model = GiftSearch
        exclude = ('user', )

        labels = {
            'title': 'Title:',
            'image': 'Gift Image URL:',
            'up_to_price': 'Up To Price:',
        }

        error_messages = {
            'title': {
                'required': 'Title field is required!'
            },
        }

    def clean_title(self):
        title = self.cleaned_data.get("title")
        if len(title) < 3:
            raise ValidationError("Title must be at least 3 characters long.")
        return title


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
