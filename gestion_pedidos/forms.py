from django.forms import ModelForm

from .models import Pedido



class FormularioPedido(ModelForm):
    "Modelo de formulario para crear un pedido"
    
    class Meta:
        model = Pedido
        fields = '__all__'

    