from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from course.models import CourseModel
from course.serializers import CourseSerializer
"""
一、函数式视图 Function Based Views
"""

@api_view(['GET', 'POST'])
def course_list(request):
    """
    获取所有课程信息或新增一个课程
    :param request: 请求对象
    :return: JsonResponse
    """
    if request.method == 'GET':
        query_set = CourseSerializer(instance=CourseModel.objects.all(), many=True, context={'request': request})
        return Response(data=query_set.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        s = CourseSerializer(data=request.data, partial=True) # partial=True表示允许部分字段更新(不是所有字段都必须传递)，默认为False(所有字段都必须传递)
        if s.is_valid(): # 验证数据是否合法
            s.save(teacher=request.user) # 由于序列化器中的teacher字段是只读字段，所以这里需要手动添加teacher字段，request.user表示当前登录的用户，在本业务中谁创建的课程就是谁就是老师
            return Response(data=s.data, status=status.HTTP_201_CREATED)
        return Response(data=s.errors, status=status.HTTP_400_BAD_REQUEST)