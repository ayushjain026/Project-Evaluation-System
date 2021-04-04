from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("email_verify/", views.email_verify),
    path("dashboard/", views.dashboard, name="dashboard"),
    path('submission/', views.submission, name="submission"),
    path("project/", views.project, name="project"),
    path("work_history/", views.work_history, name="work_history"),
    path("profile/", views.profile, name="profile"),
    path("notice/", views.notices, name='notice'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)