from django.contrib import admin
from . import models

# Register your models here.

# 모델들이 어드민 안에서 어떻게 보이게 하는가.


@admin.register(models.Image)  # 이 데코레이터가 무엇을 의미하는가?????? 아래 클래스를 등록하는 것
class ImageAdmin(admin.ModelAdmin):
    # pass   # pass는 텅 빈 클래스를 의미

    list_display_links = (
        'location',   # location 눌러서 편집 가능
    )

    search_fields = (
        'location',    # search bar 추가
        'caption',
    )

    list_filter = (
        'location',
        'creator',
    )

    list_display = (
        'file',
        'location',
        'caption',
        'creator',
        'created_at',
        'updated_at',
    )


@admin.register(models.Like)
class LikeAdmin(admin.ModelAdmin):

    list_display = (
        'creator',
        'image',
    )


@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):

    list_display = (
        'message',
        'creator',
        'image',
        'created_at',
        'updated_at',
    )
