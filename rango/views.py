from django.shortcuts import render
from django.http import HttpResponse

def index(request):

    context_dict = {'boldmessage':"Cruncy, creamy, cookie, candy, cupcake!"}

    return render(request, 'rango/index.html', context=context_dict)

# Return a rendered response to send to the client.
# We make use of the shortcut function to make our lives easier.
# Note that the first parameter is the template we wish to use.
def about(request):
    return HttpResponse("Rango says here is the about page"
                        "<p><a href='/rango/'>Home</a></p>")

