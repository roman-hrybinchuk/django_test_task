from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from shop_managment.models import Worker, TradePoint, Visit


class WorkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Worker
        fields = '__all__'
        read_only_fields = ('name', 'phone_number')


class TradePointSerializer(serializers.ModelSerializer):
    class Meta:
        model = TradePoint
        exclude = ('worker',)
        read_only_fields = ('name',)


class VisitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visit
        fields = '__all__'
        read_only_fields = ('timestamp',)

    def validate(self, attrs):
        worker: Worker = self.context['worker']
        trade_point: TradePoint = attrs['trade_point']

        if trade_point.worker.id != worker.id:
            raise ValidationError('Worker number is not connected')

        return attrs
