from __future__ import unicode_literals

from django.db import models

# Create your models here.

class product_info(models.Model):
	index=models.CharField(max_length=100,null=True)
	product_id=models.IntegerField(null=True)
	long_desc_html=models.CharField(max_length=1000,null=True)
	seller_thumb_url=models.CharField(max_length=1000,null=True)
	resource_types=models.CharField(max_length=1000,null=True)
	content_type=models.IntegerField(null=True)
	long_desc=models.CharField(max_length=1000,null=True)
	title=models.CharField(max_length=1000,null=True)
	url=models.CharField(max_length=1000,null=True)
	edm_score=models.FloatField(null=True)
	avg_rating=models.FloatField(null=True)
	creation_date=models.CharField(max_length=1000,null=True)
	Inappropriate=models.IntegerField(default=0,null=True)
	not_helpful=models.IntegerField(default=0,null=True)
	wrong_tags=models.IntegerField(default=0,null=True)
	spam=models.IntegerField(default=0,null=True)

	def __unicode__(self):
		return self.title

	#def __unicode__(self):
	#	return u'%s,%s,%s, %s, %s, %s ,%s ,%s, %s, %s ,%s, %s, %s ' % (self.index, self._id,self.long_desc_html,self.seller_thumb_url,self.resource_types,self.content_type,\
    #    	self.long_desc,self.title,self.greads_review_url,self.url,self.edm_score,self.avg_rating,self.creation_date)
