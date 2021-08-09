from django.http.response import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from .models import Bot, DeliveryFinal, Table, Delivery
from .serializers import DeliveryFinalSerializer, BotSerializer, TableSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response

import time

# Create your views here.

#################################################################
################    BOT SELECTION VIEW     ######################
#################################################################
def selectBot(request):
    qs = Bot.objects.all().filter(avialable = True)
    qs1 = Bot.objects.all().filter(avialable = False)
    return render(request, 'FlunkeyApp/select_bot.html', {'qs':qs, 'qs1':qs1})
#################################################################
#################################################################
#################################################################

#################################################################
###################    BOT REPAIR VIEW     ######################
#################################################################
def RepairBot(request, id):
    obj = Bot.objects.get(id = id)
    obj.avialable = True
    obj.save()
    return redirect('FlunkeyApp:select-bot')

#################################################################
#################################################################
#################################################################


#################################################################
################  TABLE SELECTION VIEW     ######################
################################################################# 
def selectTable(request, bot):
    qs = Table.objects.all().filter(avialable = True)   # To fetch avialable tables
    qs1 = Table.objects.all().filter(avialable = False)  # To fetch unavilable tables
    b = Bot.objects.get(id = bot)
    bot_no = b.bot_no
    bot_name = b.name
    bot_ip = b.ip
    bot_port = b.port


    d = Delivery.objects.create(
                                bot_no = bot_no,
                                bot_name = bot_name,
                                ip = bot_ip,
                                port = bot_port,
                                food_delivered = False,
                                )
    return render(request, 'FlunkeyApp/select_table.html',  {'qs':qs, 'qs1':qs1})
#################################################################
#################################################################
#################################################################


#################################################################
##################  DELIVERY VIEW       #########################
#################################################################
def DeliveryView(request, table):
    d = Delivery.objects.latest('pk')
    table = Table.objects.get(id = table)

    table_no = table.table_number
    try:
        d = Delivery.objects.latest('pk')
        d.table_no = table_no
        d.save()  

        d1 = DeliveryFinal.objects.create(
                                        bot_no = d.bot_no,
                                        bot_name = d.bot_name,
                                        ip = d.ip,
                                        port = d.port,
                                        food_delivered = False,  
                                        table_no = d.table_no,
                                        time = time.time()
                                        )
        d1.save()      
    except:
        print('no deliveries')

    

    return render(request, 'FlunkeyApp/delivery.html', {'d1':d1})


def DeleteTimeInDeliView(request):
    obj = DeliveryFinal.objects.latest('pk')
    obj.time = 0
    obj.save()

    return redirect('FlunkeyApp:select-bot')

#################################################################
#################################################################
#################################################################


#################################################################
###################    API DATA FOR GET METHOD    ###############
#################################################################

#################################################################
@api_view(['GET'])
def GetApiView(request):
    print('api')
    data = DeliveryFinal.objects.latest('pk')
    serializers = DeliveryFinalSerializer(data, many = False)
    print(serializers.data)
    return Response(serializers.data)    
#################################################################
#################################################################


#################################################################
##################    API DATA FOR PUT METHOD     ###############
#################################################################
@api_view(['POST'])
def UpdateBotView(request, bot_no):
    b = Bot.objects.get(bot_no = bot_no)
    print(b.avialable)
    serializer = BotSerializer(instance = b, data = request.POST)
    
    if serializer.is_valid():
        print('valid serializer')        
        serializer.save()
    print(serializer.data['avialable'])
    return Response(serializer.data)    


@api_view(['POST'])
def UpdateTableView(request, id):
    t = Table.objects.get(id = id)
    print(t.avialable)
    serializer = TableSerializer(instance = t, data = request.POST)
    
    if serializer.is_valid():
        print('valid serializer')        
        serializer.save()
    print('hiii')
    return Response(serializer.data)



#################################################################
#################################################################
#################################################################





def check(request):
    return render(request, 'FlunkeyApp/base.html')