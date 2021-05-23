from django.shortcuts import render
from .models import GetIndexDataModel
import json
from django.http import HttpResponse


def index(request):
	return render(request,"index.html",{})



def GetIndexData(request,*args,**kwargs):
	objectslist=[]
	objs=GetIndexDataModel.objects.all().order_by('-id')
	for obj in objs:
		d={'schema':obj.schema,'rating':obj.rating,'aum':obj.aum,'fund_return_1yr':obj.fund_return_1yr,'fund_return_2yr':obj.fund_return_2yr,'fund_return_3yr':obj.fund_return_3yr,'fund_return_5yr':obj.fund_return_5yr,'fund_return_10yr':obj.fund_return_10yr,'volatility':obj.volatility,'unique_fund_id':obj.unique_fund_id}
		objectslist.append(d)
	return HttpResponse(json.dumps({'history_data': objectslist}), content_type="application/json")

