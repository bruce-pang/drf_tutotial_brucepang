from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.routers import DefaultRouter
from course.views import fbv_cbv_views, function_based_views, class_based_views, generic_classed_based_views, viewsets_views

router = DefaultRouter() # 将DefaultRouter实例化
router.register(prefix='viewsets', viewset=viewsets_views.CourseViewSet) # 注册viewsets_views.CourseViewSet视图集

urlpatterns = [
    # Function Based Views
    path('fbv/list/', function_based_views.course_list, name='fbv_course_list'),
    path('fbv/detail/<int:pk>/', function_based_views.course_detail, name='fbv_course_detail'),

    # Class Based Views
    path('cbv/list/', class_based_views.CourseList.as_view(), name='cbv_course_list'),
    path("cbv/detail/<int:pk>/", class_based_views.CourseDetail.as_view(), name='cbv_course_detail'),

    # Generic Class Based Views
    path('gcbv/list/', generic_classed_based_views.GenericCourseList.as_view(), name='gcbv_course_list'),
    path('gcbv/detail/<int:pk>/', generic_classed_based_views.GenericCourseDetail.as_view(), name='gcbv_course_detail'),

    # ViewSets
    # path('viewsets/list/', viewsets_views.CourseViewSet.as_view(
    #     {'get': 'list', 'post': 'create'} # get是http请求方式，list是minxins中ListModelMixin的list方法， 其他的同理，可以通过ModelViewSet点进去看
    # ), name='viewsets_course_list'),
    # path('viewsets/detail/<int:pk>/', viewsets_views.CourseViewSet.as_view(
    #     {'get': 'retrieve', 'put': 'update', 'delete': 'destroy', 'patch': 'partial_update'}
    # ), name='viewsets_course_detail'),

    # 以上的路由都是手动写的，非常麻烦，下面使用drf提供的router来自动生成路由
    path('', include(router.urls)) # 使用router.urls来自动生成路由
]