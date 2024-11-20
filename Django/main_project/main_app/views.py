from django.shortcuts import render
from django.http import HttpResponse, HttpRequest


# Create your views here.
def print_hello(request):
    return render(request, "main_app/index.html")


"""BOOKS"""


def books(request):
    return render(request, "main_app/books.html")


def top_books(request):
    return render(request, "main_app/top_books.html")


def free_books(request):
    return render(request, "main_app/free_books.html")


def top_free_books(request):
    return render(request, "main_app/top_free_books.html")


def oldschool_books(request):
    return render(request, "main_app/oldschool_books.html")


"""AUTHORS"""


def authors(request):
    return render(request, "main_app/authors.html")


def top_authors(request):
    return render(request, "main_app/top_authors.html")


def ukraine_authors(request):
    return render(request, "main_app/ukraine_authors.html")


def usa_authors(request):
    return render(request, "main_app/usa_authors.html")


def ukraine_top_authors(request):
    return render(request, "main_app/ukraine_top_authors.html")


"""ORDERS"""


def orders(request):
    return render(request, "main_app/orders.html")


def orders_done(request):
    return render(request, "main_app/orders_done.html")


def orders_canceled(request):
    return render(request, "main_app/orders_canceled")
