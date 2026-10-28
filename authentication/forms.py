# from django import forms
# from django.contrib.auth import get_user_model
# from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

# User = get_user_model()


# def style_fields(form, placeholders=None, autocomplete=None):
#     """Give every widget the same CSS class (and optional placeholder/autocomplete)."""
#     placeholders = placeholders or {}
#     autocomplete = autocomplete or {}
#     for name, field in form.fields.items():
#         field.widget.attrs["class"] = "field-input"
#         if name in placeholders:
#             field.widget.attrs["placeholder"] = placeholders[name]
#         if name in autocomplete:
#             field.widget.attrs["autocomplete"] = autocomplete[name]


# class RegisterForm(UserCreationForm):
#     first_name = forms.CharField(max_length=150, label="First name")
#     last_name = forms.CharField(max_length=150, label="Last name")
#     email = forms.EmailField(label="Email address")

#     field_order = [
#         "first_name", "last_name", "email", "username", "password1", "password2",
#     ]

#     class Meta(UserCreationForm.Meta):
#         model = User
#         fields = ("first_name", "last_name", "email", "username")

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields["password1"].label = "Password"
#         self.fields["password2"].label = "Confirm password"
#         style_fields(
#             self,
#             placeholders={
#                 "first_name": "First name",
#                 "last_name": "Last name",
#                 "email": "you@example.com",
#                 "username": "Choose a username",
#             },
#             autocomplete={
#                 "first_name": "given-name",
#                 "last_name": "family-name",
#                 "email": "email",
#                 "username": "username",
#                 "password1": "new-password",
#                 "password2": "new-password",
#             },
#         )

#     def clean_email(self):
#         email = self.cleaned_data["email"].strip().lower()
#         if User.objects.filter(email__iexact=email).exists():
#             raise forms.ValidationError("An account with this email already exists.")
#         return email


# class LoginForm(AuthenticationForm):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields["username"].label = "Username"
#         style_fields(
#             self,
#             placeholders={"username": "Your username"},
#             autocomplete={"username": "username", "password": "current-password"},
#         )
#         self.fields["password"].widget.attrs["placeholder"] = "Your password"