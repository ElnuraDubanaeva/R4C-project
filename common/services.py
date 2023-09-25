import json
from django.http import JsonResponse


class ValidateService:
    @staticmethod
    def validate_json(json_data):
        try:
            data = json.loads(json_data)
        except json.JSONDecodeError as e:
            return JsonResponse({"error": "Invalid JSON data"}, status=400)
        return data
