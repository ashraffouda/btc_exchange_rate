from rest_framework import generics
from .models import ExchangeEntry
from rest_framework.decorators import (
    api_view,
    authentication_classes,
    permission_classes,
)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from . import helpers
from rest_framework.authentication import (
    SessionAuthentication,
    BasicAuthentication,
    TokenAuthentication,
)


@api_view(["GET", "POST"])
@authentication_classes(
    [SessionAuthentication, BasicAuthentication, TokenAuthentication]
)
@permission_classes([IsAuthenticated])
def get_exchange_entry(request):
    if request.method == "POST":
        exentry = helpers.get_realtime_exchange_rate()
    elif request.method == "GET":
        exentry = ExchangeEntry.objects.last()
    return Response({"rate": exentry.rate, "time": str(exentry.time)})
