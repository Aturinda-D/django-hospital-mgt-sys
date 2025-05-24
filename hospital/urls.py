from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import home, login_view, patients, appointments, add_patient, add_appointment, update_patient, update_appointment, delete_patient, delete_appointment

urlpatterns = [
    path('', home, name='home'),
    path('login/', login_view, name='login'),
    path('accounts/logout/', LogoutView.as_view(), name='logout'),
    path('patients/', patients, name='patients'),
    path('add_patient/', add_patient, name='add_patient'),
    path('update_patient/', update_patient, name='update_patient'),
    path('delete_patient/', delete_patient, name='delete_patient'),
    path('appointments/', appointments, name='appointments'),
    path('add_appointment/', add_appointment, name='add_appointment'),
    path('update_appointment/', update_appointment, name='update_appointment'),
    path('delete_appointment/', delete_appointment, name='delete_appointment'),
]