from django import forms

from GiftWithCause_DjangoProject.comments.models import Comment


class CommentBaseForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text', ]
        #
        # labels = {
        #     'title': 'Title:',
        #     'image': 'Gift Image URL:',
        #     'up_to_price': 'Price:',
        # }

        widgets = {
            'text': forms.TextInput(attrs={"placeholder": "Write your comment here..."}),
        }

        # error_messages = {
        #     'title': {
        #         'required': 'Title field is required!'
        #     },
        # }


class CommentCreateForm(CommentBaseForm):
    pass


class CommentEditForm(CommentBaseForm):
    pass


class CommentDeleteForm(CommentBaseForm):
    class Meta(CommentBaseForm.Meta):
        widgets = {
            'text': forms.TextInput(attrs={"readonly": "readonly"}),
        }
