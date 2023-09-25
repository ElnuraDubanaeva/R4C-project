from django.urls import path
from .views import OrderRobotView
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path("order/robot/", csrf_exempt(OrderRobotView.as_view()), name="order-robot")
]
