from django.shortcuts import render,redirect
from .models import CustomerEnquiry
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.utils.html import strip_tags
# Create your views here.

def Home(request):
    return render(request,'home.html')

def Query(request):
    if request.method == "POST":
        name = request.POST['name']
        mobile = request.POST['mobile']
        email = request.POST['email']
        queries = request.POST['queries']
        cust=CustomerEnquiry(name=name, mobile=mobile, email=email, queries=queries)
        cust.save()
        id = cust.id
        url = f"http://127.0.0.1:8000/{id}"
        try:
           send_mail('Support Desk mail',f'The Consumer Name is {name} And the Consumer mail id is {email}\n The Consumer Query: {queries}  \n you can response him by this link: {url}',settings.EMAIL_HOST_USER,[settings.EMAIL_HOST_USER],fail_silently=False)
        except:
            print("net not working proper")        
    return render(request,'query.html')
    
def Resp(request,id):
    url = f"http://127.0.0.1:8000/review"
    enq = CustomerEnquiry.objects.get(id=id)
    if request.method == "POST":
        resp = request.POST.get('resp')
        template = render_to_string('review.html',{'resp':resp,'enq':enq})
        template1 = strip_tags(template) 
        send_mail('Thank for your Suggestion',f'Hello Mr. {enq.name}\n as per you Suggestion {resp}\n \n You can rate us by thi link: {url}',None,[f'{enq.email}'],fail_silently=False)
        # email = EmailMessage('Thank for your Suggestion',template,settings.EMAIL_HOST_USER,[f'{enq.email}'],)
        # email = EmailMultiAlternatives('Thank for your Suggestion',template1,settings.EMAIL_HOST_USER,[f'{enq.email}'])
        # email.fail_silently = False
        # email.attach_alternative(template, "text/html")
        # email.send()   
    enq = CustomerEnquiry.objects.get(id=id)
    return render(request,'response.html',{'enq':enq})

def Review(request):
    return render(request,'review.html')