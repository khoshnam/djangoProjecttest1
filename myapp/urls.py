from django.urls import path

from myapp.views import ContractsCreateView,PremiumCollectionCreateView

urlpatterns = [
    path('',ContractsCreateView.as_view(),name='index'),
path('c/',PremiumCollectionCreateView.as_view(),name='index2'),
]