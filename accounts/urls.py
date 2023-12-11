from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('sent/', views.sent, name='sent'),
    path('reset/', views.reset, name='reset'),
    path('home/', views.home, name='home'),
    path('books/', views.books, name='books'),
    path('addbook/', views.addbook, name='addbook'),
    path('posts/', views.posts, name='posts'),
    path('thanks/', views.thanks, name='thanks'),
    path('product/<int:book_id>/', views.product, name='product'),
]