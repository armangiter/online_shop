from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import View
from .forms import UserRegistrationsFrom, VerifyCodeForm, UserLoginForm
import random
from utils import send_otp_code, IsNotAuthenticatedUserMixin
from .models import OtpCode, User
from django.contrib import messages
from django.utils.translation import gettext_lazy as _


# Create your views here.

class UserRegisterView(IsNotAuthenticatedUserMixin, View):
    form_class = UserRegistrationsFrom
    template_name = 'customer/register.html'

    def get(self, request):
        form = self.form_class
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            random_code = random.randint(1000, 9999)
            send_otp_code(form.cleaned_data['phone'], random_code)
            OtpCode.objects.create(phone=form.cleaned_data['phone'], code=random_code)
            request.session['user_registrations_info'] = {
                'phone': form.cleaned_data['phone'],
                'email': form.cleaned_data['email'],
                'full_name': form.cleaned_data['full_name'],
                'password': form.cleaned_data['password'],
            }
            messages.success(request, _('we send a code'), 'success')
            return redirect('customer:verify_code')
        return render(request, self.template_name, {'form': form})

    def test_func(self):
        return not self.request.user.is_authenticated


class UserRegisterVerifyCodeView(IsNotAuthenticatedUserMixin, View):
    form_class = VerifyCodeForm

    def get(self, request):
        form = self.form_class
        return render(request, 'customer/verify.html', {'form': form})

    def post(self, request):
        user_session = request.session['user_registrations_info']
        code_instance = OtpCode.objects.get(phone=user_session['phone'])
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            if cd['code'] == code_instance.code:
                User.objects.create_user(phone=user_session['phone'], email=user_session['email'],
                                         full_name=user_session['full_name'], password=user_session['password'])
                code_instance.delete()
                messages.success(request, _('you are registered'), 'success')
                return redirect('home:home')
            else:
                messages.error(request, _('this code is wrong'), 'danger')
                return redirect('customer:verify_code')
        return redirect('home:home')


class UserLoginView(IsNotAuthenticatedUserMixin, View):
    form_class = UserLoginForm
    template_name = 'customer/login.html'

    def get(self, request):
        form = self.form_class
        return render(request, 'customer/login.html', {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            request.session['user_phone'] = {
                'phone': cd['phone']
            }
            random_code = random.randint(1000, 9999)
            send_otp_code(cd["phone"], random_code)
            OtpCode.objects.create(phone=cd['phone'], code=random_code)
            messages.success(request, _('we send a code'), 'success')
            return redirect('customer:login_verify')
        return render(request, self.template_name, {'form': form})


class UserLoginVerifyView(IsNotAuthenticatedUserMixin, View):
    form_class = VerifyCodeForm

    def get(self, request):
        form = self.form_class
        return render(request, 'customer/verify.html', {'form': form})

    def post(self, request):
        user_session = request.session['user_phone']
        code_instance = OtpCode.objects.get(phone=user_session['phone'])
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, phone=user_session['phone'])
            if cd['code'] == code_instance.code and user:
                login(request, user)
                code_instance.delete()
                messages.success(request, _('you are logged in'), 'success')
                return redirect('home:home')
            else:
                messages.error(request, _('this code is wrong'), 'danger')
                return redirect('customer:verify_code')
        return render(request, 'customer/verify.html', {'form': form})


class UserLogoutView(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)
        messages.success(request, _('logged out'), 'success')
        return redirect('home:home')
