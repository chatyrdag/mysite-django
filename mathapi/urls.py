from django.urls import path
from . import views


urlpatterns = [
    path('multtab/', views.multtab),
    path('lineareq/<int:level>/', views.lineareq)
]
