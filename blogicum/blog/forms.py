from django import forms

from .models import Post, Comment, User


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        exclude = ('author',)
        # Это добавит удобный календарик для выбора даты
        widgets = {
            'pub_date': forms.DateInput(attrs={'type': 'date'})
        }

    # Мы переопределяем инициализацию формы, чтобы вручную отключить проверку
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Эти две строчки принудительно делают поля необязательными,
        # даже если в модели что-то пошло не так.
        self.fields['category'].required = False
        self.fields['location'].required = False


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('text',)


class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')