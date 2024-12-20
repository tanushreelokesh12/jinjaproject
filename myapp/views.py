from django.shortcuts import render

# Create your views here.
def view(request):
	name="Rama"
	place="Banglore"
	c={'Name':name,'Place':place}
	return render(request,'htmlpages/2.html',c)