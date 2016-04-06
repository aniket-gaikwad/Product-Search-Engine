from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from searchEngine.models import product_info
import ipdb
import json
from django.core import serializers
from haystack.query import SearchQuerySet
import scraping

# Create your views here.

def home(request):
	"""
		This view is for landing of Project.
	"""
	list_product_objects=product_info.objects.all()
	if(len(list_product_objects)==0):
		## Empty table
		scraping.getJSONdata();
	return render_to_response("base.html",RequestContext(request))



def display(request):
	return render_to_response("display.html",RequestContext(request))



def displayData(request):
	"""	
		A developer view to see all data in database.
	"""
	#ipdb.set_trace();
	product_info_data=product_info.objects.all()
	return render_to_response("display.html",{'data':product_info_data},RequestContext(request))



def search(request):
	"""	
		This view will load landing page for searchEngine app.
		It will initially check for database if table contains entries. If not call scraper.
	"""
	list_product_objects=product_info.objects.all()
	if(len(list_product_objects)==0):
			scraping.getJSONdata();
	return render(request,"search_results.html",RequestContext(request))




def search_titles(request):
	"""	
		This will search index for given query and generate the querySet results for it.
	"""
	#ipdb.set_trace()
	object_list=[]
	print("search_title starts")
	print(request)
	try:
		sTerm = request.POST['query']
		#sTerm="maths"
		print("\n Print query term : {0}").format(sTerm)
		if sTerm==None or sTerm=="":
			return render_to_response("ajax_search.html",{'data':object_list},RequestContext(request))
		
	except:
		print("\n EXCEPTION")
		return render_to_response("ajax_search.html",{'data':object_list},RequestContext(request))
	
	results = SearchQuerySet().autocomplete(content_auto=request.POST.get('query',''))
	i=0
	for entry in results:
		object_list.append(product_info.objects.get(pk=entry.pk))
		print("\n results : {0}").format(object_list[i].index)
		i+=1

	return render_to_response("ajax_search.html",{'data':object_list},RequestContext(request))
	 

 
def flag_values(request):
	"""
		This view will update the flag entries in database.
	"""
	#print("flag_values : ")
	dictionary=request.POST
	#print(dictionary)
	product_id=dictionary["product-id"]
	entry=product_info.objects.get(pk=product_id)
	inappropriate=0
	not_helpful=0
	wrong_tags=0
	spam=0
	for key,val in dictionary.iteritems():
		if key=="inappropriate": 
			inappropriate=1
		if key=="not_helpful": 
			not_helpful=1
		if key=="wrong_tags": 
			wrong_tags=1
		if key=="spam":
			spam=1
	#print("\n  product_id : {0} , inappropriate : {1} , not_helpful : {2} , wrong_tags : {3} , spam : {4}").format(product_id,\
	#inappropriate,not_helpful,wrong_tags,spam)	
	
	product_info.objects.filter(pk=product_id).update(Inappropriate=inappropriate,not_helpful=not_helpful,\
		wrong_tags=wrong_tags,spam=spam)
	return HttpResponse(1)
	 

	

	


