from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name='home'),

    path('add/',
         views.add_fee,
         name='add_fee'),

    path('view/',
         views.view_fee,
         name='view_fee'),

    path('edit/<int:id>/',
         views.edit_fee,
         name='edit_fee'),

    path('delete/<int:id>/',
         views.delete_fee,
         name='delete_fee'),
    path(
    'admin-dashboard/',
    views.admin_dashboard,
    name='admin_dashboard'
        ),

    path('search/',
         views.search_fee,
         name='search_fee'),
]
