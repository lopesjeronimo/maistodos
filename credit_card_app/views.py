from rest_framework import mixins, viewsets
from rest_framework.permissions import IsAuthenticated

from credit_card_app.models import CreditCard
from credit_card_app.serializers import CreditCardSerializer

# Create your views here.


class CreateListRetrieveViewSet(
    mixins.CreateModelMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet
):
    """
    A viewset that provides `retrieve`, `create`, and `list` actions.

    To use it, override the class and set the `.queryset` and
    `.serializer_class` attributes.
    """

    pass


class CreditCardViewSet(CreateListRetrieveViewSet):
    queryset = CreditCard.objects.all()
    serializer_class = CreditCardSerializer
