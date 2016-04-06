import json
import urllib2
import MySQLdb
from searchEngine.models import product_info
count=0
 


def getJSONUtil(url):
	"""
		This method will pull data from Edmodo api and using models push data into 
		'searchEngine_product_info' table.
	"""
	global count
	data = json.load(urllib2.urlopen(url))
	products=data["products"]
	## get _source,_index,_id from products
	for i in range(len(products)):
		_index=products[i]["_index"]
		_id=products[i]["_id"]
		fields=products[i]["fields"]
		print("\n Id : {0}").format(_id)
		print("\n Index : {0}").format(_index)
		###  get nested data in _source
		long_desc_html=fields["long_desc_html"][0]
		seller_thumb_url=fields["seller_thumb_url"][0]
		resource_types=fields["resource_types"][0]
		content_type=fields["content_type"][0]
		long_desc=fields["long_desc"][0]
		title=fields["title"][0]
		greads_review_url=fields["greads_review_url"][0]
		url=fields["url"][0]
		edm_score=fields["edm_score"][0]
		avg_rating=fields["avg_rating"][0]
		creation_date=fields["creation_date"][0]
		#print("\n long_desc_html : {0} \n seller_thumb_url : {1} \n resource_types : {2}").format(long_desc_html[0],seller_thumb_url[0],resource_types[0])
		#print("\n content_type : {0} \n long_desc : {1} \n title : {2} \n greads_review_url : {3}").format(content_type[0],long_desc[0],title[0],greads_review_url[0])
		#print("\n url : {0} \n edm_score : {1} \n avg_rating : {2} \n creation_date : {3}").format(url[0],edm_score[0],avg_rating[0],creation_date[0])
		
		try:
			p1=product_info(index=_index,product_id=_id,long_desc_html=long_desc_html,seller_thumb_url=seller_thumb_url,resource_types=resource_types,\
		content_type=content_type,long_desc=long_desc,title=title,url=url,edm_score=edm_score,avg_rating=avg_rating,creation_date=creation_date)
			p1.save()
		except Exception,e:
			print("\n ERROR : Insert unsuccessful... ")
			print str(e)
			 
		print("\n Insert Success ...")
		count+=1
 


def getJSONdata():
	"""
		This will build url using search term and call getJSONUtil
	"""

	base_url="https://spotlight.edmodo.com/api/search/?q="
	query_term_list=["math","mitosis", "fractions","history","arts","holidays","cooking","dance","drama","music","graphical arts","programming","web design","game design","phonics",
	"reading","poetry","writting","chinese","german","english","latin","french","arabic","spanish","italian","calculus","decimals","statistics","geometry","religion","coaching","arithmetic"]
	for query_term in query_term_list:
		try:
			url=base_url+query_term
			getJSONUtil(url)
				
		except Exception,e:
			print("ERROR at : {0}").format(query_term)
			print str(e)
		
	print("\n **** Total products *** : {0}").format(count)
	

# if __name__=="__main__":
# 	getJSONdata()	
# 	#MySQLConn()