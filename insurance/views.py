from django.http import Http404
from rest_framework.views import APIView
from .models import Insurance
from .serializers import InsuranceSerializer
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404


class InsuranceList(APIView):

    def get(self, request, format=None):
        insurances = Insurance.objects.all()
        serializer = InsuranceSerializer(insurances, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = InsuranceSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class InsuranceDetail(APIView):


    def get(self, request, pk, format=None):
        insurance = get_object_or_404(Insurance, pk=pk)
        serializer = InsuranceSerializer(insurance)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        insurance = get_object_or_404(Insurance, pk=pk)
        serializer = InsuranceSerializer(insurance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        insurance = get_object_or_404(Insurance, pk=pk)
        insurance.delete()
        return Response(
            {
                "message": f"ID: {pk} is successfully deleted on the database!"
            },
            status=status.HTTP_204_NO_CONTENT
        )

