from django.shortcuts import render
from django.views import View
from .forms import UserRegistrationsFrom


# Create your views here.

class UserRegisterView(View):
    form_class = UserRegistrationsFrom

    def get(self, request):
        form = self.form_class
        return render(request, 'customer/register.html', {'form': form})

    def post(self, request):
        pass
