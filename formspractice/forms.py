from django import forms
import datetime


class ExampleForm(forms.Form):
    name = forms.CharField()
    comment = forms.CharField(widget=forms.Textarea(attrs={'rows': 3}))
    email = forms.EmailField(
        label="Please enter your email address"
    )
    agree = forms.BooleanField()
    date = forms.DateField(widget=forms.NumberInput(attrs={'type': 'date'}))
    birt_year_choices = ['1988', '1989', '1990']
    birth_year = forms.DateField(
        widget=forms.SelectDateWidget(years=birt_year_choices))
    value = forms.DecimalField()
    first_name = forms.CharField(initial="Md Jahirul Islam")
    today = forms.DateField(initial=datetime.date.today)
    color_choices = [
        ('blue', 'Blue'),
        ('green', 'Green'),
        ('black', 'Black'),
        ('red', 'Red'),
    ]
    favorite_color = forms.ChoiceField(choices=color_choices)
    favorite_colors = forms.ChoiceField(
        widget=forms.RadioSelect, choices=color_choices)
    new_favorite_colors = forms.MultipleChoiceField(choices=color_choices)
    new_favorite_colors2 = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple, choices=color_choices)
    roll_number = forms.IntegerField(
        help_text="Enter 6 digit roll number"
    )
    password = forms.CharField(
        widget=forms.PasswordInput()
    )
    decimal_number = forms.DecimalField(max_digits=5, decimal_places=2)
    json_field = forms.JSONField()
