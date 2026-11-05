
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

User = get_user_model()


def style_fields(form, placeholders=None, autocomplete=None):
    """Apply consistent styling and accessibility attributes to form fields."""

    placeholders = placeholders or {}
    autocomplete = autocomplete or {}

    for name, field in form.fields.items():
        field.widget.attrs.update({
            "class": "field-input",
        })

        if name in placeholders:
            field.widget.attrs["placeholder"] = placeholders[name]

        if name in autocomplete:
            field.widget.attrs["autocomplete"] = autocomplete[name]


class RegisterForm(UserCreationForm):

    first_name = forms.CharField(
        max_length=150,
        label="First name",
        required=True
    )

    last_name = forms.CharField(
        max_length=150,
        label="Last name",
        required=True
    )

    email = forms.EmailField(
        label="Email address",
        required=True
    )

    phone_number = forms.CharField(
        max_length=20,
        label="Phone number",
        required=True
    )

    field_order = [
        "first_name",
        "last_name",
        "email",
        "phone_number",
        "username",
        "password1",
        "password2",
    ]

    class Meta(UserCreationForm.Meta):
        model = User
        fields = (
            "first_name",
            "last_name",
            "email",
            "phone_number",
            "username",
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["password1"].label = "Password"
        self.fields["password2"].label = "Confirm password"

        style_fields(
            self,
            placeholders={
                "first_name": "Enter your first name",
                "last_name": "Enter your last name",
                "email": "you@example.com",
                "phone_number": "Enter your phone number",
                "username": "Choose a username",
                "password1": "Create a password",
                "password2": "Confirm your password",
            },
            autocomplete={
                "first_name": "given-name",
                "last_name": "family-name",
                "email": "email",
                "phone_number": "tel",
                "username": "username",
                "password1": "new-password",
                "password2": "new-password",
            },
        )

    def clean_email(self):
        email = self.cleaned_data["email"].strip().lower()

        if User.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError(
                "An account with this email already exists."
            )

        return email

    def clean_phone_number(self):
        phone = self.cleaned_data["phone_number"].strip()

        if User.objects.filter(phone_number=phone).exists():
            raise forms.ValidationError(
                "An account with this phone number already exists."
            )

        return phone


class LoginForm(AuthenticationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["username"].label = "Username"
        self.fields["password"].label = "Password"

        style_fields(
            self,
            placeholders={
                "username": "Enter your username",
                "password": "Enter your password",
            },
            autocomplete={
                "username": "username",
                "password": "current-password",
            },
        )
