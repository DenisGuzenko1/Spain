from django import forms

from .models import User


class UserForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['level'].empty_label = ''

    class Meta:
        model = User
        fields = ['name', 'phone_number', 'mail', 'level', 'target', 'time', 'communication_method',
                  'special_requirements', 'experience',
                  'about_user', 'comments']
        widgets = {
            'mail': forms.TextInput(attrs={'cols': 20, 'rows': 1}),
            'name': forms.TextInput(attrs={'size': '24'}),
            'target': forms.Textarea(attrs={'cols': 20, 'rows': 1}),
            'special_requirements': forms.Textarea(attrs={'cols': 22, 'rows': 1}),
            'experience': forms.Textarea(attrs={'cols': 22, 'rows': 1}),
            'comments': forms.Textarea(attrs={'cols': 20, 'rows': 1}),
            'about_user': forms.Textarea(attrs={'cols': 20, 'rows': 1})
        }
