from django.forms import ModelForm

from django.contrib.auth.models import User
from django import forms
from .models import commenting, UserProfile,UserNotes,carpentry,tailoring,tailorcommenting
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class UserProfileForm( UserCreationForm):
    

    class Meta:
      model  =  UserProfile
      fields = [ 'image','notes']


class ContactForm(forms.Form):

    Your_email = forms.EmailField(required=True)
    
    
    message = forms.CharField(widget=forms.Textarea)

   
class UserForm(UserCreationForm):
    

    class Meta:

      model  = User
      fields = ['username','email','password1','password2']
      email =forms.EmailField(required = True)
    

    def clean_email(self):
        # Get the email
        email = self.cleaned_data.get('email')

        # Check to see if any users already exist with this email as a username.
        try:
            match = User.objects.get(email=email)
        
        except User.MultipleObjectsReturned:
             user = User.objects.filter(email=email).order_by('id')[0]

        except User.DoesNotExist:
            # Unable to find a user, this is fine
            return email

        # A user was found with this as a username, raise an error.
        raise forms.ValidationError('This email address is already in use.')

class CommentForm(forms.ModelForm):
    class Meta:
      model  = commenting
      fields = [  'body']

class tailoringCommentForm(forms.ModelForm):
    class Meta:
     
      model  = tailorcommenting

      fields = [  'body']

class carpentryForm(forms.ModelForm):
    class Meta:
      model  = carpentry
      fields = [  'title','imagedailyupdate','latestcarpentryupdate','linktofurtherreading']


class tailoringForm(forms.ModelForm):
    class Meta:
      model  = tailoring
      fields = [  'title','imagedailyupdate','latesttailoringupdate','linktofurtherreading']

class EditProfileForm(forms.ModelForm):
    
    class Meta:
        model = User
        fields = (
            'email',
            'username'
            

        )

class UserProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ['image','career_interests']
        

class EditImageForm(forms.ModelForm):
       

    class Meta:
        model = UserProfile
        fields = ['image']
            
class AddNotesForm(forms.ModelForm):
    

    class Meta:
      model  = UserNotes
      fields = [ 'notes']
