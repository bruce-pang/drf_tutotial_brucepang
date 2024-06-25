from rest_framework import viewsets
from course.models import CourseModel
from course.serializers import CourseSerializer
"""
generic_classed_based_views.py中的代码虽然使用了CBV，但是依旧需要把方法分开写，能不能只写一个类就行呢？
四、DRF的视图集viewsets,
"""

class CourseViewSet(viewsets.ModelViewSet): # 继承ModelViewSet，自带了get、post、put、delete方法
    """
    课程列表和详情
    """
    queryset = CourseModel.objects.all() # 属性名固定，不能修改
    serializer_class = CourseSerializer # 属性名固定，不能修改

    def perform_create(self, serializer): # 需要重写perform_create方法，因为teacher字段不由前端传入，需要后端处理
        serializer.save(teacher=self.request.user)

