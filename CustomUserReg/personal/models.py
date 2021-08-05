from django.db import models

# Create your models here.

# PRIOR=[
# 	("H","high"),
# 	("M","medium"),
# 	("L","low"),
# ]

# class Question(models.Model):
# 	title=models.CharField(max_length=50)
# 	question=models.CharField(max_length=300)
# 	priority=models.CharField(max_length=1, choices=PRIOR)

# 	def __str__(self):
# 		return self.title

# 	class Meta:
# 		verbose_name="The question"
# 		verbose_name_plural="People questions"