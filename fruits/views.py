from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt

def read_json():
    with open('data.json', 'r', encoding='utf-8') as file:
        file = json.load(file)

    json_file =[]
    json_file = file
    
    return json_file
    

# Create your views here.
@csrf_exempt
def index(request , methods = ('GET','POST')):
    # Opening JSON file
    if request.method == 'GET' :
        file = read_json()
        return JsonResponse(file,safe=False)
    
    if request.method == 'POST' :
        file = read_json()

        req = json.loads(request.body)
        
        for i in file:
            if i['id'] == req['id']:
                return JsonResponse({'error' : 'ID not vaild' })
            
        file.append(req)

        with open('data.json', 'w') as outfile:
            json.dump(file, outfile)
            
        return JsonResponse(file,safe=False)
        

def get_fruit(request,id ):
    #define var to put the id in it
    obj = None
    
    file = read_json()
    # make for loop to check the data
    for i in file :
        if i['id'] == id:
            obj = i
            break
    
    #check the data if it's null or invald
    if obj == None:
        return JsonResponse({'error' : 'ID not found' })
   
    return JsonResponse(obj)
