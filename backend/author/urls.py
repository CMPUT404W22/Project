from django.urls import path

from author import views

urlpatterns = [
    # path('register/', views.Register.as_view(), name="register"),
    path('', views.GetAuthorsApiView.as_view(), name="authors"),
    path('<str:user_id>/', views.GetAuthorApiView.as_view(), name="author"),
    path('<str:user_id>/followers', views.GetAuthorFollowersApiView.as_view(), name="author follower"),
    path('<str:user_id>/followers/<str:foreign_user_id>', views.GetAuthorFollowersApiView.as_view(), name = "delete follower")
]
