from django.urls import path
from .import views

urlpatterns = [
   path('product/', views.view_product, name='view_product'),
   path('raucu/', views.view_category, name='view_category'),
   path('traicay/', views.view_category1, name='view_category1'),
   path('nuocep/', views.view_category2, name='view_category2'),
   path('cacloaihat/', views.view_category3, name='view_category3'),
   path('detailproduct/<int:id>/', views.detailproduct,name='detailproduct'),
]
