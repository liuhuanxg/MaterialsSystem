from django.contrib.admin.sites import AdminSite
from django.http import HttpResponseRedirect
from django.template.response import TemplateResponse
from django.views.decorators.cache import never_cache


class MySite(AdminSite):
    @never_cache
    def index(self, request, extra_context=None):
        """
        Display the main admin index page, which lists all of the installed
        apps that have been registered in this site.
        """
        app_list = self.get_app_list(request)

        context = {
            **self.each_context(request),
            'title': self.index_title,
            'app_list': app_list,
            **(extra_context or {}),
        }
        print("context:{}".format(context))
        request.current_app = self.name

        return TemplateResponse(request, self.index_template or 'admin/index.html', context)


def my_index(request):
    extra_context = {
        "test": "msg"
    }
    return HttpResponseRedirect("/", {"extra_context": extra_context})
