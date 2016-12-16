import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tango_with_django_project.settings')

import django 

django.setup()

from rango.models import Category, Page

def populate():
	
	python_pages = [
		{"title": "Official Python Tutorial",
		"url": "http://docs.python.org/2/tutorial/"},
		{"title": "How to Think like a Computer Scientist",
		"url": "http://www.greenteapress.com/thinkingpython/"},
		{"title": "Learn Python in 10 Minutes", 
		"url": "http://www.korokitakis.net/tutorials/python/"}
		]

	django_pages = [

		{"title": "Official Django Tutorial", 
		"url": "https://docs.djangoproject.com/en/1.9/intro/tutorial01/"},
		{"title": "Django Rocks", 
		"url": "http://wwww.djangorocks.com/"},
		{"title": "How to Tango with Django", 
		"url": "http://www.tangowithdjango.com/"}
		]

	other_pages = [

		{"title": "Bottle", 
		"url": "http://bottlepy.org/docs/dev/"},
		{"title": "Flask", 
		"url": "http://flask.pocoo.org"}
		]

	cats = {"Python": {"pages": python_pages},
			"Django": {"pages": django_pages},
			"Other Frameworks": {"pages": other_pages} }


	for cat, cat_data in cats.items():
		#per the request to populate the categories with different values
		if cat == 'Python':
			c = add_cat(cat, 128, 64)
		elif cat == 'Django':
			c = add_cat(cat, 64, 32)
		else:
			c = add_cat(cat,32,16)

		for p in cat_data["pages"]:
			add_page(c, p["title"], p["url"])

	for c in Category.objects.all():
		for p in Page.objects.filter(category=c):
			print("- {0} - {1}".format(str(c), str(p)))

def add_page(cat, title, url, views=0):
	p = Page.objects.get_or_create(category=cat, title=title)[0]
	p.url=url
	p.views=views
	p.save()
	return p

#updated to add the ability to pass num of views and likes in as parameters 
def add_cat(name, numViews=0, numLikes=0):
	c = Category.objects.get_or_create(name=name, views=numViews, likes=numLikes)[0]
	c.save()
	return c

if __name__ == '__main__':
	print("Starting the Rango population script.")
	populate()
	
