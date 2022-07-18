from django.urls import path, include

from apps.users import urls as user_urls
from apps.robots import urls as robot_urls
from apps.trains import urls as train_urls
from apps.teams import urls as team_urls
from apps.match import urls as match_urls
from apps.request_join_team import urls as join_team_urls

urlpatterns = [
    path('api/', include([
        path('v1/', include([
            path('users/', include(user_urls)),
            path('robots/', include(robot_urls)),
            path('trains/', include(train_urls)),
            path('teams/', include(team_urls)),
            path('match/', include(match_urls)),
            path('request_join_team/', include(join_team_urls))
        ])),
    ]))
]
