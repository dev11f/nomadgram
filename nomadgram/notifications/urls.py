from django.conf.urls import url
from . import views

app_name = "notifications"

urlpatterns = [
    url(
        regex=r'^$',
        view=views.Notifications.as_view(),  # class를 view로 보자
        name='notifications'
    ),
]
