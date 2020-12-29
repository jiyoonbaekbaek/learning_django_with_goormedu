from django.contrib import admin
from .models import Post
# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display=(
        'id',
        'title',
        'view_count',
        'created_at',
        'updated_at'
    ) #list_display : 원하는 컬럼들을 보여줌 "이러한 정보들을 테이블 형태로 보고 싶어"

    search_fields=(
        'title',
    ) #search_fields : "title 로 검색을 가능하게 할꺼야 "