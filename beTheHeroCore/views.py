from django.shortcuts import redirect, render
from beTheHeroCore.models import Account, Case
from beTheHeroCore.forms import RegistrationForm, CaseForm
from django.contrib.auth import authenticate, login, logout

def home(request):
    if not request.user.is_authenticated:
        return redirect('loginAccount')
    cases = Case.objects.filter(relatedAccount = request.user)

    return render(request, 'incidents.html', {'cases':cases})

def caseDetail(request, pk):
    case = Case.objects.get(pk=pk)
    return render(request, 'caseDetail.html', {'case':case})

def editCase(request, pk):
    case = Case.objects.get(pk=pk)

    if request.POST:
        form = CaseForm(request.POST, instance=case)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:

        form = CaseForm(instance=case)

        return render(request, 'register.html', {'form':form})

def registerCase(request):
    if request.POST:
        form = CaseForm(request.POST)
        if form.is_valid():
            case = form.save(commit=False)
            case.relatedAccount = request.user
            case.save()
            request.user.cases.add(case)
            return redirect('home')
    else:
        form = CaseForm()
        return render(request, 'register.html', {'form':form})


def deleteCase(request, pk):
    case = Case.objects.filter(pk=pk).delete()
    return redirect('home')


def registerAccount(request):
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')
            user = authenticate(email=email, password=password)
            
            user.save()
            login(request, user)
            return redirect('home')
        else:
            return redirect('registerAccount')
        
    else:
        form = RegistrationForm()
        return render(request, 'register.html', {'form':form})

def loginAccount(request):
    if request.POST:
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(email=email, password=password)

        if user:
            login(request, user)
            return redirect('home')
        else:
            return redirect('loginAccount')
    else:
        return render(request, 'login.html')

def logoutAccount(request):
    logout(request)
    return redirect('home')