from django.conf.urls import url
from . import views

# 여기서 url을 설정해주면 setting - urls.py에 추가해줘야 함.
app_name = "images"

urlpatterns = [
    url(
        regex=r'^$',
        view=views.Images.as_view(),  # class를 view로 보자
        name='feed'
    ),
    url(
        regex=r'^(?P<image_id>[0-9]+)/$',  # $는 뒤에 더 안 붙는다는 뜻
        view=views.ImageDetail.as_view(),
        name='image_detail'
    ),
    url(
        regex=r'^(?P<image_id>[0-9]+)/likes/$',  # $는 뒤에 더 안 붙는다는 뜻
        view=views.LikeImage.as_view(),
        name='like_image'
    ),
    url(
        regex=r'^(?P<image_id>[0-9]+)/unlikes/$',
        view=views.UnLikeImage.as_view(),
        name='unlike_image'
    ),
    url(
        regex=r'^(?P<image_id>[0-9]+)/comments/$',
        view=views.CommentOnImage.as_view(),
        name='comment_image'
    ),
    url(
        regex=r'^(?P<image_id>[0-9]+)/comments/(?P<comment_id>[0-9]+)/$',
        view=views.ModerateComments.as_view(),
        name='moderate_comments'
    ),
    url(
        regex=r'comments/(?P<comment_id>[0-9]+)/$',
        view=views.Comment.as_view(),
        name='comment'
    ),
    url(
        regex=r'^search/$',
        view=views.Search.as_view(),
        name='search'
    )

]


# /images/3/like/
# 좋아요 만드는 법
# 0. create the url and the view
# 1. take the id from the url
# 2. we want to find an image with this id
# 3. we want to create a like for that image
