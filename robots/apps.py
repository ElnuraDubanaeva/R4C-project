from django.apps import AppConfig


class RobotsConfig(AppConfig):
    name = "robots"

    def ready(self):
        from .signals import check_robot_availability
