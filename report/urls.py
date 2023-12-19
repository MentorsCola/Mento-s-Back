from django.urls import path
from .views import ReportCreateView

urlpatterns = [
    path('reports/<int:board_id>/', ReportCreateView.as_view(), name='report-create'),
]