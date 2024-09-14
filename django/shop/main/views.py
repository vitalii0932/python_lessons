from django.shortcuts import render
from .models import Drugs

# Create your views here.
def drugs(request):
	content = Drugs.objects.all()

	return render(request, 'index.html', {
		'drugs': content
	})