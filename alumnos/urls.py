from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('crear', views.session, name='crear'),
    path('mostrar', views.mostrar, name='mostrar'),
    path('eliminar/<int:id>', views.eliminar, name='eliminar'),

]