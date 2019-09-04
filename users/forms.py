from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import User


class AccountCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'password1', 'password2', 'first_name', 'last_name', 'profession', 'department')


class AccountChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('email',)
