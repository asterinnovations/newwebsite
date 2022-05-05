import json
import os
import random
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.conf import settings
# Create your views here.
from django.core.mail import send_mail
from django.contrib import messages
import math
from django.views.decorators.csrf import csrf_exempt,csrf_protect #Add this
from django.core.mail import EmailMultiAlternatives
from email.mime.image import MIMEImage
from email.mime.image import MIMEImage
from functools import lru_cache
from django.contrib.staticfiles import finders
def home(request):
    if request.method == "POST":    
 
        # data from the form is fetched using super function
        
         
        # extract the username and text field from the data
        email = request.POST['inlineFormInputGroupUsername2']
        send_mail(
            'Email From: ' + settings.EMAIL_HOST_USER,  # subject

            'You are subscribed to Aster newsletter.' ,


            settings.EMAIL_HOST_USER,
            [email, ]
        )
        messages.success(request, 'You\'re subscribed to aster newsletter.')
   
    
    return render(request,'website1/index.html')

# @lru_cache()
# def logo_data():
#     img_path = os.path.join(settings.BASE_DIR, '/static/assets/img/logo.png')
#     print(img_path)
#     with open(finders.find('static/assets/img/logo.png'), 'rb') as f:
#         logo_data = f.read()
#     logo = MIMEImage(logo_data)
#     logo.add_header('Content-ID', '<logo>')
#     return logo

def about(request):
    if request.method == "POST":    
 
        # data from the form is fetched using super function
        
         
        # extract the username and text field from the data
        email = request.POST['inlineFormInputGroupUsername2']
        send_mail(
            'Email From: ' + settings.EMAIL_HOST_USER,  # subject

            'You are subscribed to Aster newsletter.' ,


            settings.EMAIL_HOST_USER,
            [email, ]
        )
        messages.success(request, 'You\'re subscribed to aster newsletter.')


    return render(request,'website1/about.html')




def contact(request):
   
   
   

    if  'newsletter' in request.POST:
        email = request.POST['inlineFormInputGroupUsername2']
        send_mail(
            'Email From: ' + settings.EMAIL_HOST_USER,  # subject

            'You are subscribed to Aster newsletter.' ,


            settings.EMAIL_HOST_USER,
            [email, ]
        )
        messages.success(request, 'You\'re subscribed to aster newsletter.')
    
    
    if  'add_object' in request.POST:
        # name = request.POST['name']
        # print(name)
        print("ok")
  
        name = request.POST.get('name')
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        print(email)
        digits = "0123456789"
        OTP = ""
        for i in range(6) :
            OTP += digits[math.floor(random.random() * 10)]
         
        


        # email=request.GET.get   ("email")
        # print(email)
        o=OTP
        subject, from_email, to = 'Message From Aster Website', email, settings.EMAIL_HOST_USER
        text_content = 'This is an important message.'
        html_content = o + ' is your one time password (OTP). Please, enter the OTP to proceed. Thank you, Aster Innovation Pvt. Ltd.'
       
        msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
        msg.attach_alternative(html_content, "text/html")
        msg.send()

        # send_mail('OTP request',o,settings.EMAIL_HOST_USER,[email], fail_silently=False, html_message=htmlgen)
        print(o)
      
        # data = {'o':o}
        # print(data)
        # print(data['csrfmiddlewaretoken'])
        # return redirect('/contact')
        request.session['selected_name'] = name

        request.session['selected_subject'] = subject

        request.session['selected_message'] = message

        request.session['selected_email'] = email
        request.session['selected_otp'] = o
        # return render(request,'website1/otp.html')
        return redirect('otp')

        # return redirect('/contact')
        
   





    

    # if 'contact-form' in request.POST:
    #     name = request.POST.get('name')
    #     email = request.POST['email']
    #     subject = request.POST['subject']
    #     message = request.POST['message']
        
    #     print('the message has been sent')
    #     return render("/")
    #     messages.success(request, 'You\'re subscribe to aster newsletter.')


    return render(request,'website1/contact.html')




def services(request):
    if request.method == "POST":    
 
        # data from the form is fetched using super function
        
         
        # extract the username and text field from the data
        email = request.POST['inlineFormInputGroupUsername2']
        send_mail(
            'Email From: ' + settings.EMAIL_HOST_USER,  # subject

            'You are subscribed to Aster newsletter.' ,


            settings.EMAIL_HOST_USER,
            [email, ]
        )
        messages.success(request, 'You\'re subscribed to aster newsletter.')
    

    return render(request,'website1/services.html')

    
def team(request):
    if request.method == "POST":    
 
        # data from the form is fetched using super function
        
         
        # extract the username and text field from the data
        email = request.POST['inlineFormInputGroupUsername2']
        send_mail(
            'Email From: ' + settings.EMAIL_HOST_USER,  # subject

            'You are subscribed to Aster newsletter.' ,


            settings.EMAIL_HOST_USER,
            [email, ]
        )
        messages.success(request, 'You\'re subscribed to aster newsletter.')
    
  
    return render(request,'website1/team.html')

def terms(request):
    if request.method == "POST":    
 
        # data from the form is fetched using super function
        
         
        # extract the username and text field from the data
        email = request.POST['inlineFormInputGroupUsername2']
        send_mail(
            'Email From: ' + settings.EMAIL_HOST_USER,  # subject

            'You are subscribed to Aster newsletter.' ,


            settings.EMAIL_HOST_USER,
            [email, ]
        )
        messages.success(request, 'You\'re subscribed to aster newsletter.')
    
    return render(request,'website1/terms.html')


def cliq(request):
    return render(request,'website1/cliq.html')


def privacy(request):
    if request.method == "POST":    
 
        # data from the form is fetched using super function
        
         
        # extract the username and text field from the data
        email = request.POST['inlineFormInputGroupUsername2']
        send_mail(
            'Email From: ' + settings.EMAIL_HOST_USER,  # subject

            'You are subscribed to Aster newsletter.' ,


            settings.EMAIL_HOST_USER,
            [email, ]
        )
        messages.success(request, 'You\'re subscribed to aster newsletter.')
    
    return render(request,'website1/privacy.html')


def otp(request):
    selected_name = request.session.get('selected_name')
    selected_subject = request.session.get('selected_subject')
    selected_message = request.session.get('selected_message')
    selected_email = request.session.get('selected_email')

    selected_otp = request.session.get('selected_otp')
    print('--------------')
    print(selected_email)
    print(selected_message)
    print(selected_name)
    print(selected_otp)
    print('-------------------')

    if 'verify-otp' in request.POST:
        otp = request.POST.get('otp')
        print(otp)
        otp=str(otp)
        selected_otp=str(selected_otp)
        print(selected_otp)
        if selected_otp == otp:
            print('##########')
            print(selected_name)
            print(selected_otp)

            subject, from_email, to = 'Message From Aster Website', selected_email, settings.EMAIL_HOST_USER
            text_content = 'This is an important message.'
            # html_content = '<p> You\'ve a message. Following is the detail</p> <table border="2"> <tr> <th>Name</th> <th>Email</th> <th>Subject</th> <th>Message</th> </tr> <tr> <td>'+name+ '</td> <td> ' + email + '</td> <td> ' +subject+'</td> <td>' + message+'</td>'
            html_content = '''
            <img src="cid:logo.png" width="auto" height="150" style="padding-left:500px"/>
            <p>You've got a message from the website. Look at below for the further details</p>
            
                    
            <table  align="center" width="100%">    
    <tr>
      <th>Name</th> <td >'''+ selected_name+'''</td>
      <hr>
    </tr>
   <tr>
     <th>Email</th> <td>'''+ selected_email+'''</td>
     <hr>
    </tr>
     <tr>
      <th>Subject</th> <td>'''+ selected_subject+'''</td>
    </tr>
     <tr>
      <th>Message</th> <td>'''+ selected_message+'''</td>
    </tr>
    </table>

            '''
            msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
            msg.mixed_subtype = 'related'
            msg.attach_alternative(html_content, "text/html")
            img_dir = 'static/assets/img'
            image = 'logo.png'
            file_path = os.path.join(img_dir, image)
            with open(file_path, 'rb') as f:
                img = MIMEImage(f.read())
                img.add_header('Content-ID', '<{name}>'.format(name=image))
                img.add_header('Content-Disposition', 'inline', filename=image)
            msg.attach(img)
           

           
            # msg.content_subtype = 'html'
            # msg.mixed_subtype = 'related'
            # img_path = os.path.join(settings.BASE_DIR, '/static/assets/img/logo.png')
            # with open(img_path, 'rb') as banner_image:
            #     banner_image = MIMEImage(img_path.read())
            #     banner_image.add_header('Content-ID', '<blogsImage.svg>')
            #     msg.attach(banner_image)
            # msg.send()
            msg.attach_alternative(html_content, "text/html")
            msg.send()

            msg.send(fail_silently=False)

            # send_mail(
            #     'From : '+ selected_email+'/ : '+ selected_subject,#subject
            #     'Message: '+html_content,

            #     selected_email,
            #         ['sabinkatwalof@gmail.com'],
            #     )
            messages.success(request,'Your message has been sent sucessfully.')
            return redirect('contacts')
        elif selected_otp != otp:

            messages.error(request,'Your otp is not correct. Please, type the correct OTP code.')
            return redirect('otp')
    return render(request,'website1/otp.html')

def generateOTP() :
     digits = "0123456789"
     OTP = ""
     for i in range(4) :
         OTP += digits[math.floor(random.random() * 10)]
     return OTP

def send_otp(request):
     email=request.GET.get   ("email")
     print(email)
     o=generateOTP()
     htmlgen = '<p>Your OTP is <strong>o</strong></p>'
     send_mail('OTP request',o,'<your gmail id>',[email], fail_silently=False, html_message=htmlgen)
     return HttpResponse(o)