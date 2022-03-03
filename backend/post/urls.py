from django.urls import path
from post import views
urlpatterns = [
    path('', views.GetPostsApiView.as_view(), name="post creation"),
    path('<str:post_id>', views.GetPostApiView.as_view(), name="post"),

]