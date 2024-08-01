from django.forms import BooleanField, ModelForm

from newsletter.models import Message, Client, Newsletter


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, BooleanField):
                field.widget.attrs['class'] = 'form-check-input'
            else:
                field.widget.attrs['class'] = 'form-control'


class MessageForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Message
        exclude = ('author',)


class ClientForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Client
        exclude = ('author',)


class CreateNewsletterForm(StyleFormMixin, ModelForm):

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super().__init__(*args, **kwargs)
        self.fields['clients'].queryset = Client.objects.filter(author=user)
        self.fields['message'].queryset = Message.objects.filter(author=user)

    class Meta:
        model = Newsletter
        exclude = ('author', 'status')


class UpdateNewsletterForm(CreateNewsletterForm):

    class Meta:
        model = Newsletter
        exclude = ('author',)
