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

        # load the post request into var
        req = json.loads(request.body)
        
        for i in file:
            if i['id'] == req['id']:
                return JsonResponse({'error' : 'ID not valid' })
        
        # using append function to add the data to the file    
        file.append(req)
        
        # write into the file with the new data
        with open('data.json', 'w') as outfile:
            json.dump(file, outfile)
            
        return JsonResponse(file,safe=False)
        
@csrf_exempt
def get_fruit(request, id, methods = ('GET','DELETE')):
    #define var to put the id in it
    if request.method == 'GET':
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

    if request.method == 'DELETE' :
        #call the read file function 
        file = read_json()
        is_found = False
        
        # make for loop to check the id
        for index,i in enumerate(file) :
            
            if i['id'] == id:
                # delete the object from the file using pop function
                file.pop(index)
                is_found = True
                # open the file to wirte in it the new data
                with open('data.json', 'w') as outfile:
                    json.dump(file, outfile)
                break
            
        # check if there isn't ID 
        if is_found == False :
                return JsonResponse({'error' : 'ID not found' })
        
        return JsonResponse(file,safe=False)
