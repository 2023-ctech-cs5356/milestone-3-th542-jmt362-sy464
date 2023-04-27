from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .forms import ItemForm

# Create your views here.
def new_post(request):
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('/')
    else:
        form = ItemForm()
        context = {
            'form': form
        }
    return render(request, 'post.html', context)
    # context = {}
    # form = ItemForm(request.POST or None, request.FILES or None)

    # if form.is_valid():
    #     form.save()

    # context['form'] = form
    # return render(request,"post.html",context)