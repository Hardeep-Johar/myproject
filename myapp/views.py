from django.shortcuts import render

# Create your views here.
def home(request):
    data = dict()
    import datetime
    data['time'] = datetime.datetime.now()
    return render(request,"home.html",context=data)