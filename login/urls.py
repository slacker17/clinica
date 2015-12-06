"""login URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

#PDF
#from django.conf.urls.defaults import *
from django.conf.urls import patterns
from wkhtmltopdf.views import PDFTemplateView

class MyPDF(PDFTemplateView):
    filename = 'my_pdf.pdf'
    template_name = 'tabla.html'
    cmd_options = {
        'margin-top': 3,
    }

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^registro/', 
        'usuarios.views.registrarPaciente', 
        name='registr'),
    url(r'^thanks/', 
        'usuarios.views.gracias', 
        name='gracias'),
    url(r'^error/', 
        'usuarios.views.error', 
        name='error'),
    url(r'^buscar/', 
        'usuarios.views.buscar_paciente',
        name='buscar'),
    url(r'^actualizar/(\d)$',
        'usuarios.views.actualizarPaciente',
        name='actualizar'),
    url(r'^actualizado/',
        'usuarios.views.actualizado', 
        name='paciente_actualizado'),
]

#pdfs 
urlpatterns += [    
    url(r'^pdf/', 'usuarios.views.pdf', name='pdf'),
    url(r'^pacientespdf/(\d)/', 'usuarios.views.pacientes_pdf', name='pac_pdf'),
    url(r'^expediente/([0-9]{1,})/', 'usuarios.views.expediente', name='expediente_pdf'),

]
