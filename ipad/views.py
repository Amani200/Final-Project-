from typing import ItemsView
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.template import loader
from phone.models import Itemsipad,ItemDetailsipad,Carrt_ipad,Payno
from phone.forms import CreateUserForm
from phone.forms import LoginUserForm
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login, logout ,authenticate
from django.contrib.auth.decorators import login_required
from phone.forms import ProductForm

# Create your views here.

@login_required(login_url='/auth_login/')
def cipad(request):
      template=loader.get_template('cipad.html')
      current_user = request.user.id
      cart=Carrt_ipad.objects.all().filter(Id_user=current_user).first()
      product=Itemsipad.objects.get(itemdetailsipad=cart.Id_product)
      context={
            'cart':cart,
            'productname':product,
             'request':request
            
       }
      return HttpResponse(template.render(context=context)) 



def indexx(request):
    template=loader.get_template('index.html')
    return HttpResponse(template.render())

def add_to_cartipad(requset,id):
       currentuser=requset.user
       discount=2
       state=False
       ipad=ItemDetailsipad.objects.select_related('itemmsid').filter(id=id)
    
       for item in ipad:
           net=item.total-discount
       cart = Carrt_ipad(
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
       count=Carrt_ipad.objects.filter(Id_user=currentuser).count()
       print(count)
       cart.save()
       requset.session['countcart']=count
       return redirect("/showipad")



def showipad(request):
    template=loader.get_template('showipad.html')
    ipad=ItemDetailsipad.objects.select_related('itemmsid')
    context={''}
    print(ipad.query)
    return HttpResponse(template.render({'ipad':ipad,'request':request}))


def detailsipad(request,id):
    template=loader.get_template('dipad.html')
    ipad=ItemDetailsipad.objects.select_related('itemmsid').filter(id=id)
    print(ipad.query)
    context={
        'ipad':ipad,
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



def payipad(requset):
    template=loader.get_template('payipad.html')
    pay=Payno.objects.all()
    print(pay)
    return HttpResponse(template.render({'pay':pay,'request':requset}))
       


@csrf_exempt    
def addcardeipad(request):
    template=loader.get_template('addipad.html')
    if request.method=="POST":
        form=ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/pay')
    else:
            form=ProductForm
    return HttpResponse(template.render({'form':form}))

def doneipad(request):
    template=loader.get_template('doneipad.html')
    return HttpResponse(template.render())


