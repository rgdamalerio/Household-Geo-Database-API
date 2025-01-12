from django.shortcuts import render
from django.core.exceptions import PermissionDenied
from django.views.decorators.http import require_http_methods
from .forms import HouseholdSearchForm
from .serializers import HouseholdSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from aggregate.models import AggregatedFamiliesandPopulation
from django.db.models import Sum
from django.http import HttpResponse
from django.core.serializers import serialize
from .models import Households
from django.http import JsonResponse


def is_valid_queryparam(param):
    return param != '' and param is not None

@require_http_methods(["GET"])
def household_datasets(request):
    if request.user.is_authenticated:
        if request.user.is_superuser or request.user.groups.filter(name='admin').exists():
            qs = Households.objects.all()
        else:
            municipality = request.user.userlocation.psgccode_mun
            qs = Households.objects.filter(municipality=municipality)
        
        # Retrieve query parameters
        controlnumber_icontains_query = request.GET.get('controlnumber')
        purok_fk_icontains_query = request.GET.get('purok_fk')

        if controlnumber_icontains_query:
            qs = qs.filter(controlnumber__icontains=controlnumber_icontains_query)

        if purok_fk_icontains_query:
            qs = qs.filter(purok__icontains=purok_fk_icontains_query)

        query_params = [
            'respondent', 'enumerator', 'municipality', 'barangay', 'enumerator',
            'editor', 'year_construct', 'estimated_cost', 'number_bedrooms',
            'number_storey', 'medical_treatment', 'year_flooded', 'year_evacuate',
            'householdbuildingtypes', 'householdtenuralstatus', 'householdroofmaterials',
            'householdwallmaterials', 'householdwatertenuralstatus', 'waterlevelsystems',
            'evacuationareas'
        ]

        for param in query_params:
            value = request.GET.get(param)
            if is_valid_queryparam(value):
                qs = qs.filter(**{param + '__exact': value})

        boolean_fields = [
            'access_electricity', 'access_internet', 'access_water_supply',
            'potable', 'floods_occur', 'experience_evacuate',
            'access_health_medical_facility', 'access_telecommuniciation',
            'access_drill_simulation'
        ]

        for field in boolean_fields:
            values = request.GET.getlist(field)
            if values:
                qs = qs.filter(**{field + '__in': values})
        
        households = serialize('geojson', qs, use_natural_foreign_keys=True, fields=('pk', 'location', 'latitude', 'longitude'))
        return HttpResponse(households, content_type='application/json')
    
    else:
        qs = Households.objects.none()
        return HttpResponse(qs, content_type='application/json')

#AJAX
@require_http_methods(["GET"])
@api_view(['GET'])
def household_info(request):
  if request.user.is_authenticated:
    # # Do something for authenticated users.

    qs = Households.objects.get(pk=request.GET.get('pk'))
    serialize = HouseholdSerializer([qs],many=True)
    return Response(serialize.data)
  else:
    # Do something for anonymous users.
    raise PermissionDenied()

#AJAX
@require_http_methods(["GET"])
def household_search_form(request):
  if request.user.is_authenticated:
    # Do something for authenticated users.
    form = HouseholdSearchForm()
    context = {'form':form}
    return render(request,'household/household_search_form.html',context)
  else:
    # Do something for anonymous users.
    raise PermissionDenied()

#AJAX
@require_http_methods(['POST'])
def chart_view(request):
    if request.user.is_authenticated:
        if request.user.is_superuser or request.user.groups.filter(name='admin').exists():
            qresult = AggregatedFamiliesandPopulation.objects.values('munname').annotate(
                total_households=Sum('households'),
                total_male=Sum('male'),
                total_female=Sum('female'),
            )
        else:
            municipality = request.user.userlocation.psgccode_mun
            qresult = AggregatedFamiliesandPopulation.objects.filter(munname=municipality).values('munname').annotate(
                total_households=Sum('households'),
                total_male=Sum('male'),
                total_female=Sum('female'),
            )

        labels = []
        data = []
        for item in qresult:
            labels.append(item['munname'])
            data.append([
                item['total_households'],
                item['total_male'],
                item['total_female'],
            ])

        context = {'labels': labels, 'data': data}
        return render(request, 'household/chart_view_content.html', context)
    else:
        raise PermissionDenied()
    
def search_view(request):
    if request.method == 'POST':
        place_name = request.POST.get('search_input').strip()
        match_households = Households.objects.filter(barangay__psgccode__icontains=place_name)

        if match_households.exists():
            households = serialize('geojson', match_households, use_natural_foreign_keys=True, fields=('pk', 'location', 'latitude', 'longitude'))
            return HttpResponse(households, content_type='application/json')
        else:
            return JsonResponse({'message': f'No households found for search input: {place_name}'})
    else:
        return JsonResponse({'message': 'Invalid request method'})
