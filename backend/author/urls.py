from django.urls import path

from author import views

urlpatterns = [
    path('register/', views.Register.as_view(), name="register"),
    path('profile/<str:username>/', views.Authors.as_view(), name="authors"),
]
