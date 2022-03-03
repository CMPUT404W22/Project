from django.urls import path

from author import views
from following import views as followingViews

urlpatterns = [
    # path('register/', views.Register.as_view(), name="register"),
    path('', views.GetAuthorsApiView.as_view(), name="authors"),
    path('<str:user_id>/', views.GetAuthorApiView.as_view(), name="author"),
    path('<str:user_id>/followers', followingViews.GetFollowersApiView.as_view(), name="get follower"),
    path('<str:user_id>/followers/<str:foreign_user_id>', followingViews.EditFollowersApiView.as_view(), name = "edit follower")
]
