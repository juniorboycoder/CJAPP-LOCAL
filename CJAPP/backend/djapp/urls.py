from django.urls import include
from django.conf.urls import  url


from .views import HomeView
from .import views

from django.urls import path

from django.urls import reverse_lazy
  
from rest_framework.urlpatterns import format_suffix_patterns

from django.conf import settings
from django.conf.urls.static import static

from django.contrib.auth import views as auth_views




app_name='djapp'

urlpatterns = [
    url(r'^$', views.HomeView, name="homeapp"),

    url(r'^login/$', views.LoginView.as_view(), name='login'),

    url(r'^logout_user/$', views.logout_user, name='logout_user'),
    

    url(r'^posted/(?P<pk>[0-9]+)/$', views.QuestionDetail, name='questiondetail'),

    url(r'^postedtailoring/(?P<pk>[0-9]+)/$', views.QuestionDetail2, name='questiondetail2'),
    
    url(r'^mainpagevisitor/$', views.MainPageDirectVisitors, name='mainpagevisitor'),


  
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate_account, name='activate'),

    url(r'^user/$', views.UsersView.as_view(), name= 'user'),

    url(r'^carpentryquestion/$', views.CarpentryCreate.as_view(), name= 'carpentryadded'),

    url(r'^tailoringquestion/$', views.TailoringCreate.as_view(), name= 'tailoringadded'),

    url(r'^posted/(?P<pk>[0-9]+)/addcomment/$', views.addcarpentrycomments, name='addcomment'),

    url(r'^posted/(?P<pk>[0-9]+)/addcommenttailoring/$', views.addtailoringcomments, name='addcomment2'),


   
    url(r'^profile/(?P<pk>\d+)/$', views.view_profile, name='profile'),
    
    url(r'^otherprofile/(?P<pk>\d+)/$', views.view_profile2, name='profile2'),

    url(r'^editprofile/$', views.edit_profile, name='editprofile'),
    
    url(r'^profile/(?P<pk>[0-9]+)/addnotes/$', views.AddNotes, name='AddNotes'),

    url(r'image/(?P<pk>[0-9]+)/$', views.Addimage.as_view(), name='image-add'),

   
    url(r'^(?P<pk>[0-9]+)/delete/$', views.Notesdelete.as_view(), name='notes-delete'),
    
    url(r'^(?P<pk>[0-9]+)/deletecarpentry/$', views.Carpentrydelete.as_view(), name='carpentry-delete'),
    
    url(r'^(?P<pk>[0-9]+)/carpdelete/$', views.carpentrycommentdelete.as_view(), name='carpentrycomments-delete'),

    url(r'^(?P<pk>[0-9]+)/deletetailoring/$', views.Tailoringdelete.as_view(), name='tailoring-delete'),

    url(r'^(?P<pk>[0-9]+)/commentingdeletetailoring/$', views.Tailoringcommentingdelete.as_view(), name='tailoringcomments-delete'),



    url(r'carpentry/(?P<pk>[0-9]+)/$', views.CarpentryUpdate.as_view(), name='carpentry-update'),
    

    url(r'tailoring/(?P<pk>[0-9]+)/$', views.tailoringUpdate.as_view(), name='tailoring-update'),
    
    url(r'^thanks/$', views.thanks, name='thanks'),
    
    
    url (r'^register/$', views.usersignup, name='register'),  

    #change password
    url(r'^change-password/$', views.change_password, name='change_password'),

#change password
    
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name= 'djapp/reset_password.html',email_template_name= 'djapp/reset_password_email.html', success_url=reverse_lazy('djapp:password_reset_done')), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name= 'djapp/reset_password_done.html'), name='password_reset_done'),
    path('password_reset/confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name= 'djapp/reset_password_confirm.html'), name='password_reset_confirm'),
    path('password_reset/complete/', auth_views.PasswordResetCompleteView.as_view(template_name= 'djapp/reset_password_complete.html'), name='password_reset_complete'),
    
   
]

