from django.shortcuts import render
from rest_framework.decorators immport api_view
from rest_framework.response import Response
from datetime import datetime, timezone
import requests

# Create your views here.
@api_view(['GET'])
def me(request):
    try:
        req = requests.get("https://catfact.ninja/fact", timeout=5)
        res = raise_for_status()
        fact = res.json().get()