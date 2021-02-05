from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserChangeForm
from django.urls import reverse_lazy
from .forms import EditProfileForm
from django.contrib import messages

class UserEditView(generic.UpdateView):
    form_class = EditProfileForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user
