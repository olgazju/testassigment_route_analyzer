from .models import Route, Location
from rest_framework import viewsets
from .serializers import RouteSerializer, LocationSerializer
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

class RouteViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Route.objects.all()
    serializer_class = RouteSerializer


class LocationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

    def get_queryset(self):
        route_id = self.request.query_params.get('route_id')
        
        queryset = Location.objects.filter(route_id=route_id).order_by("timestamp")

        return queryset

@csrf_exempt
def intersection(request):
    if request.method == 'POST':
        print("post", request.POST)
        queryset = Location.objects.all()
        return JsonResponse({'routes':[1, 2]})