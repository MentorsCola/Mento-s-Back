from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('board/', include('board.urls')),
    path('user/', include('django.contrib.auth.urls')), # auth URL patterns
    path('user/', include('user.urls')), # 유저에 정의된 URL
    path('like/', include('like.urls')),
    path('comment/', include('comment.urls')),
    path('nickname/', include('nicknames.urls')),
    path('tag/', include('tag.urls')),
    path('report/', include('report.urls'))
]
