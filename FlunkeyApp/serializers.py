from rest_framework import serializers
from .models import DeliveryFinal, Bot, Table


class DeliveryFinalSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryFinal
        fields = '__all__'
    

class BotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bot
        fields = ('avialable',)

class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = ('avialable',)
