from __future__ import unicode_literals
from django.shortcuts import render
from django.conf import settings
from rest_framework.response import Response
from django.views import View
from .models import *
from .serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework import status
from django_otp.oath import totp
from django_otp.util import random_hex
import time
from django.core.mail import EmailMessage
import random


#------------------------------------------- Activate Account ------------------------------------------
class activate(APIView):	
	def post(self,request):
		print('Activate Function Called')
		params = request.data
		print(params)
		user = users_details.objects.get(Email = params["Email"])
		if user:
			print('User -- Present')
			print('Database OTP = ',user.otp )
			if user.otp == params["otp"]:
				print('OTP Found')
				user.is_activate = True
				print('Account Activated')
				serializer = UserSerializer(user)
				return Response({"data":serializer.data,"message":"Activate Success"}, status=status.HTTP_200_OK)		
			return Response({"message":"Invalid password"}, status=status.HTTP_400_Invalid_Password)					
		return Response({"message":"Email not found"}, status=status.HTTP_400_Email_Not_Found)


#------------------------------------------- Sign Up ------------------------------------------
class signup_user(APIView):
	user1 = users_details.objects.all()
	serializer_class = UserSerializer

	def post(self,request):
		serializer = UserSerializer(data=request.data)
		params = request.data
		if serializer.is_valid():
			serializer.save()
			print('THIS IS SERIALIZER EMAIL : ',params['Email'])
			otp = random.randint(235257,950171)
			client = Client(settings.TWILIO_ACCOUNT_STD, settings.TWILIO_AUTH_TOKEN)
			email = EmailMessage('TODAY TEST : OTP',str(otp), to = [params["Email"]])
			email.send()			
			user = users_details.objects.get(Email = params["Email"])
			user.otp=otp
			user.save()			
			serializer = UserSerializer(user)	
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



#------------------------------------------- LOGIN ------------------------------------------
class login(APIView):	
	def post(self,request):
		params = request.data
		print(params)
		user = users_details.objects.get(Email = params["Email"])
		if user:
			if user.password == params["password"]:
				serializer = UserSerializer(user)
				return Response({"data":serializer.data,"message":"Login Success"}, status=status.HTTP_200_OK)		
			return Response({"message":"Invalid password"}, status=status.HTTP_400_Invalid_Password)					
		return Response({"message":"Email not found"}, status=status.HTTP_400_Email_Not_Found)

#------------------------------------------- display User ------------------------------------------
class display(APIView):
	def post(self,request):
		if serializer.is_valid():
			params = request.data
			user = users_details.objects.get(Email = params["Email"])
			serializer = UserSerializer(user)
			return Response({"User_Details":serializer.data})

			

#------------------------------------------- Delete User ------------------------------------------
class delete_user(APIView):
	def post(self,request):
		params = request.data
		print(params)
		user = users_details.objects.get(Email = params["Email"])
		password = users_details.objects.get(password = params["password"])
		if user:
			if password:
				user.delete()
				return Response({"message":"Delete Success"}, status=status.HTTP_200_OK)		
		return Response({"message":"User NOt Found"}, status=status.HTTP_400_Email_Not_Found)




#------------------------------------------- Edit User ------------------------------------------
class edit_user(APIView):
	def post(self,request):
		params = request.data
		print(params)
		user = users_details.objects.get(Email = params["Email"])
		password = users_details.objects.get(password = params["password"])
		if user:
			if password:
				 user.username = params["new_username"]
				 user.Email = params["new_Email"]
				 user.Phone = params["new_Phone"]
				 user.save()
				 serializer = UserSerializer(user)
				 return Response({"data":serializer.data,"message":"Edit Success"}, status=status.HTTP_200_OK)		
		return Response({"message":"User NOt Found"}, status=status.HTTP_400_Email_Not_Found)



#------------------------------------------- reset_password ------------------------------------------
class reset_password(APIView):
	def post(self,request):
		print('reset_password  CALLED')
		params = request.data
		print(params)
		if  users_details.objects.get(Email = params["Email"]):
			if  users_details.objects.get(otp = params["otp"]):
				user = users_details.objects.get(Email = params["Email"])
				new_password = params["new_password"]
				user.password = new_password
				# user.otp.delete()
				user.save()
				serializer = UserSerializer(user)
				return Response({"Successful :reset_password for":params["Email"]})
		else:
			return Response({"USER NOT FOUND":params["Email"]})





#------------------------------------------- forgot_password ------------------------------------------
class forgot_password(APIView):
	def post(self,request):
		print('SEND OTP  CALLED')
		params = request.data
		print(params)
		if  users_details.objects.get(Email = params["Email"]):
			user = users_details.objects.get(Email = params["Email"])
			user_email = params["Email"]
			otp = random.randint(235257,950171)		
			print('--IM SEND OTP--OTP IS =',otp,type(otp))
			client = Client(settings.TWILIO_ACCOUNT_STD, settings.TWILIO_AUTH_TOKEN)
			email = EmailMessage('TODAY TEST : OTP',str(otp), to = [user_email])
			email.send()
			user = users_details.objects.get(Email = params["Email"])
			user.otp = otp
			user.save()
			serializer = UserSerializer(user)
			return Response({"OTP SENT TO ":user_email})
		else:
			return Response({"USER NOT FOUND with Email":params["Email"]})