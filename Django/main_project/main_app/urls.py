from django.urls import path
from . import views

urlpatterns = [
    path("", views.print_hello),
    path("books", views.books),
    path("books/top", views.top_books),
    path("books/free", views.free_books),
    path("books/top/free", views.top_free_books),
    path("books/oldschool", views.oldschool_books),
    path("authors/", views.authors),
    path("authors/top", views.top_authors),
    path("authors/ukraine", views.ukraine_authors),
    path("authors/usa", views.usa_authors),
    path("authors/top/ukraine", views.ukraine_top_authors),
    path("orders", views.orders),
    path("orders/done", views.orders_done),
    path("orders/canceled", views.orders_canceled),
]
