from django.views import View
from django.http import JsonResponse
from common.services import ValidateService
from .forms import OrderRobotForm
from .services import OrderService


class OrderRobotView(View):
    form_class = OrderRobotForm

    def post(self, request):
        data = ValidateService.validate_json(request.body)
        form = self.form_class(data)
        if form.is_valid():
            data = OrderService.make_order(form.cleaned_data)
            return JsonResponse({"data": data}, status=200)
        else:
            return JsonResponse({"error": form.errors}, status=400)
