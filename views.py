from django.shortcuts import render, redirect  
from note.forms import noteForm  
from note.models import Note  
# Create your views here.  
def emp(request):  
    if request.method == "POST":  
        form = noteForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/show')  
            except:  
                pass  
    else:  
        form = noteForm()  
    return render(request,'index.html',{'form':form})  
def show(request):  
    note = Note.objects.all()  
    return render(request,"show.html",{'note':note})  
def edit(request, id):  
    note = Note.objects.get(id=id)  
    return render(request,'edit.html', {'note':note)  
def update(request, id):  
    note =Note.objects.get(id=id)  
    form = noteForm(request.POST, instance = note)  
    if form.is_valid():  
        form.save()  
        return redirect("/show")  
    return render(request, 'edit.html', {'note': note})  
def destroy(request, id):  
    note = Note.objects.get(id=id)  
    note.delete()  
    return redirect("/show")  
