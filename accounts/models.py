from django.db import models
from django.contrib.auth.models import User


class Book(models.Model):
    title = models.CharField(max_length=100, null=False)
    author = models.CharField(max_length=100, null=False)
    price = models.IntegerField(null=False)
    stock = models.IntegerField(null=False)
    genre = models.CharField(max_length=100, null=False)
    description = models.TextField(null=False)
    isbn = models.IntegerField(unique=True, null=False)

    # image = models.ImageField(upload_to='pics')

    def __str__(self):
        return self.title

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    content = models.TextField()

class ProductReview(models.Model):
    product = models.ForeignKey('accounts.Book', on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey('accounts.User', on_delete=models.CASCADE, related_name='reviews')
    review = models.TextField()
    rating = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Product Reviews'

    def __str__(self):
        return self.product.title
    
    def get_rating(self):
        return self.rating

class User(models.Model):
    USER_TYPE_CHOICES = [
        ('admin', 'Admin'),
        ('customer', 'Customer'),
        ('author', 'Author'),
    ]

    user_type = models.CharField(max_length=50, choices=USER_TYPE_CHOICES, default='customer')
    user_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100, null=False)
    last_name = models.CharField(max_length=100, null=False)
    username = models.CharField(max_length=100, null=False)
    email = models.EmailField(max_length=100, null=False)
    password = models.CharField(max_length=100, null=False)
    phone = models.IntegerField(null=False)
    age = models.IntegerField(null=False)
    # address = models.CharField(max_length=200, null=False, default='')
    # account_creation_date = models.DateField(auto_now_add=True, null=False)

    def __str__(self):
        return self.username

# class Cart(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     books = models.ManyToManyField(Book)


class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False)
    order_date = models.DateField(auto_now_add=True, null=False)

    def __str__(self):
        return str(self.order_id)

class Wishlist(models.Model):
    wishlist_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE)
    wishlist_date = models.DateField(auto_now_add=True, null=False)

    def __str__(self):
        return str(self.wishlist_id)

class Posts(models.Model):
    post_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    post_title = models.CharField(max_length=100, null=False)
    post_content = models.TextField(null=False)
    post_date = models.DateField(auto_now_add=True, null=False)

    def __str__(self):
        return str(self.post_id)