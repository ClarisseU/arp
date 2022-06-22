from django.urls import path, re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    re_path('^$',views.home, name='homepage'),
    re_path('^registration/login', views.loginPage, name = 'loginPage'),
    re_path('^trainings', views.training, name = 'training'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)