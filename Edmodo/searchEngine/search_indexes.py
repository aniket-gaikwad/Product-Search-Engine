import datetime
from haystack import indexes
from searchEngine.models import product_info


class productIndex(indexes.SearchIndex,indexes.Indexable):
	text=indexes.CharField(use_template=True,document=True)
	#title=indexes.CharField(model_attr='title')
	#long_desc=indexes.CharField(model_attr='long_desc')

	content_auto=indexes.EdgeNgramField(model_attr='title')

	def get_model(self):
		return product_info

	def index_queryset(self,using=None):
		return self.get_model().objects.all()


