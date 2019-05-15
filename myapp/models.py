from django.db import models
# from django.core.validators import MinValueValidator,MaxValueValidator
import uuid
class Coupon(models.Model):
	code = models.CharField(max_length=50,unique=True)
	valid_from=models.DateTimeField()
	valid_to=models.DateTimeField()
	# discount=models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(100)])
	active=models.BooleanField()
	def __str__(self):
		return self.code
# class Factory(models.Model):
# 	factory_name=models.CharField(max_length=100)
# 	email = models.EmailField()
# 	contact_number=models.IntegerField()
# 	facebook_id=models.CharField(max_length=50)
# class Employee(models.Model):
# 	factory_name=models.ForeignKey(Factory,on_delete=models.CASCADE)
# 	code=models.CharField(max_length=100, null=True, blank=True, unique=True, default=uuid.uuid4()) 
# 	# code_number = models.CharField(max_length=50,unique=True)
# 	employee_name=models.CharField(max_length=100)
# 	valid_from=models.DateTimeField()
# 	valid_to=models.DateTimeField()
# 	active=models.BooleanField()
