import http

from django.shortcuts import render, redirect, get_object_or_404
from .forms import UserForm
from .models import User
from django.http import HttpResponseRedirect, HttpResponse


def join(request):
    return render(request, 'join.html')

def confirmation(request):
    user = request.user
    context = {
        'user': user,
    }
    # by adding 'context' i make it available when the page is rendered after the method is called
    # being available means that i can display the value stored in the dictionary when i call the key
    # using two curly braces
    return render(request, 'new_user_confirmation.html', context)

def createUser(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('new_user_confirmation.html')
    else:
        print(form.errors)
        form = UserForm()
    context = {
        'form': form,
    }
    return render(request, 'create_user.html', context)









# **************************************Sandbox********************************
# I wasted my time following the instructions but the code below could be
# helpful if im trying to edit items already in the db such as a user profile



# def signup(request, pk):
#     pk = int(pk)
#     item = get_object_or_404(User, pk=pk)
#     form = UserForm(data=request.POST or None, instance=item)
#     if request.method == 'POST':
#         if form.is_valid():
#             form2 = form.save(commit=False)
#             form2.save()
#             return redirect('topics')
#         else:
#             print(form.errors)
#     else:
#         return render(request, 'topics.html', {'form': form})
#
#

