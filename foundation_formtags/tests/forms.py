from django import forms

CHOICES = (
    ('a', 'Option 1'),
    ('b', 'Option 2'),
    ('c', 'Option 3'),
)


class SimpleForm(forms.Form):
    text = forms.CharField(label='text')


class ComplexForm(forms.Form):
    char_field = forms.CharField()
    char_field_widget = forms.CharField(widget=forms.TextInput(attrs={'class':'foo'}))
    choice_field = forms.ChoiceField(choices=CHOICES)
    radio_choice = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
    multiple_choice = forms.MultipleChoiceField(choices=CHOICES)
    multiple_checkbox = forms.MultipleChoiceField(
        choices=CHOICES, widget=forms.CheckboxSelectMultiple
    )
    file_field = forms.FileField()
    password_field = forms.CharField(widget=forms.PasswordInput)
    textarea = forms.CharField(widget=forms.Textarea)
    boolean_field = forms.BooleanField()
