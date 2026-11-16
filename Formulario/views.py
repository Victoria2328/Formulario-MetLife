import csv
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Formulario
from .forms import FormularioForm

def crear_formulario(request):
    if request.method == 'POST':
        form = FormularioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('crear_formulario') # Recarga la página limpia tras guardar
    else:
        form = FormularioForm()
    
    return render(request, 'formulario.html', {'form': form})

def descargar_excel(request):
    response = HttpResponse(content_type='text/csv; charset=utf-8')
    response['Content-Disposition'] = 'attachment; filename="datos_formulario.csv"'
    response.write('\ufeff'.encode('utf8'))

    writer = csv.writer(response, delimiter=';')
    fields = [field.name for field in Formulario._meta.fields]
    writer.writerow(fields)

    for reg in Formulario.objects.all():
        fila = [getattr(reg, field) for field in fields]
        writer.writerow(fila)

    return response