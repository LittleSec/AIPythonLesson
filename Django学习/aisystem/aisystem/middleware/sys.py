from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponseRedirect

# 写完记得加入setting.py
class LoginMiddleWare(MiddlewareMixin):
    def process_request(self, request):
        if request.path not in ['/user/login', '/user/code']:
            if 'username' not in request.session or not request.session["username"]:
                return HttpResponseRedirect("/user/login")