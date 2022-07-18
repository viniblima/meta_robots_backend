from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import DjangoJobStore, register_events
from django.utils import timezone
from django_apscheduler.models import DjangoJobExecution
import sys
from apps.teams.models import Team
from apps.match.models import Match
from datetime import datetime

# This is the function you want to schedule - add as many as you want and then register them in the start() function below


def deactivate_expired_accounts():
    print('Im working')


def create_match():
    """
    Cria partida, utilizando rotina de repeticao
    """

    for team in Team.objects.all():
        have_match = Match.objects.filter(
            first_team=team) | Match.objects.filter(second_team=team)

        if have_match.count():
            print('Team >>>>')
            print(have_match.count())
            print(have_match)

        else:
            opponents = Team.objects.exclude(id=team.id)

            for opponent in opponents:
                opponent_have_match = Match.objects.filter(
                    first_team=opponent) | Match.objects.filter(second_team=opponent)

                if opponent_have_match.count():
                    print('Oponente >>>>')
                    print(opponent_have_match.count())
                    print(opponent_have_match)

                else:
                    Match.objects.create(
                        first_team=team,
                        second_team=opponent,
                        schedule=datetime.now()
                    )
                    print(Match.objects.filter(first_team=team))
                    break

    # Match.objects.create(
    #     first_team=Team.objects.all().last(),
    #     second_team=Team.objects.all().first(),
    #     schedule=datetime.now()
    # )


def start():
    scheduler = BackgroundScheduler()
    # scheduler.add_jobstore(DjangoJobStore(), "default")
    # # # run this job every 24 hours
    scheduler.add_job(create_match, 'interval',
                      minutes=1, name='clean_accounts', jobstore='default')
    # # register_events(scheduler)
    scheduler.start()
    # print("Scheduler started...", file=sys.stdout)
