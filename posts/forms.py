from django import forms

from posts.models import Post


class NewPostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'intro', 'body', 'image', 'status', 'categories', 'publication_date']
