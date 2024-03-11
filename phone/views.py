from typing import ItemsView
from django import template
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.template import loader
from .models import Items,ItemDetails,Carrt,Paynoww,Payno
from .forms import CreateUserForm
from .forms import LoginUserForm
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login, logout ,authenticate
from django.contrib.auth.decorators import login_required
from .forms import ProductForm

# Create your views here.
@login_required(login_url='/auth_login/')
def checkout(request):
      template=loader.get_template('checkout.html')
      current_user = request.user.id
      cart=Carrt.objects.all().filter(Id_user=current_user).first()
      product=Items.objects.get(itemdetails=cart.Id_product)
      context={
            'cart':cart,
            'productname':product,
             'request':request
            
       }
      return HttpResponse(template.render(context=context)) 



def index(request):
    template=loader.get_template('index.html')
    return HttpResponse(template.render())

def add_to_cart(requset,id):
       currentuser=requset.user
       discount=2
       state=False
       phone=ItemDetails.objects.select_related('itemmsid').filter(id=id)
    
       for item in phone:
           net=item.total-discount
       cart = Carrt(
      Id_product=item.id,
      Id_user=currentuser.id,
      price=item.price,
      qty=item.qty,
      tax=item.tax,
      total=item.total,
      discount=discount,
      net=net,
      status=state
) 
       currentuser=requset.user.id
       count=Carrt.objects.filter(Id_user=currentuser).count()
       print(count)
       cart.save()
       requset.session['countcart']=count
       return redirect("/showphone")



def showphone(request):
    template=loader.get_template('showphone.html')
    phone=ItemDetails.objects.select_related('itemmsid')
    context={''}
    print(phone.query)
    return HttpResponse(template.render({'phone':phone,'request':request}))

def details(request,id):
    template=loader.get_template('details.html')
    phone=ItemDetails.objects.select_related('itemmsid').filter(id=id)
    print(phone.query)
    context={
        'phone':phone,
        'request':request
    }
    return HttpResponse(template.render(context))

@csrf_exempt
def aut_logout(request):
    if request.method=="POST":
        logout(request)
        return redirect("/")

@csrf_exempt
def auth_login(request):
    form=LoginUserForm()
    if request.method=="POST":
        form=LoginUserForm(data=request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']

            user=authenticate(username=username,password=password)
            if user:
                if user.is_active:
                    login(request,user)
                    return render(request,'index.html')
    context={'form':form}
    return render(request, 'auth_login.html',context)

    

@csrf_exempt
def auth_register(request):
    template=loader.get_template('auth_register.html')
    form=CreateUserForm()
    if request.method=="POST":
        form=CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('auth_login')
    context={'registerform':form}     
    return HttpResponse(template.render(context=context))


def pay(requset):
    template=loader.get_template('pay.html')
    pay=Payno.objects.all()
    print(pay)
    return HttpResponse(template.render({'pay':pay,'request':requset}))
       


@csrf_exempt    
def addcarde(request):
    template=loader.get_template('add.html')
    if request.method=="POST":
        form=ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/pay')
    else:
            form=ProductForm
    return HttpResponse(template.render({'form':form}))

def done(request):
    template=loader.get_template('done.html')
    return HttpResponse(template.render())
