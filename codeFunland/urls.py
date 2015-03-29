from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
# from django.conf.urls.static import static

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'codeFunland.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^yoyo/', include(admin.site.urls)),
    url(r'^$', include('start.urls', namespace="start")),
    url(r'^users/', include('users.urls', namespace="users")),
    url(r'^courses/', include('courses.urls', namespace="courses")),
    url(r'^labs/', include('labs.urls', namespace="labs")),
)

# urlpatterns += patterns('users.views',
    # url(r'^test1/$', 'test1'),
    # url(r'^test2/(?P<var>\d.*)/$', 'test2', {'test_var': ''}),
# )

if settings.DEBUG:
    urlpatterns += patterns(
        'django.views.static',
        url(r'^media/(?P<path>.*)$',
        'serve',
        {'document_root': settings.MEDIA_ROOT}),
    )

handler404 = "start.views.page_not_found"
