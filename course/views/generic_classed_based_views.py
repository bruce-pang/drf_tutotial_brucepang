from rest_framework import generics
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from course.models import CourseModel
from course.serializers import CourseSerializer
from course.permission import IsOwnerOrReadOnly
"""
三、通用类视图 Generic Class Based Views
"""
class GenericCourseList(generics.ListCreateAPIView): # 自带了get和post方法
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication] # 指定认证类
    """
    课程列表
    """
    queryset = CourseModel.objects.all() # 属性名固定，不能修改
    serializer_class = CourseSerializer # 属性名固定，不能修改

    def perform_create(self, serializer): # 需要重写perform_create方法，因为teacher字段不由前端传入，需要后端处理
        serializer.save(teacher=self.request.user)

class GenericCourseDetail(generics.RetrieveUpdateDestroyAPIView): # 自带了get、put、delete方法
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly] # 权限类
    """
    课程详情
    """
    queryset = CourseModel.objects.all()
    serializer_class = CourseSerializer