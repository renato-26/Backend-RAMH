from djnago import forms
from .models import dispositivos 

class DispositivosForm(forms.ModelsForm):
    class Meta:
        model = dispositivos
        fields = '__all__'

        def clean_nombre(self):
            nombre = self.cleaned_data.get('nombre')

            if len(nombre)< 3:
                raise fomrs.ValidationError('El nombre debe tener al menos 3 caractares')

            return nombre