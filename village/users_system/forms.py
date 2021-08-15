from django import forms
from django.contrib.auth.models import User

class LoginForm(forms.ModelForm):
    """That form for login User"""
    password = forms.CharField(widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        self.fields['username'].label = 'Логин'
        self.fields['password'].label = 'Пароль'
        self.fields['username'].widget.attrs.update({'class':'form-control'})
        self.fields['password'].widget.attrs.update({'class':'form-control'})

    def clean(self):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        if not User.objects.filter(username = username).exists():
            raise forms.ValidationError(f'Пользователь с логином {username} не найден!')
        user = User.objects.filter(username = username).first()
        if user:
            if not user.check_password(password):
                raise forms.ValidationError("Неверный пароль!")
        return self.cleaned_data

    class Meta:
        model = User
        fields = ['username', 'password']




class RegistrationForm(forms.ModelForm):
    """This form for registrate user"""
    confirm_password = forms.CharField(widget = forms.PasswordInput)
    password = forms.CharField(widget = forms.PasswordInput)        
    email = forms.EmailField(required = True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Логин'
        self.fields['password'].label = 'Пароль'
        self.fields['confirm_password'].label = 'Подтвердите пароль'
        self.fields['email'].label = 'Адрес электронной почты'
        self.fields['first_name'].label = 'Ваше имя'
        self.fields['last_name'].label = 'Ваша фамилия'
        self.fields['username'].widget.attrs.update({'class':'form-control'})
        self.fields['password'].widget.attrs.update({'class':'form-control'})
        self.fields['confirm_password'].widget.attrs.update({'class':'form-control'})
        self.fields['email'].widget.attrs.update({'class':'form-control'})
        self.fields['first_name'].widget.attrs.update({'class':'form-control'})
        self.fields['last_name'].widget.attrs.update({'class':'form-control'})

    def clean_email(self):
        email = self.cleaned_data['email']

        if User.objects.filter(email = email).exists():
            raise forms.ValidationError("Пользователь с таким адрессом электронной почты уже зарегистрирован") 
        return email

    def clean_username(self):
        username = self.cleaned_data['username']

        if User.objects.filter(username = username).exists():
            raise forms.ValidationError(f"Пользователь с username: {username} уже зарегистрирован")
        return username                                    

    def clean(self):
        password = self.cleaned_data['password']
        confirm_password = self.cleaned_data['confirm_password']

        if not password == confirm_password:
            raise forms.ValidationError("Пароли не совпадают")
        return self.cleaned_data

    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password','confirm_password']
