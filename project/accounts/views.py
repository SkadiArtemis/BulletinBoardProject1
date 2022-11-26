from django.contrib.auth.models import (User,
                                        Group)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404
from django.views.generic import (UpdateView,
                                  FormView)
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import UserAuth
from .forms import (EditProfileForm,
                    Auth_codeForm)
import random


code_not_correct = str('')


class AccountProfileViews(LoginRequiredMixin,FormView):
    template_name = 'allauth/account/profile.html'
    form_class = Auth_codeForm

    def dispatch(self, request, *args, **kwargs):
        if UserAuth.objects.filter(user=self.request.user).exists():
            return super().dispatch(request, *args, **kwargs)
        return HttpResponseRedirect(reverse('auth_code'))

    def form_valid(self, form, **kwargs):
        global code_not_correct
        if form.cleaned_data['code'] == UserAuth.objects.get(user=self.request.user).code:
            Group.objects.get(name='AuthUsers').user_set.add(self.request.user)
        else:
            code_not_correct = 'Введен неверный код подтвержения'
        return HttpResponseRedirect(reverse('account_profile'))

    def get_context_data(self, **kwargs):
        context = super(AccountProfileViews, self).get_context_data(**kwargs)
        context['code_not_correct'] = code_not_correct
        if self.request.user.groups.filter(name='AuthUsers').exists():
            context['auth'] = True
        else:
            context['auth'] = False
        return context


@login_required
def auth_code(request):
    global code_not_correct
    code_not_correct = ''

    if not UserAuth.objects.filter(user=request.user).exests():
        add_user = UserAuth()
        add_user.user = request.user
        add_user.save()

    user = UserAuth.objects.get(user=request.user)
    user.code = random.randint(1000, 9999)
    user.save()
    send_mail(
        subject=f'MMORPG Bulletin Board:  подтверждение e-mail',
        message=f'Доброго дня, {request.user}! Для подтверждения регистрации, введите код {user.code} на '
                f'странице регистрации\nhttp://127.0.0.1:8000/accounts/profile',
        from_email='artemis.apollo1999@gmail.com',
        recipient_list=[request.user.email, ],
    )
    return HttpResponseRedirect(reverse('account_profile'))


class UpdateProfileViews(LoginRequiredMixin, UpdateView):
    model = User
    form_class = EditProfileForm
    success_url = 'accounts/profile'
    template_name = 'allauth/account/update_profile.html'

    def setup(self, request, *args, **kwargs):
        self.user_id = request.user.pk
        return super().setup(request, *args, **kwargs)

    def get_object(self, queryset=None):
        if not queryset:
            queryset = self.get_queryset()
        return get_object_or_404(queryset, pk=self.user_id)