from django.utils import timezone
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .forms import DenunciaForm
from .models import Denuncia



def denuncia_list(request):
    denuncias = Denuncia.objects.order_by('published_date')
    return render(request, 'denuncia/denuncia_list.html', {'denuncias': denuncias})

def denuncia_detail(request, pk):
    denuncia = get_object_or_404(Denuncia, pk=pk)
    return render(request, 'denuncia/denuncia_detail.html', {'denuncia': denuncia})

def denuncia_new(request):
    if request.method == "POST":
        form = DenunciaForm(request.POST)
        if form.is_valid():
            denuncia = form.save(commit=False)
            denuncia.cedula = form.cleaned_data['cedula']
            denuncia.nombreApellido = form.cleaned_data['nombreApellido']
            denuncia.denunciaTexto = form.cleaned_data['denunciaTexto']
            denuncia.published_date = timezone.now()
            denuncia.save()
            return redirect('denuncia_detail', denuncia.id)
    else:
        print("denuncia nuevo else")
        form = DenunciaForm()
    return render(request, 'denuncia/denuncia_edit.html', {'form': form})

def denuncia_edit(request, pk):
    denuncia = get_object_or_404(Denuncia, pk=pk)
    if request.method == "POST":
        form = DenunciaForm(request.POST, instance=denuncia)
        if form.is_valid():
            denuncia = form.save(commit=False)
            denuncia.cedula = request.cedula
            denuncia.nombreApellido = request.nombreApellido
            denuncia.denunciaTexto = request.denunciaTexto
            denuncia.published_date = timezone.now()
            denuncia.save()
            return redirect('denuncia_detail', pk=denuncia.pk)
    else:
        form = DenunciaForm(instance=denuncia)
    return render(request, 'denuncia/denuncia_edit.html', {'form': form})
