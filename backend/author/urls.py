from django.urls import path

from author import views
from following import views as followingViews
from notification import views as notificationViews
from like import views as likesViews

urlpatterns = [
    # path('register/', views.Register.as_view(), name="register"),
    path('', views.GetAuthorsApiView.as_view(), name="authors"),
    path('login/', views.Login.as_view(), name="login"),
    path('<str:user_id>/', views.GetAuthorApiView.as_view(), name="author"),
    path('<str:user_id>/liked', likesViews.GetLikedApiView.as_view(), name="liked"),
    path('<str:user_id>/followers', followingViews.GetFollowersApiView.as_view(), name="get follower"),
    path('<str:user_id>/followers/<str:foreign_user_id>', followingViews.EditFollowersApiView.as_view(), name="edit follower"),
    #path('<str:user_id>/inbox', notificationViews..as_view(), name = "edit follower")
]
