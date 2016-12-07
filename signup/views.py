from django.shortcuts import render
from django.http import HttpResponse
from models import Users
import json
import time
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.


@api_view(['GET', 'POST'])
def register(request):
    """
    List all snippets, or create a new snippet.
    """
    if request.method == 'GET':
        return Response('get')

    elif request.method == 'POST':

        ''' Sample input
        {
            "client_id" :12,
            "client_secret" : "123sdf",
            "email" : "vaibhav3497@gmail.com",
            "webstore_url" : "www.pingax.com",
            "registered_at" :1234,
            "webstore_platform" : "shopify"
            
        }
        '''
        user_input = request.data

        # Score primary connection information
        temporaryCredentialsRequestUrl = user_input.get('temporaryCredentialsRequestUrl') 
        adminAuthorizationUrl = user_input.get('adminAuthorizationUrl')
        accessTokenRequestUrl = user_input.get('accessTokenRequestUrl')
        apiUrl = user_input.get('apiUrl')
        consumerKey = user_input.get('consumerKey')
        consumerSecret = user_input.get('consumerSecret')

        email = user_input.get('email')
        webstore_url = user_input.get('webstore_url')
        registered_at = user_input.get(time.time())
        webstore_platform = user_input.get('webstore_platform')

        try:
            user = Users(
                         email=email,
                         webstore_url=webstore_url,
                         registered_at=registered_at,
                         webstore_platform=webstore_platform,

                         temporaryCredentialsRequestUrl=temporaryCredentialsRequestUrl,
                         adminAuthorizationUrl=adminAuthorizationUrl,
                         accessTokenRequestUrl=accessTokenRequestUrl,
                         apiUrl=apiUrl,
                         consumerKey=consumerKey,
                         consumerSecret=consumerSecret
                         )
            user.save()

            return Response({"success":True})

        except Exception as e:
            return Response({"message":e})

@api_view(['GET'])
def get_all_users(request):
    user_web=[]
    all_users = Users.objects.all()
    for each_user in all_users:
        # each_user.webstore_url
        user_web.append(each_user.webstore_url)

    return Response({"registered_stores":user_web})