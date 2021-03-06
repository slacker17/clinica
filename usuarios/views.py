#-*- coding:utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from usuarios.forms import *
from usuarios.models import Paciente as pac
# PDF

import os
from io import BytesIO
from reportlab.pdfgen import canvas
from django.http import HttpResponse
# pacientes
from django.http import HttpResponse
from django.views.generic import ListView
from reportlab.platypus import SimpleDocTemplate, Paragraph, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import Table
from reportlab.platypus import Image

from reportlab.platypus import (BaseDocTemplate, Frame, Paragraph, 
                    NextPageTemplate, PageBreak, PageTemplate)
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import A4

def expediente(request, pacienteid):
    paciente = pac.objects.get(id=int(pacienteid))
    nombre = paciente.nombre
    apellido_materno = paciente.apellido_materno
    apellido_paterno = paciente.apellido_paterno
    curp = paciente.curp
    fecha_nacimiento = paciente.fecha_nacimiento
    fecha_ingreso = paciente.fecha_ingreso
    edad = paciente.edad
    sexo = paciente.sexo.capitalize()
    direccion = paciente.direccion
    peso = paciente.peso
    estatura = paciente.estatura
    diagnostico = paciente.diagnostico
    mejorias = paciente.mejorias
    enfermedad = paciente.enfermedad
    tratamiento = paciente.tratamiento
    buffer = BytesIO()

    response = HttpResponse(content_type='application/pdf')
    p = canvas.Canvas(buffer)
    titulo = "EXPEDIENTE CLINICO"
    #MARGENES
    p.line(15,825,575,825) #top
    p.line(15,17,575,15) #bottom
    p.line(15,17,15,825) #left
    p.line(575,825,575,14) #right

    p.drawImage("/etc/vale/Pictures/m_logot.jpg", 45, 770, width=45, height=45)
    p.setFont("Times-Bold",17)
#    p.setColor("red")
    p.drawString(200,800,titulo)
    # DDATOS LATERAL IZQUIERDA
    p.setFont("Times-Bold",12)
    p.drawString(60, 730, "NOMBRE:   "+nombre)
    p.line(118,728,250,728)
    p.drawString(60, 710, "APELLIDO PATERNO:  "+apellido_paterno)
    p.line(190,708,360,708)
    p.drawString(60, 690, "APELLIDO MATERNO:  "+apellido_materno)
    p.line(190,688,360,688)
    p.drawString(60, 670, "FECHA DE NACIMIENTO: "+str(fecha_nacimiento))
    p.line(200,668,360,668)
    p.drawString(60, 650, "EDAD: "+str(edad)+" anios")
    p.line(100,648,150,648)
    p.drawString(60, 630, "SEXO: "+sexo)
    p.line(100,628,160,628)
    p.drawString(60, 610, "DIRECCION: "+direccion)
    p.line(130,608,360,608)
    p.drawString(60, 590, "ENFERMEDAD: "+enfermedad)
    p.line(145,588,360,588)
    p.drawString(60, 480, "DIAGNOSTICO: ")
    p.drawString(60, 450, diagnostico)
    p.line(60,448,540,448)
    p.drawString(60, 410, "TRATAMIENTO: ")
    p.drawString(60, 390, tratamiento)
    p.line(60,388,540,388)
    p.drawString(60, 340, "MEJORIAS: ")
    p.drawString(60, 320, tratamiento)
    p.line(60,318,540,318)

    # DATOS LATERAL DERECHA
    p.setFont("Times-Bold",10)
    p.drawString(400, 760, "Exp No: "+str(paciente.id))
    p.setFont("Times-Bold",12)
    p.drawString(400, 730, "CURP: ")
    p.drawString(400, 710, curp)
    p.line(400, 705, 540, 705)

    p.drawString(400, 670, "FECHA DE INGRESO: ")
    p.drawString(410, 650, str(fecha_ingreso))
    p.line(400, 648, 540, 648)

    p.drawString(400, 620, "PESO: ")
    p.drawString(410, 600, str(peso)+" Kg.")
    p.line(400, 598, 540, 598)

    p.drawString(400, 580, "ESTATURA: ")
    p.drawString(410, 560, str(estatura)+" Mts.")
    p.line(400, 558, 540, 558)


    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()
    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)
    return response

def pacientes_pdf(request, opcion):
    pdf_name = titulo = "" 
    allpacientes = []
    if opcion == '1':
        pdf_name="pacientes_tercera_edad.pdf"
        allpacientes = [(p.id, p.nombre, p.apellido_paterno, p.apellido_materno, p.edad, p.enfermedad, p.tratamiento) 
                        for p in pac.objects.filter(edad__range=[60,120])]
        titulo = "Listado de Pacientes de la Tercera Edad"
    if opcion == '2':
        pdf_name="pacientes_ninos.pdf"
        allpacientes = [(p.id, p.nombre, p.apellido_paterno, p.apellido_materno, p.edad, p.enfermedad, p.tratamiento) 
                        for p in pac.objects.filter(edad__range=[0,17])]
        titulo = "Listado de Pacientes Ninos"
    if opcion == '3':
        pdf_name="pacientes_adultos.pdf"
        allpacientes = [(p.id, p.nombre, p.apellido_paterno, p.apellido_materno, p.edad, p.enfermedad, p.tratamiento) 
                        for p in pac.objects.filter(edad__range=[18,59])]
        titulo = "Listado de Pacientes Adultos"
    if opcion == '4':
        pdf_name="pacientes_hombres.pdf"
        allpacientes = [(p.id, p.nombre, p.apellido_paterno, p.apellido_materno, p.edad, p.enfermedad, p.tratamiento) 
                        for p in pac.objects.filter(sexo='masculino')]
        titulo = "Listado de Pacientes Hombres"

    IMAGEN  = '/etc/vale/Pictures/m_logot.jpg'
    response = HttpResponse(content_type='application/pdf')
    # la linea 26 es por si deseas descargar el pdf a tu computadora
    # response['Content-Disposition'] = 'attachment; filename=%s' % pdf_name
    buff = BytesIO()
    doc = SimpleDocTemplate(buff,
                            pagesize=letter,
                            rightMargin=20,
                            leftMargin=20,
                            topMargin=10,
                            bottomMargin=10,
                        )
    pacientes = []
    styles = getSampleStyleSheet()
    #imagen_logo = Image(os.path.realpath(IMAGEN), width=50, height=50)
    #pacientes.append(imagen_logo)
    header = Paragraph(titulo, styles['title'])
    #pacientes.append(p)
    pacientes.append(header)
    headings = ('Matricula','Nombre', 'Apellido Paterno','Apellido Materno','Edad','Enfermedad','Tratamiento')
    
    t = Table([headings] + allpacientes)
    t.setStyle(TableStyle(
        [
            ('GRID', (0, 0), (7, -1), 1, colors.dodgerblue),
            ('LINEBELOW', (0, 0), (-1, 0), 2, colors.darkblue),
            ('BACKGROUND', (0, 0), (-1, 0), colors.dodgerblue)
        ]
    ))
    pacientes.append(t)
    doc.build(pacientes)
    response.write(buff.getvalue())
    buff.close()
    return response
    
def pdf(request):
    # Create the HttpResponse object with the appropriate PDF headers.
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="somefilename.pdf"'
    buffer = BytesIO()

    # Create the PDF object, using the response object as its "file."
    p = canvas.Canvas(buffer)

    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    p.drawString(100, 100, "Hello world.")

    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()
    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)
    return response


def registrarPaciente(request):
    if request.method == 'POST':
        form = FormularioPaciente(request.POST)
        if form.is_valid():
            datos = form.cleaned_data
            paciente = pac(datos['numero'],
			   datos['nombre'].capitalize(),
                           datos['apellido_paterno'].capitalize(),
                           datos['apellido_materno'].capitalize(),
                           datos['curp'].upper(),
                           datos['fecha_nacimiento'],
                           datos['fecha_ingreso'],
                           datos['edad'],
                           datos['sexo'],
                           datos['direccion'].capitalize(),
                           datos['peso'],
                           datos['estatura'],
                           datos['diagnostico'].capitalize(),
            )
            paciente.save()
            # form = EmployeeForm()  -> limpiar formulario
            return HttpResponseRedirect(reverse('gracias'))
    else:
        form = FormularioPaciente()

    return render(request,'registro.html',{'form':form})


def actualizarPaciente(request, numero_paciente):
    paciente = pac.objects.get(id=numero_paciente)
    if request.method == 'POST':
        form = ActualizarPaciente(request.POST)
        if form.is_valid():
            datos = form.cleaned_data
            if datos['mejorias']:
                paciente.mejorias=datos['mejorias']
            if datos['diagnostico']:
                paciente.diagnostico=datos['diagnostico']
            if datos['enfermedad']:
                paciente.enfermedad=datos['enfermedad']
            if datos['tratamiento']:
                paciente.tratamiento=datos['tratamiento']
            if datos['peso']:
                paciente.peso=datos['peso']
            if datos['estatura']:
                paciente.estatura=datos['estatura']
            paciente.save()
            return HttpResponseRedirect(reverse('paciente_actualizado'))
    else:
        form = ActualizarPaciente()
    return render(request,'actualizar.html',{'form':form, 'paciente':paciente.nombre})


# metodo que busca si existe el paciente y procede a ejecutar una accion
def buscar_paciente(request):
    if request.method == 'POST':
        form = BuscarMatricula(request.POST)
        if form.is_valid():
            datos = form.cleaned_data
            try:
                paci = pac.objects.get(id=datos['matricula'])
                return HttpResponseRedirect(reverse('actualizar',args=[paci.id]))
            except pac.DoesNotExist:                 
                return HttpResponseRedirect(reverse('error'))
    else:
        form = BuscarMatricula()
    return render(request,'buscar_paciente.html',{'form':form})
                
        
# metodos auxiliares
def gracias(request):
    return render(request,'gracias.html')


def error(request):
    return render(request,'error.html')

def actualizado(request):
    return render(request,'gracias.html')
