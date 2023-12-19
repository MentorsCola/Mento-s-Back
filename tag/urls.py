from django.urls import path
from .views import TagCreateView

urlpatterns = [
    # 다른 URL 패턴들...
    path('tags/<int:board_id>/', TagCreateView.as_view(), name='tag-create'),
]