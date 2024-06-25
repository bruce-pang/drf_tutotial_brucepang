from rest_framework import serializers
from django.contrib.auth.models import User
from .models import CourseModel


class CourseForm(serializers.ModelSerializer):
    class Meta:
        model = CourseModel
        fields = ['name', 'introduction', 'teacher', 'price',]

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields = ['username', 'email', 'password']
        fields = '__all__'

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user




class CourseSerializer(serializers.ModelSerializer):
    # 由于 teacher 是一个外键，在显示时，我们希望显示老师的用户名，而不是老师的 id
    teacher = serializers.ReadOnlyField(source='teacher.username') # source='teacher.username'表示teacher字段的值是teacher对象的username属性

    class Meta:
        model = CourseModel # 写法和上面的CourseModel一样
        # exclude = ('id',) # 注意元组中只有一个元素时不能写成('id')这种形式，要写成('id',)这种形式
        # fields = ('id', 'name', 'introduction', 'teacher', 'price', 'create_time', 'update_time')
        fields = '__all__'