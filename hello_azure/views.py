from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

import logging
from kiteconnect import KiteConnect

def index(request):
    print('Request for index page received')
    return render(request, 'hello_azure/index.html')

@csrf_exempt
def hello(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        
        if name is None or name == '':
            print("Request for hello page received with no name or blank name -- redirecting")
            return redirect('index')
        else:
            print("Request for hello page received with name=%s" % name)
            context = {'name': name }
            return render(request, 'hello_azure/hello.html', context)
    else:
        return redirect('index')

def kitecheck(request):
    kite = KiteConnect(api_key="3qii6wc19h0s5qsk")
    data = kite.generate_session("wCJNX8W5YaXbOw5UvRUwc6qeBaNsHlHk", api_secret="be6ww12se8t0djxmnbrldzg95gdelw41")
    kite.set_access_token(data["access_token"])
    # Fetch all orders
    orderlist=kite.orders()   
    logging.info("Order placed. ID is: {}".format(orderlist[0]))
    print(orderlist)
    