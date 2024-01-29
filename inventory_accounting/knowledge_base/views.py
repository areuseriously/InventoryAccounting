from django.shortcuts import render, redirect, get_object_or_404
from django.http import FileResponse
from .models import File
import os
from .forms import FileForm


def file_list(request):
    files = File.objects.all()
    return render(request, 'file_list.html', {'files': files})


def file_download(request, file_id):
    file = get_object_or_404(File, pk=file_id)
    response = FileResponse(open(file.file.path, 'rb'))
    response['Content-Disposition'] = 'attachment; filename="{}"'.format(file.file.name.split('/')[-1])
    return response


def file_delete(request, file_id):
    file = get_object_or_404(File, pk=file_id)
    os.remove(file.file.path)
    file.delete()
    return redirect('file_list')


def file_create(request):
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('file_list')
    else:
        form = FileForm()
    return render(request, 'file_create.html', {'form': form})
