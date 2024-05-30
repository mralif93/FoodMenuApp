from django.urls import path
from . import views

app_name = 'food'
urlpatterns = [
  # list item
  path('', views.index, name='index'),
  path('item/', views.item, name='item'),
  # detail item
  path('<int:pk>/', views.FoodDetail.as_view(), name='detail'),
  # add item
  path('add/', views.CreateItem.as_view(), name='create_item'),
  #  edit item
  path('update/<int:id>/', views.update_item, name='update_item'),
  #  delete item
  path('delete/<int:id>/', views.delete_item, name="delete_item"),
]