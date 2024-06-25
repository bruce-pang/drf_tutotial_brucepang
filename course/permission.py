from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission): # 只有拥有者才能编辑，其他人只能读
    """自定义权限：只有对象的所有者才有写权限，其他人只有读权限"""
    def has_object_permission(self, request, view, obj): # 最简单的自定义权限的方法，就是重写has_object_permission方法
        """
        所有的request请求都有读权限，因此一律允许GET/HEAD/OPTIONS请求
        :param request:
        :param view:
        :param obj:
        :return: bool
        """
        # if request.method in ("GET", "HEAD", "OPTIONS"):
        # 以上写法等价于下面的写法
        if request.method in permissions.SAFE_METHODS:
            return True
        # 如果是其他请求，只有对象的所有者才有写权限
        return obj.teacher == request.user