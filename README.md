# 关于DRF的认证与鉴权
## 1.认证
    'DEFAULT_AUTHENTICATION_CLASSES': [ # DRF默认的认证类
        'rest_framework.authentication.BasicAuthentication', # 用户名密码认证（基于Base64在请求头传递，可以轻易解密）
        'rest_framework.authentication.SessionAuthentication', # session认证, 需要开启CSRF token， 否则会报403错误
        'rest_framework.authentication.TokenAuthentication', # token认证
    ],
这里重点介绍TokenAuthentication，因为它是最常用的认证方式。
### 1.1 如何生成Token
    1.1.1 通过DRF自带的命令行工具生成
    python manage.py drf_create_token [username] # 仅支持DRF自带的User模型，测试用
    1.1.2 通过代码生成
    from rest_framework.authtoken.models import Token
    token = Token.objects.create(user=user)
    1.1.3 通过信号量生成
    from django.dispatch import receiver
    from rest_framework.authtoken.models import Token
    from django.db.models.signals import post_save
    from django.contrib.auth.models import User
    @receiver(post_save, sender=User)
    def create_user_token(sender, instance=None, created=False, **kwargs):
        if created:
            Token.objects.create(user=instance)