from django.shortcuts import render
from django.http import JsonResponse
from phone.models import Items,ItemDetails
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view

# Create your views here.

def getallitems(request):
    phone=Items.objects.all() #Get All Items
    phonelist=list(phone.values())
    return JsonResponse({
        'phone':phonelist
    })
@api_view(['GET'])
def list_item_details(request):
    phone=ItemDetails.objects.select_related('itemmsid').all()
    list1=[]
    for item in phone:
        getitems=({
            'id':item.id,
            'name':item.itemmsid.name,
            'color':item.color,
            'price':item.price,
            'qty':item.qty,
            'tax':item.tax,
            'total':item.total,
        })
        list1.append(getitems)
    return JsonResponse({'phone':list1})

def list_item_detailsbyid(request,id):
    phone=ItemDetails.objects.select_related('itemmsid').filter(id=id)
    list1=[]
    for item in phone:
        getitems=({
            'id':item.id,
            'name':item.itemmsid.name,
            'color':item.color,
            'price':item.price,
            'qty':item.qty,
            'tax':item.tax,
            'total':item.total,
        })
        list1.append(getitems)
    return JsonResponse({
        'phone':list1
    }) 

