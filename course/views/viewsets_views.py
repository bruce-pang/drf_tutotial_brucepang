from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from course.models import CourseModel
from course.serializers import CourseSerializer
from rest_framework.authtoken.models import Token # DRF的token认证
from django.db.models.signals import post_save # 使用信号机制，当用户创建成功后，此信号会被触发
from django.dispatch import receiver # 接收信号的装饰器
from django.contrib.auth.models import User
from django.conf import settings
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
"""
generic_classed_based_views.py中的代码虽然使用了CBV，但是依旧需要把方法分开写，能不能只写一个类就行呢？
四、DRF的视图集viewsets,
"""
@receiver(post_save, sender=settings.AUTH_USER_MODEL) # 使用信号机制，当用户创建成功后，此信号会被触发, sender指定哪个模型的信号,默认是Django的User模型,支持自定义模型
def generate_token(sender, instance=None, created=False, **kwargs): # 信号的回调函数，sender是信号的发送者，instance是发送者的实例，created是是否是新创建的，kwargs是其他参数
    """
    创建用户时，自动创建Token
    :param sender:
    :param instance:
    :param created:
    :param kwargs:
    :return:
    """
    if created:
        Token.objects.create(user=instance) # 传进来的instance就是新创建的用户对象, 创建完token后在根url中就可以使用api-token-auth获取token了

class CourseViewSet(viewsets.ModelViewSet): # 继承ModelViewSet，自带了get、post、put、delete方法
    authentication_classes = [TokenAuthentication] # 指定认证类
    permission_classes = [IsAuthenticated,] # 权限类
    """
    课程列表和详情
    """
    queryset = CourseModel.objects.all() # 属性名固定，不能修改
    serializer_class = CourseSerializer # 属性名固定，不能修改

    def list(self, request, *args, **kwargs):
        print(request.user, request.auth) # request.user是当前登录的用户对象，request.auth是当前登录的用户的token对象
        print(type(request.user), type(request.auth)) # <class 'django.contrib.auth.models.User'> <class 'rest_framework.authtoken.models.Token'>
        return super().list(request, *args, **kwargs)

    def perform_create(self, serializer): # 需要重写perform_create方法，因为teacher字段不由前端传入，需要后端处理
        serializer.save(teacher=self.request.user)

