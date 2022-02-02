from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets, serializers
from django.contrib.auth import (
    authenticate,
    login as django_login,
    logout as django_logout
)
from users.models import CustomUser
from .serializers import *

def register(request):
    if request.method == 'GET':
        return render(request, 'users/register.html')

    elif request.method == 'POST':
        form = request.POST

        username = form['username']
        password = form['password']
        email = form['email']
        first_name = form['first-name']
        last_name = form['last-name']

        new_user = CustomUser.objects.create_user(
            username=username,
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name,
        )

        django_login(request, new_user)
        return HttpResponseRedirect(reverse('board:index'))


def login(request):
    if request.method == 'GET':
        return render(request, 'users/login.html')

    elif request.method == 'POST':
        form = request.POST

        username = form['username']
        password = form['password']

        user = authenticate(request, username=username, password=password)

        if user is None:
            return render(request, 'users/login.html', {'error': 'Invalid Username or Password!'})

        django_login(request, user)
        return HttpResponseRedirect(reverse('board:index'))

def logout(request):
    django_logout(request)
    return HttpResponseRedirect(reverse('board:index'))

""" def account(request):
    if request.method == 'GET':
        return render(request, 'users/account.html')
    elif request.method == 'POST':
        form = request.POST

        username = form['username']
        password = form['password']
        email = form['email']
        first_name = form['first-name']
        last_name = form['last-name']

        user = CustomUser.objects.get(username=username)
        user.email = email
        user.first_name = first_name
        user.last_name = last_name
        user.set_password(password)
        user.save()
        
        django_login(request, user)
        return render(request, 'users/account.html') """
        
@api_view(['POST', 'GET'])
def account(request):
    if request.method == 'POST':
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    else:
        serializer = CustomUserSerializer(request.user)
        return Response(serializer.data)

@api_view(['GET'])
def account_detail(request):
    user = CustomUser.objects.get(username=request.user.username)
    serializer = CustomUserSerializer(user)
    return Response(serializer.data)