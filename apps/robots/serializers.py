from rest_framework import serializers
from .models import Robot
from django.contrib.auth import get_user_model


class RobotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Robot
        fields = '__all__'

    def create(self, validated_data,):

        robot = Robot.objects.create(
            user=validated_data['user'],
            color_energy=validated_data['color_energy'],
            class_robot=validated_data['class_robot'],
            color_robot=validated_data['color_robot'],
            strength=validated_data['strength'],
            speed=validated_data['speed'],
            skill=validated_data['skill'],
            defense=validated_data['defense'],
        )

        user = get_user_model().objects.get(id=validated_data['user'].id)
        user.robots.add(robot.id)

        return validated_data
