from rest_framework import routers

from credit_card_app.views import CreditCardViewSet

router = routers.SimpleRouter()
router.register(r"credit-card", CreditCardViewSet)

urlpatterns = router.urls
