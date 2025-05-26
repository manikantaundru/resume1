from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render

from app.models import Profile
from django.template import loader
import pdfkit

# Create your views here.
def accept(request):
    if request.method=="POST":
        name=request.POST.get("name")
        mobile=request.POST.get("mobile")
        about=request.POST.get("about")
        degree=request.POST.get("degree")
        university=request.POST.get("university")
        school=request.POST.get("school")
        previous_work=request.POST.get("previous_work")
        skills=request.POST.get("skills")
        profile=Profile(name=name,,phone=mobile,summary=about,degree=degree,university=university,school=school,previous_work=previous_work,skills=skills)
        profile.save()
    return render(request,'app/accept.html')
def resume(request,id):
    user_profile=Profile.objects.get(id=id)
    template=loader.get_template('app/resume.html')
    html=template.render({'user_profile':user_profile})
    options={
        'page-size':'Letter',
        'encoding':"UTF-8",
    }
    pdf=pdfkit.from_string(html,False,options=options)
    response=HttpResponse(pdf,content_type='application/pdf')
    response['Content-Disposition']='attachment;filename="resume.pdf"'
    return response

   
