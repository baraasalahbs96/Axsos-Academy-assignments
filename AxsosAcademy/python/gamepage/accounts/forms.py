from django import forms
from django.core.exceptions import ValidationError
from datetime import date
from .models import CustomUser, Game


class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email', 'date_of_birth', 'avatar_url']
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
        }

    def clean_first_name(self):
        v = self.cleaned_data.get('first_name', '').strip()
        if not v:
            raise ValidationError('First name should not be blank')
        if len(v) < 4:
            raise ValidationError('First name should be at least 4 characters')
        return v

    def clean_last_name(self):
        v = self.cleaned_data.get('last_name', '').strip()
        if not v:
            raise ValidationError('Last name should not be blank')
        if len(v) < 4:
            raise ValidationError('Last name should be at least 4 characters')
        return v

    def clean_email(self):
        email = self.cleaned_data.get('email', '').strip().lower()
        if not email:
            raise ValidationError('Email should be valid and unique')
        if CustomUser.objects.filter(email=email).exists():
            raise ValidationError('This email is already registered')
        return email

    def clean_date_of_birth(self):
        dob = self.cleaned_data.get('date_of_birth')
        if not dob:
            raise ValidationError('Date of birth is required')
        today = date.today()
        age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
        if age < 18:
            raise ValidationError('User should be 18 years or older')
        return dob

    def clean(self):
        cleaned = super().clean()
        pw = cleaned.get('password')
        cpw = cleaned.get('confirm_password')
        if pw and len(pw) < 8:
            self.add_error('password', 'Password should be at least 8 characters')
        if pw and cpw and pw != cpw:
            self.add_error('confirm_password', 'Password and confirm password should matched')
        return cleaned

    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = self.cleaned_data['email']
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user


class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ['name', 'genre', 'release_date', 'description']
        widgets = {
            'release_date': forms.DateInput(attrs={'type': 'date'}),
            'description': forms.Textarea(attrs={'rows': 5}),
        }

    def clean_name(self):
        name = self.cleaned_data.get('name', '').strip()
        if not name:
            raise ValidationError('Game name should be at least 2 char')
        if len(name) < 2:
            raise ValidationError('Game name should be at least 2 char')
        return name

    def clean_release_date(self):
        rd = self.cleaned_data.get('release_date')
        if not rd:
            raise ValidationError('Release date is required')
        if rd > date.today():
            raise ValidationError('Release date should not be in future')
        return rd

    def clean_description(self):
        desc = self.cleaned_data.get('description', '').strip()
        if not desc:
            raise ValidationError('Description should not be blank')
        return desc