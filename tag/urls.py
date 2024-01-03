from django.urls import path
from .views import TagCreateView, TagSearchView

urlpatterns = [
    path('tags/<int:board_id>/', TagCreateView.as_view(), name='tag-create'),
    path('tags/get/', TagSearchView.as_view(), name='tag-search') #query=
]