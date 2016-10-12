from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Examples:
    # url(r'^$', 'buscoayuda4101.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^', include('polls.urls', namespace="principal")),
    url(r'^admin/', include(admin.site.urls)),
    url(
        r'^login/$',
        auth_views.login,
        {
            'template_name': 'login.html'
        },
        name='login',
    ),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
