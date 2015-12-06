from django import forms

# Selectores de genero
GENERO_CHOICES = (
    ('masculino', 'Masculino',),
    ('femenino', 'Femenino',),
)

#FORMATS = ['%Y-%m-%d',      # '2006-10-25'
#           '%m/%d/%Y',      # '10/25/2006'
#           '%m/%d/%y']      # '10/25/06'

FORMATS = ['%d/%m/%Y']
# Formulario de Paciente
class FormularioPaciente(forms.Form):
    numero = forms.IntegerField(required=True)
    nombre = forms.CharField(label='nombre del paciente',
                             max_length=25,
                             required=True)
    apellido_paterno = forms.CharField(label='apellido paterno del paciente',
                                       max_length=25,
                                       required=True)
    apellido_materno = forms.CharField(label='apellido materno del paciente',
                                       max_length=25,
                                       required=True)
    curp = forms.CharField(label='curp del paciente',
                           max_length=25,
                           required=True)
    fecha_nacimiento = forms.DateField(required=True,
                                       input_formats=FORMATS,
                                       widget=forms.DateInput(format = FORMATS),)
    fecha_ingreso = forms.DateField(required=True,
                                    input_formats=FORMATS,
                                    widget=forms.DateInput(format = FORMATS),)
    edad = forms.IntegerField(required=True)
    sexo = forms.ChoiceField(required=True,
                             widget=forms.RadioSelect, 
                             choices=GENERO_CHOICES)
    direccion = forms.CharField(label='direccion',
                                max_length=40,
                                required=True,)
    peso = forms.DecimalField(label='Kg',
                              required=True,
                              max_digits=5,
                              decimal_places=2,)
    estatura = forms.DecimalField(label='Mts',
                                  required=True,
                                  max_digits=5,
                                  decimal_places=2,)
    diagnostico = forms.CharField(label='diagnostico',
                                  max_length=100,
                                  required=True,)

# Formulario Actualizar Paciente
class ActualizarPaciente(forms.Form):
    mejorias = forms.CharField(label='Mejorias',
                               max_length=50,
                               required=False,)
    diagnostico = forms.CharField(label='Diagnostico',
                                  max_length=100,
                                  required=False,)
    enfermedad = forms.CharField(label='Enfermedad',
                                 max_length=30,
                                 required=False,)
    tratamiento = forms.CharField(label='Tratamiento',
                                  max_length=40,
                                  required=False,)
    direccion = forms.CharField(label='direccion',
                                max_length=40,
                                required=False)
    peso = forms.DecimalField(label='Kg',
                              required=False,
                              max_digits=5,
                              decimal_places=2,)
    estatura = forms.DecimalField(label='Mts',
                                  required=False,
                                  max_digits=5,
                                  decimal_places=2,)

# Formulario buscar paciente
class BuscarMatricula(forms.Form):
    matricula = forms.IntegerField(required=True)

# Selectores de opciones del menu reportes generales
OPCIONES_CHOICES = (
    ('1','Tercera Edad',),
    ('2','Sexo',),
    ('3','Adultos',),
    ('4','Ninos',),
)

# Formulario Menu Reportes:
class MenuReportesGenerales(forms.Form):
    opcion = forms.ChoiceField(required=True,
                               widget=forms.RadioSelect, 
                               choices=OPCIONES_CHOICES,)

