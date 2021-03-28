from django.conf.urls import url
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", views.index),
    path("hod_register/", views.hod_register),
    path("index/", views.index, name='index'),
    path("test_save/", views.test_save),
    path("test/", views.test),
    path('hod_login/',views.hod_login, name='login'),
    path('hod_dashboard/', views.hod_dashboard),
    path("logout/", views.logout, name="logout"),
    path("add_faculty/", views.add_faculty),
    path("faculty_desc/", views.faculty_desc),
    path("edit_faculty/",views.edit_faculty),
    path("profile/", views.profile),
    path("email_verify/", views.email_verify),
    # path('login/', auth_views.LoginView.as_view(), name='login'),
    path('password_reset/done', auth_views.PasswordResetCompleteView.as_view(template_name='password/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset/',auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='password/password_reset_complete.html'), name='password_reset_complete'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)