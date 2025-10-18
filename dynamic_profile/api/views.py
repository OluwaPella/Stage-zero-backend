import requests
from datetime import datetime
from rest_framework.decorators import api_view
from rest_framework.response import Response

cat_api = "https://catfact.ninja/fact"
time_out = 5
fallback_message = "Cats are wonderful creatures, but the Cat Fact API failed."

@api_view(["GET"])
def me(request):
    """
    This endpoint returns your profile info and
    a random cat fact using the Cat Fact API.
    """
    try:
        response = requests.get(cat_api, timeout=time_out)  # fetch API
        response.raise_for_status()  # raise error if there's status code error like 400 or 500
        fact = response.json().get("fact", "No fact available now, please try again later.")
    except Exception as e:
        # if API failed to fetch
        print("Error fetching cat API:", e)
        fact = fallback_message

    data = {
        "status": "success",
        "user": {
            "email": "oolaosebikan350@gmail.com",
            "name": "Olaosebikan Pelumi",
            "stack": "Python/Django"
        },
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "fact": fact
    }

    return Response(data, status=200)
