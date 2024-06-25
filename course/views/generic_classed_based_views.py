from rest_framework import generics

from course.models import CourseModel
from course.serializers import CourseSerializer

"""
三、通用类视图 Generic Class Based Views
"""
class GenericCourseList(generics.ListCreateAPIView): # 自带了get和post方法
    """
    课程列表
    """
    queryset = CourseModel.objects.all() # 属性名固定，不能修改
    serializer_class = CourseSerializer # 属性名固定，不能修改

    def perform_create(self, serializer): # 需要重写perform_create方法，因为teacher字段不由前端传入，需要后端处理
        serializer.save(teacher=self.request.user)

class GenericCourseDetail(generics.RetrieveUpdateDestroyAPIView): # 自带了get、put、delete方法
    """
    课程详情
    """
    queryset = CourseModel.objects.all()
    serializer_class = CourseSerializer