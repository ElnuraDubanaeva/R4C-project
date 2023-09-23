from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from .views import CreateRobotView


urlpatterns = [
    path("robot/create/", csrf_exempt(CreateRobotView.as_view()), name="create-robot"),
]
