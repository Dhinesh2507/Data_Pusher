import requests
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from accounts.models import Account
from destinations.models import Destination


@api_view(['POST'])
def incoming_data(request):
    app_secret_token = request.headers.get('CL-X-TOKEN')

    if not app_secret_token:
        return Response({"detail": "Un Authenticate"}, status=status.HTTP_401_UNAUTHORIZED)

    try:
        account = Account.objects.get(app_secret_token=app_secret_token)
    except Account.DoesNotExist:
        return Response({"detail": "Un Authenticate"}, status=status.HTTP_401_UNAUTHORIZED)

    data = request.data
    destinations = account.destinations.all()

    for destination in destinations:
        if destination.http_method.lower() == 'get':
            response = requests.get(destination.url, headers=destination.headers, params=data)
        else:
            response = requests.request(destination.http_method, destination.url, headers=destination.headers,
                                        json=data)

    return Response({"detail": "Data sent successfully"}, status=status.HTTP_200_OK)
