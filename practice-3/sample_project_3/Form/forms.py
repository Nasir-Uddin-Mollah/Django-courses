from django import forms
import datetime
from django.forms.widgets import NumberInput

class Exampleform(forms.Form):
    name = forms.CharField(label='Your name', initial='Nasir')
    email = forms.EmailField()
    comment = forms.CharField(widget=forms.Textarea)
    agree = forms.BooleanField()
    comment2 = forms.CharField(widget=forms.Textarea(attrs={'rows': 2}))
    date = forms.DateField()
    birthdate = forms.DateField(widget=NumberInput(attrs={'type': 'date'}))

    BIRTH_YEAR_CHOICES = ['1980', '1981', '1982']
    birth_year = forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES))
    
    value = forms.DecimalField()
    message = forms.CharField(max_length=20)
    day = forms.DateField(initial=datetime.date.today)

    FAVORITE_COLORS_CHOICES = [
        ('blue', 'Blue'),
        ('green', 'Green'),
        ('black', 'Black'),
    ]
    favorite_color = forms.ChoiceField(choices=FAVORITE_COLORS_CHOICES)

    FAVORITE_COLORS_CHOICES2 = [
        ('blue', 'Blue'),
        ('green', 'Green'),
        ('black', 'Black'),
    ]
    favorite_color2 = forms.ChoiceField(widget=forms.RadioSelect, choices=FAVORITE_COLORS_CHOICES2)

    FAVORITE_COLORS_CHOICES3 = [
        ('blue', 'Blue'),
        ('green', 'Green'),
        ('black', 'Black'),
    ]
    favorite_color3 = forms.MultipleChoiceField(choices=FAVORITE_COLORS_CHOICES3)

    FAVORITE_COLORS_CHOICES4 = [
        ('blue', 'Blue'),
        ('green', 'Green'),
        ('black', 'Black'),
    ]
    favorite_color4 = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=FAVORITE_COLORS_CHOICES4)

    roll = forms.IntegerField(help_text = "Enter 6 digit roll number") 
    password = forms.CharField(widget = forms.PasswordInput()) 
    file = forms.FileField()
    image = forms.ImageField()
    # regex = forms.RegexField(regex="G.*s")
    url = forms.URLField()
    datetime = forms.DateTimeField(widget=NumberInput(attrs={'type': 'datetime-local'}))

    GEEKS_CHOICES = ( 
        (1, "A"), 
        (2, "B"), 
        (3, "C"), 
        (4, "D"), 
        (5, "E"), 
    )
    geek = forms.TypedChoiceField(choices=GEEKS_CHOICES, coerce=int)

    field = forms.NullBooleanField( ) 
    timec= forms.TimeField(widget=NumberInput(attrs={'type': 'time'}))
    regex =forms.RegexField(regex = "G.*s")