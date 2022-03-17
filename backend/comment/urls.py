from django.urls import path
from comment import views
from like import views as likesViews

urlpatterns = [
    path('', views.GetCommentsApiView.as_view(), name="comment"),
    path('<str:comment_id>/likes', likesViews.GetLikeCommentApiView.as_view(), name="liked comments"),

]
