from django.shortcuts import render, redirect
from .import models, serializers
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from rest_framework.authtoken.models import Token
# Create your views here.


class PatientViewSet(viewsets.ModelViewSet):
    queryset = models.Patient.objects.all()
    serializer_class = serializers.PatientSerializer


class UserRegistrationApiView(APIView):
    serializer_class = serializers.UserRegistrationSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            user = serializer.save()
            print(user)
            token = default_token_generator.make_token(user)
            print(token)
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            print("uid", uid)
            confirm_link = f"http://127.0.0.1:8000/patient/activate/{uid}/{token}"
            email_subject = "Activate your account"
            email_body = render_to_string(
                'confirm_email.html', {'confirm_link': confirm_link})
            email = EmailMultiAlternatives(
                email_subject,
                '',
                to=[user.email]
            )
            email.attach_alternative(email_body, "text/html")
            email.send()

            return Response({"Registration successful. Please check your email to activate your account."})
        return Response(serializer.errors)


def activate(request, uid64, token):
    try:
        uid = urlsafe_base64_decode(uid64).decode()
        # user = User.objects.get(pk=uid)
        user = User._default_manager.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        return redirect('login')
    else:
        return redirect('register')


class UserLoginApiView(APIView):
    def post(self, request):
        serializer = serializers.UserLoginSerializer(data=self.request.data)

        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            user = authenticate(username=username, password=password)

            if user:
                token = Token.objects.get_or_create(user=user)
                login(request, user)
                print(token)
                return Response({"token": token[0].key, 'user_id': user.id})
            else:
                return Response({"Error": "Invalid credentials."})
        return Response(serializer.errors)


class UserLogoutApiView(APIView):
    def get(self, request):
        request.user.auth_token.delete()
        logout(request)
        return redirect('login')
