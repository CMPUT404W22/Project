from django.urls import path

from following import views

url_base = 'service/authors'

urlpatterns = [
    #path('authors/<str:author_username>/following', views.Followers.as_view(), name='get-followers'),
    path('author/<str:author_username>', views.FollowersApiView.as_view(), name='get-followers'),
    path('author/<str:author_username>/<str:foreign_author_id>', views.FollowersApiView.as_view(), name = "delete-follower")
    #path('{url_base}/{AUTHOR_ID}/following/', views.index, name='main-view'),
    #path('{url_base}/{AUTHOR_ID}/addFollower/', views.index, name='main-view'),
    #path('{url_base}/{AUTHOR_ID}/removeFollower/', views.index, name='main-view'),
    #path('{url_base}/{AUTHOR_ID}/addFollowing/', views.index, name='main-view'),
    #path('{url_base}/{AUTHOR_ID}/removeFollowing/', views.index, name='main-view'),
]
