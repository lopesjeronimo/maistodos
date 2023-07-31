from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet, ViewSet

from credit_card_app.models import CreditCard
from credit_card_app.serializers import CreditCardSerializer

# Create your views here.


from rest_framework import mixins, viewsets


class CreateListRetrieveViewSet(mixins.CreateModelMixin,
                                mixins.ListModelMixin,
                                mixins.RetrieveModelMixin,
                                viewsets.GenericViewSet):
    """
    A viewset that provides `retrieve`, `create`, and `list` actions.

    To use it, override the class and set the `.queryset` and
    `.serializer_class` attributes.
    """
    pass


class CreditCardViewSet(CreateListRetrieveViewSet):
    queryset = CreditCard.objects.all()
    serializer_class = CreditCardSerializer
