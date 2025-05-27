from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import PatientForm, AppointmentForm
from .models import Patient, Appointment

# ----- HOME ----- #.
def home(request):
    return render(request, 'home.html')


# ----- LOGIN ----- #
def login_view(request):
    next_url = request.GET.get('next', 'home')

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect(next_url)
        else:
            messages.error(request, 'Invalid username or password!')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form' : form})




# ----- PATIENTS ----- #
def patients(request):
    patients = Patient.objects.all().order_by('id')
    return render(request, 'patients.html', {'patients' : patients})


@login_required
def add_patient(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Patient added successfully!')
        else:
            messages.error(request, 'Failed to add new patient to database')
    else:
        form = PatientForm()

    return render(request, 'add_patient.html', {'form' : form})


@login_required
def update_patient(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    if request.method == "POST":
        form = PatientForm(request.POST, instance=patient)
        if form.is_valid():
            form.save()
            messages.success(request, "Patient data updated successfully!")
            return redirect("patients")
        else:
            messages.error(request, "Failed to update patient data!")
    else:
        form = PatientForm(instance=patient)

    return render(request, 'update_patient.html', {'form': form})


@login_required
def delete_patient(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    if request.method == "POST":
        patient.delete()
        messages.success(request, "Patient deleted successfully!")
        return redirect("patients")
    return render(request, 'confirm_delete.html', {'object': patient, 'type': 'patient'})




# ----- APPOINTMENTS ----- #
def appointments(request):
    appointments = Appointment.objects.all()
    return render(request, 'appointments.html', {'appointments': appointments})


@login_required
def add_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Appointment added successfully!')
            # return redirect('appointments')
        else:
            messages.error(request, 'Failed to add new appointment.')
    else:
        form = AppointmentForm()
    return render(request, 'add_appointment.html', {'form' : form})


@login_required
def update_appointment(request):
    return render(request, 'update_appointment.html')


@login_required
def delete_appointment(request, pk):
    appointment = get_object_or_404(Appointment, pk=pk)
    if request.method == 'POST':
        appointment.delete()
        messages.success(request, 'Appointment deleted successfully!')
        return redirect('appointments')
    return render(request, 'confirm_delete.html', {'object': appointment, 'type': 'appointment'})