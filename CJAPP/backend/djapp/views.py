# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views import generic
# Create your views here.

from django.contrib.contenttypes.models import ContentType
from django.urls import reverse_lazy, reverse
from django.contrib.auth.forms import AuthenticationForm

from .models import carpentry, commenting,UserProfile,UserNotes,tailoring,tailorcommenting
from .forms import UserForm, CommentForm,  EditProfileForm,UserProfileForm, EditImageForm,AddNotesForm,carpentryForm,tailoringForm,tailoringCommentForm,ContactForm
from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import View
from django.contrib.auth import authenticate,login,logout

from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView, \
                                 UpdateView, RedirectView, FormView

from django.db.models import Q
from django.views.generic.edit import FormView

from django.http import HttpResponseRedirect, HttpResponse

from django.contrib.auth.models import User

from django.contrib.auth.decorators import login_required

from django.contrib.auth.mixins import LoginRequiredMixin


from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate

from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .token_generator import account_activation_token
from django.contrib.auth.models import User
from django.core.mail import EmailMessage

from django.contrib.auth.forms import PasswordChangeForm

from django.contrib.auth import (
    REDIRECT_FIELD_NAME, get_user_model, login as auth_login,
    logout as auth_logout, update_session_auth_hash,
)

from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect



class LoginView(FormView):
    template_name = 'djapp/login.html'
    form_class =  AuthenticationForm
    success_url = reverse_lazy('djapp:homeapp')


    def form_valid(self, form):
        login(self.request, form.get_user())
        return HttpResponseRedirect(self.success_url)



@ login_required

def QuestionDetail(request,pk=None):

    carpentrypostsdetail = get_object_or_404(carpentry, pk=pk)
    
   
    users=User.objects.exclude(id= request.user.id)
     
    args={ 'users': users }     
   
    return render(request, 'djapp/carpentryquestionsanddailyfacts.html', {'carpentrypostsdetail':carpentrypostsdetail},args)

@ login_required
def QuestionDetail2(request,pk=None):

    tailoringpostsdetail = get_object_or_404(tailoring, pk=pk)
    
   
    users=User.objects.exclude(id= request.user.id)
     
    args={ 'users': users }     
   
    return render(request, 'djapp/tailoringquestionsanddailyfacts.html', {'tailoringpostsdetail':tailoringpostsdetail},args)
    
    
@ login_required(login_url = '/djapp/mainpagevisitor/')

def HomeView(request):

   
    
    carpentryposts= carpentry.objects.all().order_by('-created')
    
    tailoringposts= tailoring.objects.all().order_by('-created')
    
    
    
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            
            Your_email = form.cleaned_data['Your_email']

            message = form.cleaned_data['message']
            to_email=  ('juniorboyboy2@gmail.com')
            try:
                email = EmailMessage(Your_email, message, to=[to_email])
                email.send()
                
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('djapp:thanks')
    
    mydict={'carpentryposts':carpentryposts ,'tailoringposts':tailoringposts,'form': form}

    return render(request, 'djapp/index.html',context=mydict)
 
    
    


@ login_required
def view_profile(request, pk=None):

 

 if pk:
         user = User.objects.get(pk=pk)
         
    
 else:
         
         user = request.user
 args = {'user': user}
 return render(request, 'djapp/user_profile.html', args)




@ login_required
def view_profile2(request, pk=None):

 

 if pk:
         user = User.objects.get(pk=pk)
         
    
 else:
         
         user = request.user
 args = {'user': user}
 return render(request, 'djapp/user_profile2.html', args)


    
class UsersView(LoginRequiredMixin, generic.ListView):

    template_name= 'djapp/users.html'
    context_object_name = 'users'
    def get(self,request):
     
      users=User.objects.exclude(id= request.user.id)
     
      args={ 'users': users }
      return render(request, self.template_name, args)
    



def MainPageDirectVisitors(request):

    carpentryposts= carpentry.objects.all()
    
    tailoringposts= tailoring.objects.all()

    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            
            Your_email = form.cleaned_data['Your_email']

            message = form.cleaned_data['message']
            to_email=  ('juniorboyboy2@gmail.com')
            try:
                email = EmailMessage(Your_email, message, to=[to_email])
                email.send()
                
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('djapp:thanks')
    
    
    mydict={'carpentryposts':carpentryposts ,'tailoringposts':tailoringposts, 'form': form}

    return render(request, 'djapp/indexvisitor.html',context=mydict)
 
    
    



def usersignup(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()

            current_site = get_current_site(request)
            email_subject = 'Activate Your Account'
            message = render_to_string('djapp/activate_account.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)).decode(),
                'token': account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(email_subject, message, to=[to_email])
            email.send()

           
           
            user.save()
            
            
            return redirect('djapp:thanksregister')
    else:
        form = UserForm()
    return render(request, 'djapp/signup.html', {'form': form})





@ login_required
def addcarpentrycomments(request, pk=None):
     commentpost = get_object_or_404(carpentry,pk=pk)


     
     if request.method== 'POST':
         form=CommentForm(request.POST)
        
         if form.is_valid():
                commenting = form.save(commit=False)
                commenting.user= request.user
                commenting.posting= commentpost
                
                commenting.save()

                
                return redirect ('djapp:questiondetail', pk=commentpost.pk)
     else:
         form=CommentForm()
        
     return render(request, 'djapp/addcomment.html', {'form':form},)



@ login_required
def addtailoringcomments(request, pk=None):
     commentpost = get_object_or_404(tailoring,pk=pk)


     
     if request.method== 'POST':
         form=tailoringCommentForm(request.POST)
        
         if form.is_valid():
                commenting = form.save(commit=False)
                commenting.user= request.user
                commenting.posting= commentpost
                
                commenting.save()

                
                return redirect ('djapp:questiondetail2', pk=commentpost.pk)
     else:
         form=CommentForm()
        
     return render(request, 'djapp/addtailoringcomment.html', {'form':form},)






class CarpentryCreate(LoginRequiredMixin, CreateView):
    model= carpentry
    fields = [  'title','imagedailyupdate','latestcarpentryupdate','linktofurtherreading']

    def form_valid(self, form):


        form.instance.user = self.request.user
        return super(CarpentryCreate, self).form_valid(form)

class TailoringCreate( LoginRequiredMixin,CreateView):
    model= tailoring
    fields = [  'title','imagedailyupdate','latesttailoringupdate','linktofurtherreading']

    def form_valid(self, form):


        form.instance.user = self.request.user
        return super(TailoringCreate, self).form_valid(form)




class Carpentrydelete(LoginRequiredMixin,DeleteView):
    model= carpentry

    

    success_url= reverse_lazy('djapp:homeapp')


class Tailoringdelete(LoginRequiredMixin,DeleteView):
    model= tailoring
    

    success_url= reverse_lazy('djapp:homeapp')

class carpentrycommentdelete(LoginRequiredMixin,DeleteView):
    model= commenting
    
    

    success_url= reverse_lazy('djapp:homeapp')

class Tailoringcommentingdelete(LoginRequiredMixin,DeleteView):
    model= tailorcommenting
    

    success_url= reverse_lazy('djapp:homeapp')





def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    
    return render(request, 'djapp/logout.html',context)


@ login_required
def edit_profile(request, pk=None):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect(reverse('djapp:editprofile'))
    else:
        form = EditProfileForm(instance=request.user)
        args = {'form': form}
        return render(request, 'djapp/edit_profile.html', args)

   

class Addimage(LoginRequiredMixin,UpdateView):
    model= UserProfile
    fields = ['image','career_interests']
    success_url = reverse_lazy('djapp:homeapp')


@ login_required
def AddNotes(request, pk):
    addnotepost = get_object_or_404(User,pk=pk)
   

    if request.method== 'POST':
         form=AddNotesForm(request.POST)
         if form.is_valid():
                addnote= form.save(commit=False)
                
                

                addnote.user= request.user
                
                addnote.save()

                
                return redirect ('djapp:AddNotes', pk=addnotepost.pk)
    else:
        form=AddNotesForm()
        
    return render(request, 'djapp/user_profile.html', {'form':form})




class Notesdelete(LoginRequiredMixin,DeleteView):
    model= UserNotes
    

    success_url= reverse_lazy('djapp:homeapp')






def activate_account(request, uidb64, token):
    try:
        uid = force_bytes(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return redirect('djapp:successregister')
    else:
        return HttpResponse('Activation link is invalid!')

@ login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request,form.user)
            return redirect(reverse('djapp:homeapp'))
        else:
            return redirect(reverse('djapp:change_password'))
    else:
        form = PasswordChangeForm(user=request.user)

        args = {'form': form}
        return render(request, 'djapp/change_password.html', args)


class CarpentryUpdate(LoginRequiredMixin,UpdateView):
    model= carpentry
    fields = ['title','imagedailyupdate','latestcarpentryupdate','linktofurtherreading']


class tailoringUpdate(LoginRequiredMixin,UpdateView):
    model= tailoring
    fields = ['title','imagedailyupdate','latesttailoringupdate','linktofurtherreading']





def thanks(request):
    
    return render(request, 'djapp/thanksfeedback.html')



def thanksregister(request):
    
    return render(request, 'djapp/thankyouregister.html')

def successregister(request):
    
    return render(request, 'djapp/registrationsucess.html')
