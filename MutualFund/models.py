from django.db import models

# Create your models here.

class GetIndexDataModel(models.Model):
	schema		=models.TextField()
	rating	    =models.TextField()
	aum		    =models.TextField()
	fund_return_1yr	=models.TextField()
	fund_return_2yr	=models.TextField()
	fund_return_3yr	=models.TextField()
	fund_return_5yr	=models.TextField()
	fund_return_10yr=models.TextField()
	volatility=models.TextField()
	unique_fund_id=models.TextField()
