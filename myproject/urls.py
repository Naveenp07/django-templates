# myproject/urls.py

from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.views import defaults as default_views
from django.views.generic import TemplateView

urlpatterns = [
    path(settings.ADMIN_URL, admin.site.urls),
    path('', TemplateView.as_view(template_name='index.html'), name='home'),
    path('users/', include('users.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [
        path('400/', default_views.bad_request, kwargs={'exception': Exception("Bad Request!")}),
        path('403/', default_views.permission_denied, kwargs={'exception': Exception("Permission Denied")}),
        path('404/', default_views.page_not_found, kwargs={'exception': Exception("Page Not Found")}),
        path('500/', default_views.server_error),
        path('__debug__/', include(debug_toolbar.urls)),
    ]

