from django.shortcuts import render, redirect
from .forms import UserForm,ProfileUpdate,UpdateForm

from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from django.views.generic import UpdateView
# Create your views here.
import requests




def home(request):
    
    return render(request,'blog/home.html')


def register(request):
    form = UserForm()
    if request.method == 'POST':
         form = UserForm(request.POST)

         if form.is_valid():
             username = form.cleaned_data.get('username')
             messages.success(request, f'{username} successfully created you can now login')
             form.save()
             return redirect('login')
    else:
        context = {'form':form}
        return render(request,'Register/register.html',context)


# I commented this view because i decided to use class based one
# def loginpage(request):
#     if request.method == 'POST':
      
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         user =  authenticate(request,username=username,password=password)

#         if user is not None:
#             login(request,user)
#             redirect('blog-home')
#         else:
#                 messages.error(request,'Username OR password is incorrect')

           
     
#     context = {}
#     return render(request,'Register/login.html',context)

def logoutpage(request):   
    logout(request)
    return redirect('login')

@login_required
def profile(request):
    if request.method == "POST":
        update_form = UpdateForm(request.POST,instance=request.user)
        profile_form = ProfileUpdate(request.POST,request.FILES,instance=request.user.profile)

        if update_form.is_valid() and profile_form.is_valid():
            update_form.save()
            profile_form.save()
            messages.success(request,f'Account successfully updated')
            return redirect('profile')
    else:
        update_form = UpdateForm(instance=request.user)
        profile_form = ProfileUpdate(instance=request.user.profile)
    context = {
        'update_form': update_form,
        'profile_form': profile_form
    }
    return render(request,'Register/profile.html',context)







# Api data disply
def api(request):
    response = requests.get('https://api.covidtracking.com/v1/states/daily.json').json()
    return render(request,'Register/api.html',{'response':response})
