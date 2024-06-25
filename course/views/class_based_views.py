from django.http import JsonResponse
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from course.models import CourseModel
from course.serializers import CourseSerializer
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
"""
二、类视图 Class Based Views
"""
class CourseList(APIView):
    authentication_classes = [TokenAuthentication] # 认证类
    permission_classes = [IsAuthenticated,] # 权限类
    def get(self, request):
        """

        :param request:
        :return:
        """
        query_set = CourseModel.objects.all()
        s = CourseSerializer(instance=query_set, many=True, context={'request': request}) # 这里的instance是一个QuerySet对象，many=True表示序列化多个对象
        return Response(data=s.data, status=status.HTTP_200_OK)

    def post(self, request):
        """

        :param request:
        :return:
        """
        s = CourseSerializer(data=request.data, partial=True) # data =xx是前端传递过来的数据(经过测试，post请求保存时只能传递字典类型，也就是只能传递一个对象，目前不能批量插入)，return前要先调用is_valid()方法验证数据是否合法
        if s.is_valid(): # 数据合法
            s.save(teacher=self.request.user)
            print(type(request.data), type(s.data))
            return Response(data=s.data, status=status.HTTP_201_CREATED)
        return Response(data=s.errors, status=status.HTTP_400_BAD_REQUEST)

class CourseDetail(APIView):

    # 由于下面的方法都时处理的同一个实例，所以可以定义一个get_object方法来获取实例
    @staticmethod # 静态方法
    def get_object(pk):
        try:
            return CourseModel.objects.get(pk=pk)
        except CourseModel.DoesNotExist:
            return
    def get(self, request, pk):
        """
        获取课程详情信息
        :param request:  请求对象
        :param pk: 课程id
        :return: 课程详情
        """
        obj = self.get_object(pk=pk)
        if not obj:
            return Response(data={'msg': '课程不存在'}, status=status.HTTP_404_NOT_FOUND)
        s = CourseSerializer(instance=obj, context={'request': request}) # 进行序列化返回前端
        return Response(data=s.data, status=status.HTTP_200_OK)
    def put(self, request, pk):
        """
        更新课程信息
        :param request:
        :param pk:
        :return:
        """
        obj = self.get_object(pk=pk)
        if not obj:
            return Response(data={'msg': '课程不存在'}, status=status.HTTP_404_NOT_FOUND)
        # 序列化以进行更新实例
        s = CourseSerializer(instance=obj, data=request.data, partial=True)
        if s.is_valid():
            s.save() # 保存更新
            return Response(data=s.data, status=status.HTTP_200_OK)
        return Response(data=s.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk):
        """
        删除课程信息
        :param request:
        :param pk:
        :return:
        """
        obj = self.get_object(pk=pk)
        if not obj:
            return Response(data={'msg': '课程不存在'}, status=status.HTTP_404_NOT_FOUND)
        obj.delete()
        return Response(data={'msg': '课程删除成功'}, status=status.HTTP_204_NO_CONTENT)

