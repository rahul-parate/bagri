from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class FirstView(APIView):

	def get(self, request, *args, **kwargs):
		print(request)
		return Response(status=status.HTTP_200_OK)