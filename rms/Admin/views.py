from django.shortcuts import render,redirect
from .forms import Register
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from .forms import StudentForm
from .forms import ItemForm
from .models import Students
from .models import Items
from .models import Items_Paid
from django import forms
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required, permission_required
# Create your views here.

@login_required(login_url="accounts/login")
def index(request):
    items = Items_Paid.objects.all()

    return render(request, 'index.html', {'items':items})

@login_required(login_url="accounts/login")
def add_student(request):

    form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            
            
            return redirect('/index')
    else:
        context = {'form':form}


        return render(request, 'student/add_student.html',context)


@login_required(login_url="accounts/login")
def all_student(request):
    students = Students.objects.all()
    print('hiii')
    print(students)

    return render(request, 'student/all_student.html', {'students':students})

@login_required(login_url="accounts/login")
def add_item(request):

    form = ItemForm()
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            
            
            return redirect('/all_item')
    else:
        context = {'form':form}


        return render(request, 'item/add_item.html',context)

@login_required(login_url="accounts/login")
def all_item(request):
    items = Items.objects.all()
    print('hiii')
    print(items)

    return render(request, 'item/all_item.html', {'items':items})


@login_required(login_url="accounts/login")
def payment_item(request, item):
    students = Students.objects.all()
    item_paid = Items_Paid.objects.filter(item_id=item)
    items = Items.objects.filter(id=item).first()
    item_id  = request.POST.get("item_id")
    student_id  = request.POST.get("student_id")
    if request.method == 'POST':
        if Items_Paid.objects.filter(item_id=item, student_id=student_id):
            return HttpResponse('already paid')
        if request.POST.get("paid"):
            item_price = int(request.POST.get("price"))
            account_balance = int(Students.objects.filter(id=student_id).values('account_balance')[0]['account_balance'])
            if not account_balance < item_price :
                
                Items_Paid.objects.create(item_id=item_id,student_id=student_id)

                amount_remain = account_balance - item_price
                studAcc = Students.objects.filter(id=student_id)
                studAcc.update(account_balance=amount_remain)
            else:
                return HttpResponse("Acoount balance is low")
                # raise forms.ValidationError(('your account balance is low'), params={'count': "hello"},)
            # print(amount_remain)
            # print(account_balance)
            # print('kilk')
                # return redirect('/payment_item/'+item_id)
        else:
            return redirect('/index')
    # print('hiii')
    # print(items)

    return render(request, 'item/payment_item.html', {'items':items,'students':students, 'paid':item_paid})


@login_required(login_url="accounts/login")
def student_item(request, studID):

    student_items = Items_Paid.objects.filter(student_id=studID)
    student = Students.objects.filter(id=studID).first()
    # items = Items.o
    
    return render(request, 'student/student_item.html', {'students':student,'student_items':student_items } )

def UserSignUp(request):
    form = Register()
    if request.method == 'POST':
        form = Register(request.POST)
        if form.is_valid():
            user = form.save(commit='false')
            login(request, user)
            
            return redirect('/index')
    
    else:
        # form = SignupForm()
    # return render(request, 'signup.html', {'form': form})
        context = {"form":form}
    return render(request, 'registration/register.html',context)


def logoutUser(request):
    logout(request)
    return redirect('login')
