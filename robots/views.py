import json
from django.http import HttpResponse
from django.http import JsonResponse
from django.views import View
from .forms import RobotForm
from .services import ExcelServices


class CreateRobotView(View):
    form_class = RobotForm

    def post(self, request):
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError as e:
            return JsonResponse({"error": "Invalid JSON data"}, status=400)

        form = self.form_class(data)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.serial = f"{instance.model}-{instance.version}"
            try:
                instance.save()
                return JsonResponse({"message": "Robot created successfully"})
            except Exception as e:
                return JsonResponse({"error": str(e)}, status=400)
        else:
            return JsonResponse({"error": form.errors}, status=400)


class InstallExcelAPIView(View):
    def get(self, request, *args, **kwargs):
        workbook = ExcelServices.get_excel_robots(request)
        response = HttpResponse(content_type="application/ms-excel")
        response["Content-Disposition"] = 'attachment; filename="robots.xlsx"'
        workbook.save(response)
        return response
