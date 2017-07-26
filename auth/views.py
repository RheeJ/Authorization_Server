# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes, detail_route
from rest_framework.response import Response
import requests
# Create your views here.

@api_view(["POST"])
@permission_classes((permissions.AllowAny,))
def login(r):
    """
    Input: User Email and User Password (str, str)
    Output: Access Credentials as JWT Payload
    Login using email and password to generate a user access token. Using the Authorization : Bearer <access_token> header, user can access certain features.
    """
    email, password  = r.POST.get('email'), r.POST.get('password')
    payload = (('grant_type', 'password'), ('username', email), ('password', password), ('client_id', 'kb2oCM69TqC7rOHzUQKn3mkDiSOgnE6TITBJTjsN'), ('client_secret', 'kgNZRelRLHNZHWO0kfl55FQq6s8tfamCGG04RTmTLOZxSfrcXbDex2ZulRWXuyoEwJF68QSjGjSdCQT3sw2N9HHjvVbB3YQinwlyJCWGKyD893dRIcie1R2TUes5iHo1'))
    resp = requests.post('http://127.0.0.1:8000/oauth/token/', data=payload)
    if resp.status_code == 200:
        return Response(resp.json(), 200)
    else:
        return Response('',401)

@api_view(["GET"])
@permission_classes((permissions.IsAuthenticated,))
def verify(r):
    user = r.user
    return Response(user.username,200)
