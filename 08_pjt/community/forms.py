from django import forms
from .models import Review, Comment, Reply


class ReviewForm(forms.ModelForm):
    
    class Meta:
        model = Review
        fields = ['title', 'movie_title', 'rank', 'content']


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        exclude = ['review', 'user','like_users']

class ReplyForm(forms.ModelForm):

    class Meta:
        model = Reply
        fields = ['content',]