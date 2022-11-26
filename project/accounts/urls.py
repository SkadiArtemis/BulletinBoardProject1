from django.urls import (path,
                         include)
from .views import (AccountProfileViews,
                    UpdateProfileViews,
                    auth_code)


urlpatterns = [
  path('profile', AccountProfileViews.as_view(), name='account_profile'),
  path('edit', UpdateProfileViews.as_view(), name='account_edit'),
  path('auth_code', auth_code, name='auth_code'),
  path('', include('allauth.urls')),
]