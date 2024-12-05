from django import forms


class SearchForm(forms.Form):
    gift = forms.CharField(
        required=False,
        label='',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'What gift are you searching for...',
            }
        )
    )
