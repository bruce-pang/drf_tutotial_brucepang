from django.http import JsonResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from course.models import CourseModel
from course.permission import IsOwnerOrReadOnly
from course.serializers import CourseSerializer
"""
一、函数式视图 Function Based Views
"""

@api_view(['GET', 'POST']) # 限制请求方法为GET和POST
@authentication_classes([TokenAuthentication]) # 在全局已经设置了多种认证方式，如果某个视图需要特定的认证方式，可以通过此装饰器设置，@authentication_classes一定要写在@api_view的下面，有先后顺序
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
@api_view(['GET', 'PUT', 'DELETE']) # 限制请求方法为GET、PUT和DELETE
@authentication_classes([TokenAuthentication]) # 在全局已经设置了多种认证方式，如果某个视图需要特定的认证方式，可以通过此装饰器设置，@authentication_classes一定要写在@api_view的下面，有先后顺序
@permission_classes([IsAuthenticated, IsOwnerOrReadOnly,]) # 在全局已经设置了多种权限方式，如果某个视图需要特定的权限方式，可以通过此装饰器设置，@permission_classes一定要写在@api_view的下面，有先后顺序 ， 自定义的权限也可以添加在里面
def course_detail(request, pk):
    """
    获取、更新或删除一个课程
    :param request: 请求对象
    :param pk: 课程ID
    :return: JsonResponse
    """
    try:
        course = CourseModel.objects.get(pk=pk) # 如果课程不存在，会抛出异常
    except CourseModel.DoesNotExist:
        return Response(data={'error': '课程不存在'}, status=status.HTTP_404_NOT_FOUND)
    else:
        if request.method == 'GET':
            s = CourseSerializer(instance=course, context={'request': request})
            return Response(data=s.data, status=status.HTTP_200_OK)
        elif request.method == 'PUT':
            s = CourseSerializer(instance=course, data=request.data, partial=True) # instance表示数据库的记录对象，data表示前端传递过来的对象，这两个部分组合起来就是把前端的对象更新到数据库里面去，partial=True表示允许部分字段更新(不是所有字段都必须传递)，默认为False(所有字段都必须传递)
            if s.is_valid(): # 验证数据是否合法
                s.save() # 更改数据库记录时，不需要传递teacher字段，因为创建时必须传递，更新时已经是登录用户了，所以不需要再传递
                return Response(data=s.data, status=status.HTTP_200_OK)
            return Response(data=s.errors, status=status.HTTP_400_BAD_REQUEST)
        elif request.method == 'DELETE':
            course.delete()
            return Response(data={'success': '删除成功'}, status=status.HTTP_204_NO_CONTENT)

