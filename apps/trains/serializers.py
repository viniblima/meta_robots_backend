from rest_framework import serializers

from apps.robots.models import Robot

from .models import Train

from django.conf import settings


class TrainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Train
        fields = '__all__'

    def create(self, validated_data):

        Train.objects.create(
            robot=validated_data['robot'],
            trained_attribute=validated_data['trained_attribute']
        )
        train = settings.TRAIN_OBJ[validated_data['trained_attribute']]

        robot = Robot.objects.get(
            id=validated_data['robot'].id)

        new_value = getattr(robot, validated_data['trained_attribute']) + train
        new_energy = getattr(robot, 'energy') - 1.0

        setattr(robot, validated_data['trained_attribute'], new_value)
        setattr(robot, 'energy', new_energy)

        robot.save()

        return validated_data
