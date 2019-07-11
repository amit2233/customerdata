from django.urls import path
from .views import CustomerView, FamilyView  




urlpatterns = [
        path('customer/add/', CustomerView.as_view(), name='cust-add'),
        path('customer/update/<int:pk>/', CustomerView.as_view(), name='cust-update'),
        path('customer/delete/<int:pk>/', CustomerView.as_view(), name='cust-delete'),
        path('family/add/', FamilyView.as_view(), name='author-add'),
        path('family/update/<int:pk>/', FamilyView.as_view(), name='family-update'),
        path('family/delete/<int:pk>/', FamilyView.as_view(), name='family-delete'),
    

]