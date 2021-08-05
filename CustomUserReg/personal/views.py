from django.shortcuts import render
# from personal.models import Question
from account.models import Account

# Create your views here.
def home_screen_view(request):
	# context={}
	# context["exmpl1"]= "how you doing"
	# context["exmpl2"]= "all good"

	# context={
	# 'exmpl1':"how you doing",
	# 'exmpl2':"all set  "
	# }

	
	# context={}
	# list_item=[]
	# list_item.append("one")
	# list_item.append('two')
	# list_item.append('three')
	# list_item.append('four')
	# context['list_itm']=list_item


	# to fetch from database
	# question=Question.objects.all()
	# context['question']=question


	# to fetch from account database
	context={}
	accounts= Account.objects.all()
	context['accounts']=accounts

	return render(request, "personal/home.html",context)
