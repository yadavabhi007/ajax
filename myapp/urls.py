from django.urls import path
from . import views

urlpatterns = [
    path('', views.add_data.as_view(), name='adddata'),
    path('show/', views.show_data.as_view(), name='showdata'),
    path('<int:id>/', views.update_data.as_view(), name='updatedata'),
    path('delete/<int:id>/', views.delete_data.as_view(), name='deletedata'),
]