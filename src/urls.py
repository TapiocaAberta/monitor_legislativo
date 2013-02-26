# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from core.views import homepage
from politicos.views import homepage_politico, perfil_politico
from projetos.views import homepage_projetos
import settings

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', homepage),
    # Examples:
    # url(r'^$', 'src.views.home', name='home'),
    # url(r'^src/', include('src.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('politicos.views',
    (r'^politicos/$', homepage_politico),
    (r'^politicos/(?P<politico_id>\d+)/$', perfil_politico),
)

urlpatterns += patterns('projetos.views',
    (r'^projetos/', homepage_projetos),
    (r'^projetos/detalhe/', homepage_projetos),

)

#urlpatterns += patterns('ocorrencias.views',
#    (r'^ocorrencias/', homepage_ocorrencia),
#)

urlpatterns += staticfiles_urlpatterns()

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    )