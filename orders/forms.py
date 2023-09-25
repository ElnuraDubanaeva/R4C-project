from django import forms


class OrderRobotForm(forms.Form):
    model = forms.CharField(max_length=2, required=True)
    version = forms.CharField(max_length=2, required=True)
    email = forms.EmailField(max_length=255, required=True)
