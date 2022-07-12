from django.urls import path, include

from apps.users import urls as user_urls
from apps.robots import urls as robot_urls
from apps.trains import urls as train_urls
urlpatterns = [
    path('api/', include([
        path('v1/', include([
            path('users/', include(user_urls)),
            path('robots/', include(robot_urls)),
            path('trains/', include(train_urls)),
        ])),
    ]))
]
