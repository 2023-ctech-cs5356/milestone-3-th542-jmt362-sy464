from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.views import generic
from .forms import ItemForm
from .models import Item

# Create your views here.
def new_post(request):
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            tempForm = form.save(commit = False)
            tempForm.author = request.user
            tempForm.save()
    
            return redirect('/')
    else:
        form = ItemForm()
        context = {
            'form': form
        }
    return render(request, 'post.html', context)

class MyPosts(generic.ListView):
    template_name = 'home.html'

    def get_queryset(self):
        return Item.objects.filter(author = self.request.user).order_by('-created')

class AllPosts(generic.ListView):
    queryset = Item.objects.order_by('-created')
    template_name = 'allposts.html'