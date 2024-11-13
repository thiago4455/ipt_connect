import importlib

from django.conf import settings
from django.urls import include, re_path
from django.contrib import admin

tournament_overview = importlib.import_module(
    settings.INSTALLED_TOURNAMENTS[0] + '.views'
).tournament_overview

urlpatterns = [
    # Examples:
    # url(r'^$', 'ipt_connect.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    re_path(r'^grappelli/', include('grappelli.urls')),  # grappelli URLS
    # url(r'^$', home, name='home'), #TemplateView.as_view(template_name='index.html')),#'ipt_connect.views.home'),
    re_path(r'^$', tournament_overview),
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^iprestrict/', include('iprestrict.urls', namespace='iprestrict')),
]

for tournament in settings.INSTALLED_TOURNAMENTS:
    urlpatterns.append(
        re_path(
            r'^' + tournament + '/', include(tournament + '.urls', namespace=tournament)
        ),
    )

admin.site.site_header = 'IPT administration'
