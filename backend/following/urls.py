from django.urls import path

url_base = 'service/authors'

urlpatterns = [
    path('{url_base}/{AUTHOR_ID}/followers/', views.index, name='main-view'),
    path('{url_base}/{AUTHOR_ID}/following/', views.index, name='main-view'),
    path('{url_base}/{AUTHOR_ID}/addFollower/', views.index, name='main-view'),
    path('{url_base}/{AUTHOR_ID}/removeFollower/', views.index, name='main-view'),
    path('{url_base}/{AUTHOR_ID}/addFollowing/', views.index, name='main-view'),
    path('{url_base}/{AUTHOR_ID}/removeFollowing/', views.index, name='main-view'),
]
