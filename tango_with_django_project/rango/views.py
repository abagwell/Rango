from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	#construct dict to pass to the template enginge as its context - the key is bold message and is the same as {{bold message}} from the template
	context_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}
	#return the rendered response to the client, the first parameter is the template we want to use
	return render(request, 'rango/index.html', context=context_dict)

def about(request):
    context_dict = {'aboutMessage': 'I have added this message using a view!'}
    return render(request, 'rango/about.html', context=context_dict)


