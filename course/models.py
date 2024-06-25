from django.db import models
from django.conf import settings # 导入settings模块


class CourseModel(models.Model):
    name = models.CharField(max_length=255, unique=True, help_text='课程名称', verbose_name='课程名称') # help_text是在admin后台管理页面显示的帮助文本
    introduction = models.TextField(help_text='课程介绍', verbose_name='课程介绍')
    teacher = models.ForeignKey(settings.AUTH_USER_MODEL,                              on_delete=models.CASCADE, help_text='授课老师', verbose_name='授课老师') # settings.AUTH_USER_MODEL, # 通过settings.AUTH_USER_MODEL来获取用户模型
    price = models.DecimalField(max_digits=6, decimal_places=2, help_text='课程价格', verbose_name='课程价格')
    create_time = models.DateTimeField(auto_now_add=True, help_text='创建时间', verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True, help_text='更新时间', verbose_name='更新时间')

    class Meta:
        verbose_name = '课程信息'
        verbose_name_plural = verbose_name # verbose_name_plural是verbose_name的复数形式
        ordering = ['price'] # 按照价格升序排列
    def __str__(self):
        return self.name # 对于Course对象，返回课程名称，相当于重写了Java的toString()方法



