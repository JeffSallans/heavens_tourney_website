from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'heavens_tourney.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

	url(r'^$', 'basic_site.views.index', name='home'),
	url(r'^home$', 'basic_site.views.index', name='home'),
	url(r'^demo$', 'basic_site.views.demo', name='demo'),
	url(r'^monster_builds$', 'basic_site.views.info', name='info'),
	url(r'^feedback$', 'basic_site.views.contact', name='contact'),
    url(r'^admin/', include(admin.site.urls)),
)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
