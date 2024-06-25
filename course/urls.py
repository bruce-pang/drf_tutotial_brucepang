from django.urls import path, include
from rest_framework.routers import DefaultRouter

from course.views import fbv_cbv_views, function_based_views, class_based_views, generic_classed_based_views

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
]