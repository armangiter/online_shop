from django.urls import path
from . import views

app_name = 'customer'
urlpatterns = [
    path('register/', views.UserRegisterView.as_view(), name='user_register'),
    path('verify/', views.UserRegisterVerifyCodeView.as_view(), name='verify_code'),
    path('login/', views.UserLoginView.as_view(), name='user_login'),
    path('login_verify/', views.UserLoginVerifyView.as_view(), name='login_verify'),
    path('logout/', views.UserLogoutView.as_view(), name='user_logout')
]
