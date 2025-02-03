<<<<<<< HEAD
from django import forms
from django.core import validators


class contactForm(forms.Form):
    name = forms.CharField(label='Your Name', widget=forms.Textarea(attrs={
                           'placeholder': 'Your Name'}), help_text='name should be less than 100 characters')
    email = forms.EmailField(label='Your Email')
    # file = forms.FileField(label='Your File')
    # age = forms.IntegerField(label='Your Age')
    # balance = forms.DecimalField(label='Your Balance')
    # weight = forms.FloatField(label='Your Weight')
    age = forms.CharField(label='Your Age', widget=forms.NumberInput)
    check = forms.BooleanField(label='Check')
    birthdate = forms.CharField(
        label='Birthdate', widget=forms.DateInput(attrs={'type': 'date'}))
    appointment = forms.CharField(label='Appointment', widget=forms.DateTimeInput(
        attrs={'type': 'datetime-local'}))
    CHOICES = [('S', 'Small'), ('M', 'Medium'), ('L', 'Large')]
    size = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
    MEAL = [('B', 'Breakfast'), ('L', 'Lunch'), ('D', 'Dinner')]
    meal = forms.MultipleChoiceField(
        choices=MEAL, widget=forms.CheckboxSelectMultiple)


# class StudentData(forms.Form):
#     name = forms.CharField(label='Your Name', widget=forms.TextInput)
#     email = forms.CharField(label='Your Email', widget=forms.EmailInput)
#     # def clean_name(self):
#     #     valname = self.cleaned_data['name']
#     #     if len(valname) < 4:
#     #         raise forms.ValidationError('Name should be greater than 4 characters')
#     #     return valname
#     # def clean_email(self):
#     #     valemail = self.cleaned_data['email']
#     #     if '@gmail.com' not in valemail:
#     #         raise forms.ValidationError('Email must contain @gmail.com')
#     #     return valemail

#     # or we can use this method to validate the form

#     def clean(self):
#         cleaned_data = super().clean()
#         valname = self.cleaned_data['name']
#         valemail = self.cleaned_data['email']
#         if len(valname) < 4:
#             raise forms.ValidationError(
#                 'Name should be greater than 4 characters')
#         if '@gmail.com' not in valemail:
#             raise forms.ValidationError('Email must contain @gmail.com')


def len_check(value):
    if len(value) < 10:
        raise forms.ValidationError('Name should be greater than or equal 10 characters')
    
class StudentData(forms.Form):
    name = forms.CharField(label='Your Name', widget=forms.TextInput, validators=[validators.MinLengthValidator(5, message='Name should be greater than 4 characters'), validators.MaxLengthValidator(10, message='Name should be less than 10 characters')])

    text = forms.CharField(label='Your Text', widget=forms.Textarea, validators=[len_check])

    email = forms.CharField(label='Your Email', widget=forms.EmailInput,validators=[validators.EmailValidator(message='Email must contain @gmail.com')])

    age = forms.IntegerField(label='Your Age' , widget=forms.NumberInput, validators=[validators.MinValueValidator(18, message='Age should be greater than or equal 18'), validators.MaxValueValidator(25, message='Age should be less than or equal 25')])

    file = forms.FileField(label='Your File', validators=[validators.FileExtensionValidator(allowed_extensions=['pdf', 'docs', 'jpg'], message='File must be pdf or docs or jpg')])

class Passwordvalidation(forms.Form):
    name = forms.CharField(label='Your Name', widget=forms.TextInput)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    confirm_password = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        valpass = self.cleaned_data['password']
        valcpass = self.cleaned_data['confirm_password']
        if valpass != valcpass:
            raise forms.ValidationError('Password and Confirm Password must be same')
=======
from django import forms
from django.core import validators


class contactForm(forms.Form):
    name = forms.CharField(label='Your Name', widget=forms.Textarea(attrs={
                           'placeholder': 'Your Name'}), help_text='name should be less than 100 characters')
    email = forms.EmailField(label='Your Email')
    # file = forms.FileField(label='Your File')
    # age = forms.IntegerField(label='Your Age')
    # balance = forms.DecimalField(label='Your Balance')
    # weight = forms.FloatField(label='Your Weight')
    age = forms.CharField(label='Your Age', widget=forms.NumberInput)
    check = forms.BooleanField(label='Check')
    birthdate = forms.CharField(
        label='Birthdate', widget=forms.DateInput(attrs={'type': 'date'}))
    appointment = forms.CharField(label='Appointment', widget=forms.DateTimeInput(
        attrs={'type': 'datetime-local'}))
    CHOICES = [('S', 'Small'), ('M', 'Medium'), ('L', 'Large')]
    size = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
    MEAL = [('B', 'Breakfast'), ('L', 'Lunch'), ('D', 'Dinner')]
    meal = forms.MultipleChoiceField(
        choices=MEAL, widget=forms.CheckboxSelectMultiple)


# class StudentData(forms.Form):
#     name = forms.CharField(label='Your Name', widget=forms.TextInput)
#     email = forms.CharField(label='Your Email', widget=forms.EmailInput)
#     # def clean_name(self):
#     #     valname = self.cleaned_data['name']
#     #     if len(valname) < 4:
#     #         raise forms.ValidationError('Name should be greater than 4 characters')
#     #     return valname
#     # def clean_email(self):
#     #     valemail = self.cleaned_data['email']
#     #     if '@gmail.com' not in valemail:
#     #         raise forms.ValidationError('Email must contain @gmail.com')
#     #     return valemail

#     # or we can use this method to validate the form

#     def clean(self):
#         cleaned_data = super().clean()
#         valname = self.cleaned_data['name']
#         valemail = self.cleaned_data['email']
#         if len(valname) < 4:
#             raise forms.ValidationError(
#                 'Name should be greater than 4 characters')
#         if '@gmail.com' not in valemail:
#             raise forms.ValidationError('Email must contain @gmail.com')


def len_check(value):
    if len(value) < 10:
        raise forms.ValidationError('Name should be greater than or equal 10 characters')
    
class StudentData(forms.Form):
    name = forms.CharField(label='Your Name', widget=forms.TextInput, validators=[validators.MinLengthValidator(5, message='Name should be greater than 4 characters'), validators.MaxLengthValidator(10, message='Name should be less than 10 characters')])

    text = forms.CharField(label='Your Text', widget=forms.Textarea, validators=[len_check])

    email = forms.CharField(label='Your Email', widget=forms.EmailInput,validators=[validators.EmailValidator(message='Email must contain @gmail.com')])

    age = forms.IntegerField(label='Your Age' , widget=forms.NumberInput, validators=[validators.MinValueValidator(18, message='Age should be greater than or equal 18'), validators.MaxValueValidator(25, message='Age should be less than or equal 25')])

    file = forms.FileField(label='Your File', validators=[validators.FileExtensionValidator(allowed_extensions=['pdf', 'docs', 'jpg'], message='File must be pdf or docs or jpg')])

class Passwordvalidation(forms.Form):
    name = forms.CharField(label='Your Name', widget=forms.TextInput)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    confirm_password = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        valpass = self.cleaned_data['password']
        valcpass = self.cleaned_data['confirm_password']
        if valpass != valcpass:
            raise forms.ValidationError('Password and Confirm Password must be same')
>>>>>>> af6d9f7c37900db1dbc9b7b8ef4ae50f40336f55
        return cleaned_data