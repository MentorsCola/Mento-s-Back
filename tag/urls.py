from django.urls import path
from .views import TagCreateView

urlpatterns = [
    path('tags/<int:board_id>/', TagCreateView.as_view(), name='tag-create'),
]