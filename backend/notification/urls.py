from django.urls import path
from notification import views as notificationViews

urlpatterns = [
    # NOTE: "notifcation_id" is NOT the id of the notification object. It is the id of the post/follow/like/comment
    path('inbox/<str:user_id>/<str:notification_type>/<str:notifcation_id>', notificationViews.NotificationsApiView.as_view(), name="post notifaction to inbox")
]
