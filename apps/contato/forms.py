from django import forms
from .models import Contato

ASSUNTOS_CHOICES = [
    ('Dúvida', 'Dúvida'),
    ('Elogio', 'Elogio'),
    ('Reclamação', 'Reclamação'),
    ('Outro', 'Outro')
]

class ContatoForm(forms.ModelForm):
    assunto = forms.ChoiceField(choices=ASSUNTOS_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    class Meta:
        model = Contato
        fields = ['assunto', 'nome', 'email', 'mensagem']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'mensagem': forms.Textarea(attrs={'class': 'form-control'}),
        }
