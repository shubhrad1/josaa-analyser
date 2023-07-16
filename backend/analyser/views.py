from django.db.models import Q
from django.http import JsonResponse
from analyser.models import JosaaData, Institutes, Branch
from .serializers import InstituteSerializer, BranchSerializer
from django.conf import settings
import os

def get_data(request):
    query=JosaaData.objects.all()
    filters={
        'institute':request.GET.getlist('inst',[]),
        'program':request.GET.getlist('branch',[]),
        'seatType':request.GET.getlist('seat_type',[]),
        'gender':request.GET.getlist('gender',[]),
        'year':request.GET.getlist('year',[]),
        'round':request.GET.getlist('round',[])
    }

    filter_conditions = Q()

    for field,value in filters.items():
        if value and value != ['']:
            if value == ['Indian Institute of Technology (ISM) Dhanbad']:
                filter_conditions &= Q(**{f'{field}__in':value}) | Q(**{f'{field}__in':['Indian School of Mines Dhanbad']})
            else:
                filter_conditions &= Q(**{f'{field}__in':value})
    if filter_conditions:
        queryset=query.filter(filter_conditions)
    else:
        queryset=JosaaData.objects.all()

    data=list(queryset.values())

    return JsonResponse({'data': data},safe=False)

def enumerateData():
    branches=[]
    filepath_branches=os.path.join(settings.BASE_DIR,'orcr_data','allbranch.txt')
    with open(filepath_branches,'r') as file:
        for branch in file:
            branches.append(branch.strip())
    institutes=[]
    filepath_inst=os.path.join(settings.BASE_DIR,'orcr_data','allinstitutes.txt')
    with open(filepath_inst,'r') as file:
        for inst in file:
            institutes.append(inst.strip())

    
    seat=[]
    filepath_seat=os.path.join(settings.BASE_DIR,'orcr_data','allseat.txt')
    with open(filepath_seat,'r') as file:
        for set in file:
            seat.append(set.strip())

    year=[]
    filepath_year=os.path.join(settings.BASE_DIR,'orcr_data','allyear.txt')
    with open(filepath_year,'r') as file:
        for yr in file:
            year.append(yr.strip())
    
    round=[]
    filepath_round=os.path.join(settings.BASE_DIR,'orcr_data','allround.txt')
    with open(filepath_round,'r') as file:
        for rnd in file:
            round.append(rnd.strip())

    gender=[]
    filepath_gender=os.path.join(settings.BASE_DIR,'orcr_data','allgender.txt')
    with open(filepath_gender,'r') as file:
        for gen in file:
            gender.append(gen.strip())
    return JsonResponse({'institutes':institutes,'branches':branches,'seat':seat,'gender':gender,'year':year,'round':round},safe=False)

def getInstitute(request):
    if request.method == 'GET':
        institutes = Institutes.objects.values('name').distinct()
        serializer = InstituteSerializer(institutes, many=True)
        return JsonResponse(serializer.data, safe=False)
    
def getBranch(request,institute_id):
    if request.method == 'GET':
        try:
            institutes = Institutes.objects.get(id=institute_id)
            branches= Branch.objects.filter(institute=institutes).values('name').distinct()
            serializer = BranchSerializer(branches,many=True)
            return JsonResponse(serializer.data,safe=False)
        except Institutes.DoesNotExist:
            return JsonResponse({'error':'Invalid Institute ID'},status=400)
        