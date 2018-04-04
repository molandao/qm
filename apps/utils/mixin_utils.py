from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


class LoginRequiredMixin(object):

    # 调用django的装饰器，login_required
    @method_decorator(login_required(login_url='/login/'))
    def dispatch(self,request, *args, **kwargs):
        # 必须这样写
        return super(LoginRequiredMixin, self).dispatch(request, *args, **kwargs)