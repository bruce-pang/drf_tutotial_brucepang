from django.urls import path, include
from rest_framework.routers import DefaultRouter

from course.views import fbv_cbv_views, function_based_views

urlpatterns = [
    # Function Based Views
    path('fbv/list/', function_based_views.course_list, name='fbv_course_list'),
]