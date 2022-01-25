from django.shortcuts import render,redirect
from django.contrib import messages
from blog import views
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm,userupdateform,profileupdateform
from .models import Profile


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'Account created for {username}!')
            return redirect('login')
    else:
        form = UserRegisterForm()

    return render(request,'register.html',{'form':form})
@login_required
def myprofile(request):
    if request.method == 'POST':
        u_form = userupdateform(request.POST, instance=request.user)
        p_form = profileupdateform(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = userupdateform(instance=request.user)
        p_form = profileupdateform(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'profile.html', context)

def profile(request):
    oprofile = Profile.objects.all(id = id)

    context = {
        'profile': oprofile,
    }

    return render(request, 'profile.html', context)