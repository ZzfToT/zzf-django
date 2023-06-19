from django.shortcuts import render

def index(request):
    print("12312312313123")
    return render(request, "index.html")
