from django.urls import path, include

from apps.users import urls as user_urls

urlpatterns = [
    path('api/', include([
        path('v1/', include([
            path('users/', include(user_urls)),
        ])),
    ]))
]
