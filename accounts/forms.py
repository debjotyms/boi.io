from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from accounts.models import ProductReview
from .models import Review


class ProductReviewForm(forms.ModelForm):
    review = forms.CharField(widget=forms.Textarea(attrs={'placeholder': "Write Review"}))

    class Meta:
        model = ProductReview
        fields = ['review', 'rating']


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email']


# forms.py


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['content']
