from django.urls import path
from django.contrib.auth.views import LogoutView

from user.views import CustomLoginView, RegisterPage


urlpatterns = [
    path('entrar/', CustomLoginView.as_view(), name='login'),
    path('sair/', LogoutView.as_view(next_page='login'), name='logout'),
    path('registrar/', RegisterPage.as_view(), name='register')
]
