from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, QueryDict
from django.core import serializers
import datetime

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

def action(request):
    if request.method == 'GET':
        return getAllActions(request)
    elif request.method == 'PUT':
        return createAction(request)
    return HttpResponse(status=404)

def getAllActions(request):
    return JsonResponse(list(Action.objects.values('id', 'name_text', 'action_text')), safe=False)

def createAction(request):
    name = None
    action = None
    now = datetime.datetime.now()
    
    json_data = json.loads(request.body)
    try:
        name = json_data['name']
        action = json_data['action']
    except KeyError:
        # not defined
        return JsonResponse({'success':0}, status=400)
    
    # empty
    if not name or not action:
        return JsonResponse({'success':0}, status=400)
    
    a = Action(name_text=name,action_text=action,action_date=now)
    a.save()
    return JsonResponse({'success':1})

def automatable(request):
    if request.method == 'GET':
        return getAllAutomatables(request)
    elif request.method == 'PUT':
        return createAutomatable(request)
    return HttpResponse(status=404)

def getAllAutomatables(request):
    return JsonResponse(list(Automatable.objects.values('id', 'name_text', 'state_text')), safe=False)

def createAutomatable(request):
    name = None
    state = None
    
    json_data = json.loads(request.body)
    try:
        name = json_data['name']
        state = json_data['state']
    except KeyError:
        # not defined
        return JsonResponse({'success':0}, status=400)
    
    # empty
    if not name or not state:
        return JsonResponse({'success':0}, status=400)
    
    a = Automatable(name_text=name,state_text=state)
    a.save()
    return JsonResponse({'success':1})
