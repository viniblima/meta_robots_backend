# Generated by Django 3.2.4 on 2022-07-07 16:42

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('robots', '0004_alter_robot_energy'),
        ('teams', '0005_alter_team_members'),
    ]

    operations = [
        migrations.CreateModel(
            name='RequestJoinTeam',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('status', models.CharField(default='requested', max_length=16, verbose_name='Status')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Data da criação')),
                ('modified_at', models.DateTimeField(null=True, verbose_name='Data da última mudança')),
                ('robot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='robots.robot')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teams.team')),
            ],
        ),
    ]