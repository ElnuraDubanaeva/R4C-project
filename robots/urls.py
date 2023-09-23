from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from .views import CreateRobotView, InstallExcelAPIView


urlpatterns = [
    path("robot/create/", csrf_exempt(CreateRobotView.as_view()), name="create-robot"),
    path(
        "robot/excel-install/",
        csrf_exempt(InstallExcelAPIView.as_view()),
        name="excel-install",
    ),
]
