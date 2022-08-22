from django import forms

from .models import LocalWarehousingApplication


class LocalWarehousingApplicationForm(forms.ModelForm):
    class Meta:
        model = LocalWarehousingApplication
        fields = ["app_code", "des", "create_user"]
    # app_code = forms.CharField()
