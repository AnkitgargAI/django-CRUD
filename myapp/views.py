from django.shortcuts import render, HttpResponseRedirect
from .forms import StudentRegistration
from .models import User
# Create your views here.

#  To add & show the user data


def add_show(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            nw = fm.cleaned_data["name"]
            ew = fm.cleaned_data["email"]
            pw = fm.cleaned_data["password"]
            reg = User(name=nw, email=ew, password=pw)
            reg.save()
            fm = StudentRegistration()
    else:
        fm = StudentRegistration()
    stud = User.objects.all()
    return render(request, 'myapp/addshow.html', {'form': fm, 'stu': stud})


# To delete the user data
def delete_user(request, id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        pi.delete()
    return HttpResponseRedirect("/")

# To update the data


# To delete the user data
def update_user(request, id):
    pi = User.objects.get(pk=id)
    if request.method == 'POST':
        fm = StudentRegistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
        return HttpResponseRedirect("/")
    else:
        fm = StudentRegistration(instance=pi)
    return render(request, 'myapp/updateStudent.html', {'form': fm, 'id': id})
