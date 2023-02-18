from django.shortcuts import render
from .models import AccessRecord, Topic, User, Webpage
from .forms import RegistrationForm

# Create your views here.
def index(request):
    return render(request, 'appTwo/index.html')

def records(request):
    access_records = AccessRecord.objects.order_by('date')
    record_dict = { 'records': access_records }
    return render(request, 'appTwo/records.html', context=record_dict)

def users(request):
    users_list = User.objects.order_by('first_name')
    users_dict = { 'users': users_list }
    return render(request, 'appTwo/users.html', context=users_dict)

def register(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print('Error Form is invalid')
    return render(request, 'appTwo/register.html', { 'form': form })