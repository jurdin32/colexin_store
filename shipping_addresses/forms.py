from django.forms import ModelForm
from.models import ShippingAddress

class ShippingAddressForm(ModelForm):
    class Meta:
        model = ShippingAddress
        fields = [
            'line1','line2','ciudad','estado','pais','codigo_postal','referencia'
        ]

        labels = {
            'line1': 'Calle 1',
            'line2': 'Calle 2',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['line1'].widget.attrs.update({
            'class': 'form-control'
        })  #Dic

        self.fields['line2'].widget.attrs.update({
            'class': 'form-control'
        })  # Dic

        self.fields['ciudad'].widget.attrs.update({
            'class': 'form-control'
        })  # Dic

        self.fields['estado'].widget.attrs.update({
            'class': 'form-control'
        })  # Dic

        self.fields['pais'].widget.attrs.update({
            'class': 'form-control'
        })  # Dic

        self.fields['codigo_postal'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': '0000'
        })  # Dic

        self.fields['referencia'].widget.attrs.update({
            'class': 'form-control'
        })  # Dic



