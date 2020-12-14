from django.urls import path
from .views import GiaTaskDetailView, TaskTypeDetailView, RedirectToEGEMath, RedirectToOGEMath


urlpatterns = [
    path('show/<slug:slug>/', GiaTaskDetailView.as_view(), name='task-detail'),
    path('egem/', RedirectToEGEMath.as_view(), name='ege-math'),
    path('ogem/', RedirectToOGEMath.as_view(), name='oge-math'),
    path('<slug:slug>/', TaskTypeDetailView.as_view(), name='tasktype-detail'),
]
