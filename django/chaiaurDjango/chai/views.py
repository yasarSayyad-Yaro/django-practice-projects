from django.shortcuts import render,get_object_or_404
from .models import Chaivariety
# Create your views here.
def all_chai(request):
    chais=Chaivariety.objects.all()
    return render(request,'chai/all_chai.html',{'chais':chais})

def chai_detail(request,chai_id):
    chai=get_object_or_404(Chaivariety,pk=chai_id)
    return render(request,'chai/chai_detail.html',{'chai':chai})