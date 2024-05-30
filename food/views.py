from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Item
from .forms import ItemForm
from django.template import loader
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView

# Create your views here.

def index(request):
  item_list = Item.objects.all()
  context = {
    'item_list': item_list,
  }
  return render(request, 'food/index.html', context)


def item(request):
  return HttpResponse('<h1>This is an item view</h1>')


def detail(request, item_id):
  item = Item.objects.get(pk=item_id)
  context = {
    'item': item,
  }
  return render(request, 'food/detail.html', context)

class FoodDetail(DetailView):
  model = Item
  template_name = 'food/detail.html'
  context_object_name = 'item'


def create_item(request):
  form = ItemForm(request.POST or None)

  if form.is_valid():
    form.save()
    return redirect('food:index')

  context = {
    'form': form,
  }
  return render(request, 'food/item-form.html', context)

# this is class based view for create item
class CreateItem(CreateView):
  model = Item
  fields = ['item_name', 'item_desc', 'item_price', 'item_image']
  template_name = 'food/item-form.html'
  context_object_name = 'item'

  def form_valid(self, form):
    form.instance.user_name = self.request.user
    return super().form_valid(form)
  


def update_item(request, id):
  item = Item.objects.get(id=id)
  form = ItemForm(request.POST or None, instance=item)

  if form.is_valid():
    form.save()
    return redirect('food:index')

  context = {
    'form': form,
    'item': item,
  }
  return render(request, 'food/item-form.html', context)


def delete_item(request, id):
  item = Item.objects.get(id=id)
  
  if request.method == 'POST':
    item.delete()
    return redirect('food:index')

  context = {
    'item': item,
  }
  return render(request, 'food/item-delete.html', context)