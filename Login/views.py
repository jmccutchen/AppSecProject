from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserChangeForm
from django.urls import reverse_lazy
from .forms import EditProfileForm
from django.contrib import messages

# to use below do from .forms import SignUpForm and add from django.contrib.auth.forms import UserCreationForm
# class UserRegisterView(generic.CreateView):
#     form_class = SignUpForm
#     template_name = 'registration/register.html'
#     success_url = reverse_lazy('login')


class UserEditView(generic.UpdateView):
    form_class = EditProfileForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user
