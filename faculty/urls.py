from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path("dashboard/", views.dashboard, name="dashboard"),
    path("add_student/", views.add_student, name='add_student'),
    path('logout/', views.logout, name='login'),
    path("email_verify/", views.email_verify),
    path("student_desc/", views.student_desc, name='student_desc'),
    path("delete_student/", views.delete_student),
    path('edit_student/', views.edit_student, name="edit_student"),
    path("profile/", views.profile),
    path("evaluation/", views.evaluation, name="evaluation"),
    path("create_submission/", views.create_submission, name="create_submission"),
    path("total_events/", views.total_events, name="total_events"),
    path("edit_event/", views.edit_event, name="edit_event"),
    path("delete_event/", views.delete_event, name="delete_event"),
    path("create_notice/", views.create_notice, name = "create_notice"),
    path('delete_note/', views.delete_note, name="delete_note"),
    path('view_history/', views.view_history, name="view_history"),
    path('work_history/', views.project_history, name='project_history'),
    path("evaluate_student/", views.evaluate_student, name='evaluate_student'),
    path("student_marks/", views.student_marks, name='student_marks'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)