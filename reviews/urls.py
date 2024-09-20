from django.urls import path

from .views import create_review, update_review, delete_review

urlpatterns = [
    path('reviews/create/', create_review, name='create_review'),
    path('reviews/update/<int:pk>/', update_review, name='update_review'),
    path('reviews/delete/<int:pk>/', delete_review, name='delete_review'),
]