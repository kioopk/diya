from django.urls import path
from .views import register
from django.contrib.auth import views as auth_views

app_name = "students"
urlpatterns = [
    path('register/', register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name="students/login.html"), name="login"),
    path('logout/', auth_views.LogoutView.as_view(next_page='students:login'), name="logout"),
]