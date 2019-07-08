from django.urls import path
from .views import CustomerView, FamilyView, UpdateCustomerView




urlpatterns = [
        path('customer/add/', CustomerView.as_view(), name='author-add'),
        path('customer/update/(?P<pk>\d+)', UpdateCustomerView.as_view(), name='author-add'),
        path('family/add/', FamilyView.as_view(), name='author-add'),
    

]