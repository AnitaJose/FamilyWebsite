from django.shortcuts import render,redirect
from .models import login,family,Addfamilyphotos,signup
from .forms import LoginForm,AddPhotoForm,SignupForm
# Create your views here.
global users
users=''
def login_page(request):
    global users
    users = ''
    if request.method=="POST":
        form=LoginForm(request.POST)
        login1=form.save(commit=False)
        #username=request.POST.get('Username')
        #password=request.POST.get('Password')
        users=login.objects.filter(Username=login1.Username, Password=login1.Password)

        if login.objects.filter(Username=login1.Username, Password=login1.Password):
            return render(request,'login/welcome.html',{'users':users})
        else:
            return redirect(login_page)

    else:
        form = LoginForm()
        return render(request,'login/login_page.html',{'form':form})

def guest(request):
    return render(request,'login/welcome.html',{})

def signup_page(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        #signup1 = form.save(commit=False)
        if form.is_valid():
            u = login(
                Username=form.cleaned_data['Username'],
                Password=form.cleaned_data['Password']
            )
            u.save()
            #login.objects.create(Username=form.cleaned_data['Username'], Password=form.cleaned_data['Password'])
            #u1 = login.objects.get(Username=form.cleaned_data['Username'])
            a = signup(
                FirstName=form.cleaned_data['FirstName'],
                LastName=form.cleaned_data['LastName'],
                DOB=form.cleaned_data['DateOfBirth'],
                EmailID=form.cleaned_data['EmailID'],
                PhoneNumber=form.cleaned_data['PhoneNumber'],
                Username=u
            )

            a.save()

            return redirect(login_page)
    else:
        form = SignupForm()
        return render(request,'login/signup.html',{'form':form})

def familyphotos(request):
    i1 = Addfamilyphotos.objects.all()
    return render(request,'login/familyphotos.html',{'i1':i1})

def Willy(request):
    global users
    family1 = family.objects.filter(FamilyHead='Philip K Joseph', Name='Philip K Joseph')
    family2 = family.objects.filter(FamilyHead='Philip K Joseph', Name='Kunjumol Joseph')
    family3 = family.objects.filter(FamilyHead='Philip K Joseph', Name='Joe Philip')
    family4 = family.objects.filter(FamilyHead='Philip K Joseph', Name='Jerry Philip')

    return render(request, 'login/jose.html',
                  {'family1': family1, 'family2': family2, 'family3': family3, 'family4': family4,'users':users})


def Jose(request):
    global users
    family1 = family.objects.filter(FamilyHead='Jose',Name='Jose K J')
    family2 = family.objects.filter(FamilyHead='Jose', Name='Kochumol Jose')
    family3 = family.objects.filter(FamilyHead='Jose', Name='Anita Jose')
    family4 = family.objects.filter(FamilyHead='Jose', Name='Jimmy Jose')

    return render(request,'login/jose.html',
                  {'family1':family1,'family2':family2,'family3':family3,'family4':family4,'users':users})

def Rony(request):
    global users
    family1 = family.objects.filter(FamilyHead='Rony K Joseph', Name='Rony K Joseph')
    family2 = family.objects.filter(FamilyHead='Rony K Joseph', Name='Jessy Rony')
    family3 = family.objects.filter(FamilyHead='Rony K Joseph', Name='Anu Rony')
    family4 = family.objects.filter(FamilyHead='Rony K Joseph', Name='Linu Rony')
    family4 = family.objects.filter(FamilyHead='Rony K Joseph', Name='Jeffry Rony')

    return render(request, 'login/jose.html',
                  {'family1': family1, 'family2': family2, 'family3': family3, 'family4': family4,'users':users})
def Jeny(request):
    global users
    family1 = family.objects.filter(FamilyHead='Jeny Joseph', Name='Joseph')
    family2 = family.objects.filter(FamilyHead='Jeny Joseph', Name='Jeny Joseph')
    family3 = family.objects.filter(FamilyHead='Jeny Joseph', Name='Boby Joseph')
    family4 = family.objects.filter(FamilyHead='Jeny Joseph', Name='Soby Rony')
    family4 = family.objects.filter(FamilyHead='Jeny Joseph', Name='Abraham')

    return render(request, 'login/jose.html',
                  {'family1': family1, 'family2': family2, 'family3': family3, 'family4': family4,'users':users})

def Elsamma(request):
    global users
    family1 = family.objects.filter(FamilyHead='Jeny Joseph', Name='Joseph')
    family2 = family.objects.filter(FamilyHead='Jeny Joseph', Name='Jeny Joseph')
    family3 = family.objects.filter(FamilyHead='Jeny Joseph', Name='Boby Joseph')
    family4 = family.objects.filter(FamilyHead='Jeny Joseph', Name='Soby Rony')
    family4 = family.objects.filter(FamilyHead='Jeny Joseph', Name='Abraham')

    return render(request, 'login/jose.html',
                  {'family1': family1, 'family2': family2, 'family3': family3, 'family4': family4,'users':users})

def addImage(request):
    if request.method=='POST':
        form=AddPhotoForm(request.POST,request.FILES)
        if form.is_valid():
            photo=form.save(commit=False)
            Addfamilyphotos.objects.create(Photo=photo.Photo)
            i1=Addfamilyphotos.objects.all()
            return render(request,'login/familyphotos.html',{'i1':i1})
        else:
            return redirect('addImage')
    else:
        form=AddPhotoForm()

        return render(request,'login/uploadphoto.html',{'form':form})

def back(request,pageno):
    global users
    if pageno==2:
        return render(request,'login/welcome.html',{'users':users})
    elif pageno==3:
        i1 = Addfamilyphotos.objects.all()
        return render(request, 'login/familyphotos.html', {'i1': i1})
    if pageno==0:
        return render(request, 'login/welcome.html',{})



