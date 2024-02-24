from django.shortcuts import render
from django.core.mail import send_mail
# Create your views here.
def mailfunction(request):
	send_mail(
	    'sent  mail',
	    'test email in Django with ishaan',
	    'mm8239239249@gmail.com',
	    ['Vt464670@gmail.com'],
	    fail_silently=False,
	)
	return render(request, 'index.html')