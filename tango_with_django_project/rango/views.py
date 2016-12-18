from django.shortcuts import render
from django.http import HttpResponse
from rango.models import Category
from rango.models import Page


def index(request):
	#construct dict to pass to the template enginge as its context - the key is bold message and is the same as {{bold message}} from the template
    
    category_list = Category.objects.order_by('likes')[:5]

    context_dict = {'categories': category_list}
    
    view_list = Page.objects.order_by('views')[:5]
    
    context_dict['pages'] = view_list
	
    #return the rendered response to the client, the first parameter is the template we want to use

    return render(request, 'rango/index.html', context=context_dict)

def about(request):
    context_dict = {'aboutMessage': 'I have added this message using a view!'}
    return render(request, 'rango/about.html', context=context_dict)

def show_category(request, category_name_slug):
    context_dict = {}

    try:

        category = Category.objects.get(slug=category_name_slug)
        pages = Page.objects.filter(category=category)
        context_dict['pages'] = pages
        context_dict['category'] = category

    except Category.DoesNotExist:
        context_dict['category'] = None
        context_dict['pages'] = None

    return render(request, 'rango/category.html', context_dict)



