from django.contrib import admin
from .models import Post, Comment

# Register your models here.

# 어드민 페이지에서 Post 모델과 같이 볼 수 있게 CommentInline 클래스 설정
class CommentInline(admin.TabularInline):
    model = Comment
    extra = 5
    min_num = 3
    max_num = 5
    verbose_name = '댓글'
    verbose_name_plural = '댓글'


# Post 모델 등록
@admin.register(Post)
class PostModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'image', 'content', 'created_at', 'view_count', 'writer')
    # list_editable = ['content', )
    list_filter = ('created_at', )
    search_fields = ('id', 'writer__username')
    search_help_text = '게시판 번호 및  작성자 검색이 가능합니다.'
    readonly_fields = ('created_at', )
    inlines = [CommentInline]

    # 액션 추가하기
    actions = ['make_published']

    def make_published(modeladmin, request, queryset):
        for item in queryset:
            item.content='운영 규정 위반으로 인한 게시글 삭제 처리.'
            item.save()


# Comment 모델 등록
# admin.site.register(Comment)


