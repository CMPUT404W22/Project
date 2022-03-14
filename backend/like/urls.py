from django.urls import path
from like import views

urlpatterns = [
    path('', views.GetLikeApiView.as_view(), name="send like"),
]
