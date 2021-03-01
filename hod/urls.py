from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.index),
    path("hod_register/", views.hod_register),
    path("index/", views.index),
    path("test_save/", views.test_save),
    path("test/", views.test),
    path('hod_login/',views.hod_login),
    path('hod_dashboard/', views.hod_dashboard),
    # path('success', success, name = 'success'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)