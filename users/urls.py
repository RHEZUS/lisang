from django.urls import path
from .views import register_user, login_user, auth_check
from .views import get_users, create_user, update_user, delete_user, activate_user, deactivate_user

urlpatterns = [
    # Authentication
    path('register/', register_user, name='register'),
    path('login/', login_user, name='login'),
    path('auth-check/', auth_check, name='auth_check'),

    path('users/', get_users, name='user_list'),
    path('users/create/', create_user, name='create_user'),
    path('users/update/<int:pk>/', update_user, name='update_user'),
    path('users/delete/<int:pk>/', delete_user, name='delete_user'),
    path('users/activate/<int:pk>/', activate_user, name='activate_user'),
    path('users/deactivate/<int:pk>/', deactivate_user, name='deactivate_user'),
    
]
