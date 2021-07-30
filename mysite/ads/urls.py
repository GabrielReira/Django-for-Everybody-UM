from django.urls import path, reverse_lazy
from . import views

app_name='ads'
urlpatterns = [
    path('', views.IndexView.as_view(), name='ad_list'),
    path('ad/<int:pk>', views.AdDetailView.as_view(), name='ad_detail'),
    path('ad/create', views.AdCreateView.as_view(success_url=reverse_lazy('ads:ad_list')), name='ad_create'),
    path('ad/<int:pk>/update', views.AdUpdateView.as_view(success_url=reverse_lazy('ads:ad_list')), name='ad_update'),
    path('ad/<int:pk>/delete', views.AdDeleteView.as_view(success_url=reverse_lazy('ads:ad_list')), name='ad_delete'),
]
