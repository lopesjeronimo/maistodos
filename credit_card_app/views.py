from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet, ViewSet

from credit_card_app.models import CreditCard
from credit_card_app.serializers import CreditCardSerializer

# Create your views here.


class CreditCardViewSet(ModelViewSet):
    queryset = CreditCard.objects.all()
    serializer_class = CreditCardSerializer
