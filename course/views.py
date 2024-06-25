import json

from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator # 导入method_decorator装饰器
from django.views import View

course_dict = {
    'name': '课程名称',
    'introduction': '课程简介',
    'price': 9999.99,
}
# 基于FBV的视图 编写API接口
@csrf_exempt # 取消Django的CSRF验证
def course_list(request):
    if request.method == 'GET':
        # return HttpResponse(json.dumps(course_dict), content_type='application/json')
        # 上面一行代码等价于下面一行代码
        return JsonResponse(course_dict)
    if request.method == 'POST':
        course = json.loads(request.body.decode('utf-8')) # 使用json.loads()方法将json字符串转换为Python字典时，指定编码格式为utf-8
        # return HttpResponse(json.dumps(course), content_type='application/json')
        # 上面一行代码等价于下面一行代码
        return JsonResponse(course, safe=False) # safe=False表示允许返回非字典类型的数据(解析出来是字符串的话，就把safe设置为False)

# 基于CBV的视图 编写API接口
@method_decorator(csrf_exempt, name='dispatch') # 取消Django的CSRF验证, 由于请求是打到dispatch方法上的，由dispatch去调用post，所以这里写的是dispatch
class CourseList(View):
    def get(self, request):
        return JsonResponse(course_dict)

    # @csrf_exempt
    def post(self, request):
        course = json.loads(request.body.decode('utf-8'))
        return JsonResponse(course, safe=False) # safe=False表示允许返回非字典类型的数据(解析出来是字符串的话，就把safe设置为False)

