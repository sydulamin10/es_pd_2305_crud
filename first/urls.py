from django.urls import path
from .views import first_func, delete_data, update_data

urlpatterns = [
    path('', first_func, name='first_func'),
    path('delete_data/<int:id>/', delete_data, name='delete_data'),
    path('update_data/<int:id>/', update_data, name='update_data'),
]
