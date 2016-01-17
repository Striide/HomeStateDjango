from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, QueryDict
from django.core import serializers
import json

from .models import Person, Action, Automatable

def index(request):
    return HttpResponse("HomeState index")

def people(request):
    if request.method == 'GET':
        return getAllPeople(request)
    elif request.method == 'PUT':
        return createPerson(request)
    return HttpResponse(status=404)

def getAllPeople(request):
    people = Person.objects.all()
    return JsonResponse(list(Person.objects.values('id', 'name_text')), safe=False)

def createPerson(request):
    
    name = None
    json_data = json.loads(request.body)
    try:
        name = json_data['name']
    except KeyError:
        # not defined
        return JsonResponse({'success':0}, status=400)
    
    # empty
    if not name:
        return JsonResponse({'success':0}, status=400)
    
    p = Person(name_text=name)
    p.save()
    
    return JsonResponse({'success':1})

def getAllActions(request):
    actions = Action.objects.all()
    output = ', '.join([a.name_text for a in actions])
    return HttpResponse(output)

def getAllAutomatables(request):
    automatables = Automatable.objects.all()
    output = ', '.join([a.name_text for a in automatables])
    return HttpResponse(output)