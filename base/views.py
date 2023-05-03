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

def update_post(request, post_id):
    post = Item.objects.get(pk = post_id)
    form = ItemForm(request.POST or request.FILES or None, instance = post)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'editpost.html', {'post': post, 'form': form})


class MyPosts(generic.ListView):
    template_name = 'home.html'

    def get_queryset(self):
        return Item.objects.filter(author = self.request.user).order_by('-created')

class AllPosts(generic.ListView):
    queryset = Item.objects.order_by('-created')
    template_name = 'allposts.html'

class AppliancesPosts(generic.ListView):
    queryset = Item.objects.filter(category = 'Appliances').order_by('-created')
    template_name = 'allposts.html'

class ClothesPosts(generic.ListView):
    queryset = Item.objects.filter(category = 'Clothes').order_by('-created')
    template_name = 'allposts.html'

class EducationPosts(generic.ListView):
    queryset = Item.objects.filter(category = 'Education').order_by('-created')
    template_name = 'allposts.html'

class ElectronicsPosts(generic.ListView):
    queryset = Item.objects.filter(category = 'Electronics').order_by('-created')
    template_name = 'allposts.html'

class FreePosts(generic.ListView):
    queryset = Item.objects.filter(category = 'Free').order_by('-created')
    template_name = 'allposts.html'

class HomeAndGardenPosts(generic.ListView):
    queryset = Item.objects.filter(category = 'Home & Garden').order_by('-created')
    template_name = 'allposts.html'

class MiscellaneousPosts(generic.ListView):
    queryset = Item.objects.filter(category = 'Miscellaneous').order_by('-created')
    template_name = 'allposts.html'

class MusicPosts(generic.ListView):
    queryset = Item.objects.filter(category = 'Music').order_by('-created')
    template_name = 'allposts.html'

class SportsPosts(generic.ListView):
    queryset = Item.objects.filter(category = 'Sports').order_by('-created')
    template_name = 'allposts.html'

class VehiclesPosts(generic.ListView):
    queryset = Item.objects.filter(category = 'Vehicles').order_by('-created')
    template_name = 'allposts.html'