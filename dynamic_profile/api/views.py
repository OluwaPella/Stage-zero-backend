import os
import requests
import logging
from datetime import datetime
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Setup logging
logger = logging.getLogger(__name__)

# Environment variables with fallbacks
CAT_FACT_API_URL = os.getenv('CAT_FACT_API_URL', 'https://catfact.ninja/fact')
CAT_FACT_TIMEOUT = int(os.getenv('CAT_FACT_TIMEOUT', '5'))
FALLBACK_MESSAGE = "Cats are wonderful creatures!"

@api_view(['GET'])
def me(request):
    """
    GET /me endpoint that returns profile info and random cat fact
    """
    # Fetch cat fact with proper error handling
    fact = get_cat_fact()
    
    # Build response data
    data = {
        "status": "success",
        "user": {
            "email": "oolaosebikan350@gmail.com",
            "name": "Olaosebikan Pelumi",
            "stack": "Python/Django"
        },
        "timestamp": datetime.utcnow().isoformat() + "Z",  # ISO 8601 format
        "fact": fact
    }
    
    return Response(data, status=200)

def get_cat_fact():
    """Fetch cat fact from API with comprehensive error handling"""
    try:
        response = requests.get(CAT_FACT_API_URL, timeout=CAT_FACT_TIMEOUT)
        response.raise_for_status()  # Raises exception for 4xx/5xx status codes
        
        fact_data = response.json()
        return fact_data.get('fact', FALLBACK_MESSAGE)
        
    except requests.exceptions.Timeout:
        logger.warning("Cat Facts API timeout")
        return "Unable to fetch cat fact: API timeout"
        
    except requests.exceptions.ConnectionError:
        logger.warning("Cat Facts API connection error")
        return "Unable to fetch cat fact: Connection failed"
        
    except requests.exceptions.HTTPError as e:
        logger.warning(f"Cat Facts API HTTP error: {e.response.status_code}")
        return f"Unable to fetch cat fact: HTTP {e.response.status_code}"
        
    except requests.exceptions.RequestException as e:
        logger.warning(f"Cat Facts API request error: {str(e)}")
        return "Unable to fetch cat fact: Request failed"
        
    except Exception as e:
        logger.error(f"Unexpected error fetching cat fact: {str(e)}")
        return FALLBACK_MESSAGE
