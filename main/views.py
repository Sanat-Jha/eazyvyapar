from django.shortcuts import render
from .models import register,query
# Create your views here.
def main(request):
    if request.method == "POST":
        if request.POST.get("query") == None:
            F_name = request.POST.get("first name")
            S_name = request.POST.get("second name")
            Email = request.POST.get("email")
            Phone = request.POST.get("phone")
            user = register(first_name=F_name,second_name=S_name,email=Email,phone=Phone)
            user.save()
            context = {
                "name" : F_name,
                "register" : True
            }
        else:
            F_name = request.POST.get("first name")
            S_name = request.POST.get("second name")
            Email = request.POST.get("email")
            Phone = request.POST.get("phone")
            Query = request.POST.get("query")   
            user = query(first_name=F_name,second_name=S_name,email=Email,phone=Phone,query=Query)
            user.save()
            context = {
                "name" : F_name,
                "register" : False
            }
    else:
        context = {
                "register" : None
            }
    return render(request,"index.html",context)