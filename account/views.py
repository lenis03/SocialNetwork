from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from django.contrib import messages

from .forms import UserRegisterForm


class RegisterView(View):
    form_class = UserRegisterForm
    template_name = 'account/register.html'

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            User.objects.create_user(
                cd['user_name'],
                cd['email'],
                cd['password1']
                )
            messages.success(request, 'User created successfully', 'success')
            return redirect('home:home_page')

        return render(request, self.template_name, {'form': form})
