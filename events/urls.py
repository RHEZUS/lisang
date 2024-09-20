from django.urls import path
from .views import category_list, category_create, category_update, category_delete, event_list, event_create, event_update, event_delete, event_detail, get_my_events

urlpatterns = [
    # Categories
    path('categories/', category_list, name='category_list'),
    path('categories/create/', category_create, name='category_create'),
    path('categories/update/<int:pk>/', category_update, name='category_update'),
    path('categories/delete/<int:pk>/', category_delete, name='category_delete'),

    # Events
    path('events/', event_list, name='event_list'),
    path('events/create/', event_create, name='event_create'),
    path('events/update/<int:pk>/', event_update, name='event_update'),
    path('events/delete/<int:pk>/', event_delete, name='event_delete'),
    path('events/detail/<int:pk>/', event_detail, name='event_detail'),
    path('events/my-events/', get_my_events, name='my_events'),
]