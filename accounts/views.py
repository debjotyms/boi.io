from django.shortcuts import render, redirect, get_object_or_404
from . models import User
from . models import Book
from django.db import connection
from .forms import RegisterForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login as loginUser, logout as logoutUser
from django.contrib.auth.decorators import login_required
from cart.carts import Cart
from accounts.forms import ProductReviewForm
from .forms import ReviewForm
from .models import Review

def thanks(request):
    return render(request, 'pages/thankyou.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            loginUser(request, user)
            return redirect('home')
        else:
            print('Incorrect')
            messages.warning(request, 'Username or password is incorrect')
    
    return render(request, 'login.html')

def logout(request):
    logoutUser(request)
    messages.info(request, 'Logged Out!')
    return redirect('login')

def create_user():
    name = 'rasel'
    with connection.cursor() as cursor:
        cursor.execute(f"""
            INSERT INTO accounts_user (user_type, first_name, last_name, username, email, password, phone, age, account_creation_date)
            VALUES ('customer', '{name}', 'Doe', 'johndoe', 'johndoe@example.com', 'password123', 1234567890, 30, '2022-01-01')
        """)

def signup(request):
    # This can be useful for storing orders in the database
    # if request.method == 'POST':
    #     first_name = request.POST.get('first_name')
    #     last_name = request.POST.get('last_name')
    #     username = request.POST.get('username')
    #     email = request.POST.get('email')
    #     password = request.POST.get('password')
    #     phone = request.POST.get('phone')
    #     age = request.POST.get('age')

    #     print(first_name, last_name, username, email, password, phone, age)

    #     with connection.cursor() as cursor:
    #         cursor.execute(f"""
    #             INSERT INTO accounts_user (user_type, first_name, last_name, username, email, password, phone, age)
    #             VALUES ('customer', '{first_name}', '{last_name}', '{username}', '{email}', '{password}', {phone}, {age})
    #         """)

    #     return render(request, 'home.html')
    # else:
    #     return render(request, 'signup.html')

    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"Account created for {username}!")
            return redirect('login')
    
    contex = {'form': form}
    return render(request, 'signup.html', contex)

def sent(request):
    return render(request, 'sent.html')

def reset(request):
    return render(request, 'reset.html')

@login_required(login_url='login')
def posts(request):
    return render(request, 'posts.html')

@login_required(login_url='login')
def home(request):
    return render(request, 'home.html')

@login_required(login_url='login')
def addbook(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        price = request.POST.get('price')
        stock = request.POST.get('stock')
        genre = request.POST.get('genre')
        description = request.POST.get('description')
        isbn = request.POST.get('isbn')
        # image = request.FILES.get('image')

        print(title, author, isbn, price, stock, description)

        with connection.cursor() as cursor:
            cursor.execute(f"""
                INSERT INTO accounts_book (title, author, price, stock, genre, description, isbn) 
                VALUES ('{title}', '{author}', {price}, {stock}, '{genre}', '{description}', {isbn})
            """)

        return render(request, 'addbook.html')
    else:
        return render(request, 'addbook.html')

def product(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    reviews = Review.objects.filter(book=book)
    form = ReviewForm()

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.book = book
            review.save()
            return redirect('product', book_id=book.id)

    return render(request, 'product.html', {'book': book, 'reviews': reviews, 'form': form})

@login_required(login_url='login')
def books(request):
    if 'q' in request.GET:
        q = request.GET['q']
        books = Book.objects.raw('''SELECT * FROM book_book 
                                    WHERE title LIKE %s''', 
                                    ['%' + q + '%'])
        books = Book.objects.filter(title__icontains=q)
    else:
        books = Book.objects.all()
    return render(request, 'books.html', locals())

from django.db import connection