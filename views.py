
# views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import TextFile
from .forms import TextFileForm

def text_file_list(request):
    files = TextFile.objects.all()
    return render(request, '/users/computer/project/django/notepad/templates/file_list.html', {'files': files})

def create_text_file(request):
    if request.method == 'POST':
        form = TextFileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('file_list')
    else:
        form = TextFileForm()
    return render(request, '/users/computer/project/django/notepad/templates/file_form.html', {'form': form})

def edit_text_file(request, pk):
    file = get_object_or_404(TextFile, pk=pk)
    if request.method == 'POST':
        form = TextFileForm(request.POST, instance=file)
        if form.is_valid():
            form.save()
            return redirect('file_list')
    else:
        form = TextFileForm(instance=file)
    return render(request, '/users/computer/project/django/notepad/templates/file_form.html', {'form': form})

#    return render(request, '/users/computer/project/django/notepad/templates/file_form.html', {'form': form})

def view_text_file(request, pk):
    file = get_object_or_404(TextFile, pk=pk)
    return render(request, '/users/computer/project/django/notepad/templates/file_form.html', {'form': form})
