from django.shortcuts import render
def index(request):
    context = {'username': 'Star'}
    return render(request,'index.html',context=context)
def company(request):
    return render(request,'company.html')
def school(request):
    return render(request,'school.html')
# Create your views here.
