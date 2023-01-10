from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
import json

# Create your views here.
def index(request):
    # Opening JSON file
    f = open('data.json')
    
    # returns JSON object as a dictionary
    data = json.load(f)
    
    # Closing file
    f.close()
    
    #return the data
    return JsonResponse(data,safe=False)

def get_fruit(request,id):
    # Opening JSON file
    f = open('data.json')
    
    # returns JSON object as a dictionary
    data = json.load(f)
    
    #define var to put the id in it
    obj = None
    
    # make for loop to check the data
    for i in data :
        if i['id'] == id:
            obj = i
            break
    
    #check the data if it's null or invald
    if obj == None:
        return JsonResponse({'error' : 'ID not found' })
    
    # Closing file
    f.close()    
    return JsonResponse(obj)

def add_fruit(request, methods = ('GET','POST')):
    if request.method == 'GET' :
        return render(request, 'templates/add_fruit.html')
        