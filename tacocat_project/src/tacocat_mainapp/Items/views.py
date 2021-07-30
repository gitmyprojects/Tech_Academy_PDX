from django.shortcuts import render
from .models import Item

def topics(request):
    return render(request, 'topics.html')

# ********************* create item form  ***********************************************
# this is commented out because im going to need it but not yet. step 379


# def create_item(request):
#     # store info stored in the ItemForm class, including the parameters, in 'form' variable
#     form = ItemForm(data=request.POST or None)
#
#     # if the method sent to the database via the browser request is POST then...
#     if request.method == 'POST':
#
#         # if the data stored in 'form' variable is valid, save and redirect to the url path named 'index'
#         if form.is_valid():
#             form.save()
#             return redirect('index')
#
#     # store the data in the 'form' variable in a KVP with the key of 'form' in variable named 'content'
#     content = {'form': form}
#
#     # return the 'topics.html' page with the data stored in 'content' (the form data)
#     return render(request, 'topics.html', content)
# Create your views here.
