from django import forms

from GiftWithCause_DjangoProject.comments.models import Comment


class CommentBaseForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text', ]

        widgets = {
            'text': forms.TextInput(attrs={"placeholder": "Write your comment here..."}),
        }


class CommentCreateForm(CommentBaseForm):
    pass


class CommentDeleteForm(CommentBaseForm):
    class Meta(CommentBaseForm.Meta):
        widgets = {
            'text': forms.TextInput(attrs={"readonly": "readonly"}),
        }
