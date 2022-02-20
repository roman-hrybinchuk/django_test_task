import configparser

from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.
from shop_managment.models import TradePoint
from shop_managment.serializers import TradePointSerializer, VisitSerializer


class TradePointList(APIView):

    def get(self, request):
        trade_points = TradePoint.objects.filter(worker=request.user)
        serializer = TradePointSerializer(trade_points, many=True)
        return Response(serializer.data)


class CreateVisit(APIView):
    def post(self, request):
        serializer = VisitSerializer(data=request.data, context={'worker': request.user})

        if not serializer.is_valid():
            return Response(serializer.errors)

        serializer.save()

        return Response(serializer.data)
