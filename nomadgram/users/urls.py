from django.conf.urls import url

from . import views

app_name = "users"
urlpatterns = [
    url(
        regex=r'^explore/$',
        view=views.ExploreUsers.as_view(),
        name='explore_users'
    ),
    url(
        regex=r'^(?P<user_id>[0-9]+)/follow/$',
        view=views.FollowUser.as_view(),
        name='follow_user'
    ),
    url(
        regex=r'^(?P<user_id>[0-9]+)/unfollow/$',
        view=views.UnFollowUser.as_view(),
        name='unfollow_user'
    ),
    url(
        regex=r'^(?P<username>\w+)/followers/$',
        view=views.UserFollowers.as_view(),
        name='user_followers'
    ),
    url(
        regex=r'^(?P<username>\w+)/following/$',
        view=views.UserFollowing.as_view(),
        name='user_following'
    ),
    url(
        regex=r'^search/$',
        view=views.Search.as_view(),
        name='search'
    ),
    url(
        regex=r'^push/$',
        view=views.RegisterPush.as_view(),
        name='push'
    ),
    url(
        regex=r'^(?P<username>\w+)/$',
        view=views.UserProfile.as_view(),
        name='user_profile'
    ),
    url(
        regex=r'^(?P<username>\w+)/password/$',
        view=views.ChangePassword.as_view(),
        name='change'
    ),
    url(
        regex=r'^login/facebook/$',
        view=views.FacebookLogin.as_view(),
        name='fb_login'
    )





    # url(regex=r"^$", view=views.UserListView.as_view(), name="list"),
    # url(regex=r"^~redirect/$", view=views.UserRedirectView.as_view(), name="redirect"),
    # url(regex=r"^~update/$", view=views.UserUpdateView.as_view(), name="update"),
    # url(
    #     regex=r"^(?P<username>[\w.@+-]+)/$",
    #     view=views.UserDetailView.as_view(),
    #     name="detail",
    # ),
]
