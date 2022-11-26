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



