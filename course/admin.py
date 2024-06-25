from django.contrib import admin

from .models import CourseModel
#注册Course模型，这样在admin后台管理页面就可以看到Course模型，并对其进行增删改查操作

@admin.register(CourseModel) # 使用装饰器注册Course模型
class CourseAdmin(admin.ModelAdmin):
    list_display = ['name', 'introduction', 'teacher', 'price'] # 显示的字段
    search_fields = list_display # 搜索的字段
    list_filter = list_display # 过滤的字段
    list_per_page = 2 # 每页显示的数量
    ordering = ['price'] # 按照价格升序排列
    fieldsets = [
        ('基本信息', {'fields': ['name', 'introduction', 'teacher', 'price']}),

    ] # 在admin后台管理页面显示的字段分组
