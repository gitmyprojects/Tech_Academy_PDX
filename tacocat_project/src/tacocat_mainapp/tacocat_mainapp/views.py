from django.shortcuts import render, redirect

# *********************************** functions to render templates *********************************************

# the functions created here are called by the urls.py file via the path. ex. views.home where home is the function in
# the views.py file

def home(request): # 'request is what is entered in the browser bar
    return render(request, 'home.html') # the string goes into the tacocat_app dir and gets the index.html
# file
# the reason the template folder doesnt have to be explicitly named is because the html file is in the same dir as
# the app. django recognizes its relativity.

def concept(request):
    return render(request, 'concept.html')

def scoreboard(request):
    return render(request, 'scoreboard.html')


def bacon_sausage(request):
    return render(request, 'bacon_sausage.html')

# ***********************************END of functions to render templates *********************************************








