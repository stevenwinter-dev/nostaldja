from django.shortcuts import redirect, render

# Create your views here.
from .models import Decade, Fad
from .forms import FadForm, DecadeForm

def index(request):
    return render(request, 'nostaldja/index.html')

def decade_list(request):
    decades = Decade.objects.all()
    decades = decades.order_by('start_year')
    print(decades)
    return render(
        request, 
        'nostaldja/decade_list.html', 
        {'decades':decades}
    )

def fad_list(request):
    fads = Fad.objects.all()
    fads = fads.order_by('name')
    return render(
        request, 
        'nostaldja/fad_list.html', 
        {'fads':fads}
    )

def fad_detail(request, pk):
    try:
        fad = Fad.objects.get(id=pk)
    except:
        fad = {'name': "No fad found"}
        print(f"fad with id={pk} didn't work")
    fad = Fad.objects.get(id=pk)
    return render(request, 'nostaldja/fad_detail.html', {'fad': fad})

def decade_detail(request, pk):
    # try:
    #     decade = Decade.objects.get(id=pk)
    # except:
    #     decade = {'start_year': "No decade found"}
    #     print(f"decade with id={pk} didn't work")
    decade = Decade.objects.get(id=pk)
    fads = Fad.objects.filter(decade_id=pk)
    return render(request, 'nostaldja/decade_detail.html', {'decade': decade, 'fads': fads})

def fad_create(request):
    if request.method == "POST":
        form = FadForm(request.POST)
        if form.is_valid():
            fad = form.save()
            return redirect('fad_detail', pk=fad.pk)
    else:
        form = FadForm()
    return render(request, 'nostaldja/fad_form.html', {'form': form})

def decade_create(request):
    if request.method == "POST":
        form = DecadeForm(request.POST)
        if form.is_valid():
            decade = form.save()
            return redirect('decade_detail', pk=decade.pk)
    else:
        form = DecadeForm()
    return render(request, 'nostaldja/decade_form.html', {'form': form})

def fad_edit(request, pk):
    fad = Fad.objects.get(pk=pk)
    if request.method == "POST":
        form = FadForm(request.POST, instance=fad)
        if form.is_valid():
            fad = form.save()
            return redirect('fad_detail', pk=fad.pk)
    else:
        form = FadForm(instance=fad)
    return render(request, 'nostaldja/fad_form.html', {'form':form})

def decade_edit(request, pk):
    decade = Decade.objects.get(pk=pk)
    if request.method == "POST":
        form = DecadeForm(request.POST, instance=decade)
        if form.is_valid():
            decade = form.save()
            return redirect('decade_detail', pk=decade.pk)
    else:
        form = DecadeForm(instance=decade)
    return render(request, 'nostaldja/decade_form.html', {'form':form})

def decade_delete(request, pk):
    Decade.objects.get(id=pk).delete()
    return redirect('decade_list')

def fad_delete(request, pk):
    Fad.objects.get(id=pk).delete()
    return redirect('fad_list')