from django.shortcuts import render
from rest_framework import viewsets, status
from .models import Knowledge_base

from .serilizer import KnowledgeSerializer

# Create your views here.




class KnowledgeViewset(viewsets.ModelViewSet):
    queryset = Knowledge_base.objects.all()
    serializer_class = KnowledgeSerializer
    



def load_data_template(request):
    return render(request, 'data_template.html')



def retrievedata(request):
    return render(request, 'retrievedata.html')