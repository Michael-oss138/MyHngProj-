from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from datetime import datetime, timezone
import requests

# Create your views here.
@api_view(['GET'])
def me(request):
    try:
        req = requests.get("https://catfact.ninja/fact", timeout=5)
        res.raise_for_status()
        fact = res.json().get("facts", "Cats are lovely creatures")
    except Exception:
        fact = "failed to get cat fact."

    data ={
        "status": "success",
        user: {
            "name": "Nwaizu Michael",
            "email": "nwaizumichael0@gmail.com",
            "stack": "Python/Django"
        },
        timestamp: datetime.now(tz=timezone.utc).isoformat(),
        "fact": fact
    }

    return Response(data)

