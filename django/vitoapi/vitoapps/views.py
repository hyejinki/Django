from django.shortcuts import render
import requests
from rest_framework.response import Response
from django.http.response import JsonResponse
import json

# Create your views here.
BASE_URL = 'https://openapi.vito.ai/V1/'

def index(request):
    token_url = 'https://openapi.vito.ai/v1/authenticate'
    
    try:
        resp = requests.post(token_url, data={'client_id': 'ZPu3i4SYh-hk8Wp6OCLX', 'client_secret': 'GmDrq0gmuc3YBnjCyzi9iLZrpKXXj_QoA31pm4r4'})
        resp.raise_for_status()
        data = resp.json()
        token = data.get('access_token')
        # return JsonResponse({'token' : token})
        
    except requests.exceptions.RequestException as e:
        # Handle any errors that might occur during the API request.
        return render(request,  {'error_message': 'Failed to get token.'})
   
    id_url = 'https://openapi.vito.ai/V1/transcribe'
    config = {
        "diarization": {
            "use_verification": False
        },
        "use_multi_channel":False
    }
    
    try:
        resp1 = requests.post(id_url, headers = {'Authorization': 'bearer ' + token},
                            data = {'config' : json.dumps(config)},
                            files = {'file': open('./sample2.m4a', 'rb')}
                            )
        
        print(resp1)
        data1 = resp1.json()
        
        id = data1.get('id')
        resp1.raise_for_status()
        
        return JsonResponse({'id':id})
    except requests.exceptions.RequestException as e:
        # Handle any errors that might occur during the API request.
        print(e)
        return JsonResponse({'error_message': 'Failed to get id'})