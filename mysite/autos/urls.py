from django.urls import path
from . import views

app_name = 'autos'
urlpatterns = [
    path('', views.IndexView.as_view(), name='auto_list'),
    path('create/', views.AutoCreate.as_view(), name='auto_create'),
    path('<int:pk>/update/', views.AutoUpdate.as_view(), name='auto_update'),
    path('<int:pk>/delete/', views.AutoDelete.as_view(), name='auto_delete'),

    path('make/', views.MakeView.as_view(), name='make_list'),
    path('make/create/', views.MakeCreate.as_view(), name='make_create'),
    path('make/<int:pk>/update/', views.MakeUpdate.as_view(), name='make_update'),
    path('make/<int:pk>/delete/', views.MakeDelete.as_view(), name='make_delete')
]
