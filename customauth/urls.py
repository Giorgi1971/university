from django.urls import path
from .views import index, SignUpView, profile
from django.contrib.auth import views as auth_views


app_name = 'customauth'

urlpatterns = [
    path('', index, name='index'),
    path('register/', SignUpView.as_view(), name='register_view'),
    path('login/', auth_views.LoginView.as_view(redirect_authenticated_user=False), name='login_view'),
    path('logout/', auth_views.LogoutView.as_view(next_page='customauth:index'), name='logout_view'),
    path('profile/', profile, name='profile')
]
