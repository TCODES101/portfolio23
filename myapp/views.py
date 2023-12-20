from django.shortcuts import render

# Create your views here.
def home_view(request):
    return render(request,'index.html')
def rps_view(request):
    return render(request,'rock-paper-scissors.html')
def todo_view(request):
    return render(request,'to-do-list.html')