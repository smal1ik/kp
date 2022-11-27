from rest_framework import permissions


class IsNewsEditor (permissions.BasePermission):
    def has_permission (self, request, view):
        return bool(request.user.groups.all().filter(name = "news_editor") or request.user.is_staff)

class IsAndroidApp (permissions.BasePermission):
    def has_permission (self, request, view):
        if("lAndroidApp" in str(request)):
            return True
        return False