from django.contrib.auth import get_user_model
from django.contrib.auth.forms import (
    UserCreationForm,
    AuthenticationForm,
    PasswordResetForm,
)
from django import forms
from django.core import validators
from django.core.exceptions import ValidationError
from django.forms import inlineformset_factory
from django.utils.translation import gettext_lazy as _
from ckeditor.widgets import CKEditorWidget
from captcha.fields import CaptchaField
from pilkit.processors import ResizeToFill, ResizeToCover


User = get_user_model()

class UserCreationForm(forms.ModelForm):


    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "email", "password","role", "phone_number", "with_child", "sex", "birthday", "note")
        widgets = {
            'sex': forms.RadioSelect
        }
        