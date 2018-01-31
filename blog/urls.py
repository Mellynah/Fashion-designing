from django.conf.urls import patterns, url
from blog import views

urlpatterns = [
 url(r'^$', views.index, name='index'),
   url(r"^about/$", views.about, name='about'),
    url(r"^shop/$", views.shop, name='shop'),
     url(r"^shop/ladies/$", views.shop, name='shop'),
      url(r"^contacts/$", views.contacts, name='contacts'),
       url(r"^gallery/$", views.gallery, name='gallery'),
         url(r'^login/$', views.login, name='login'),
          url(r'^register/$', views.register, name='register'),
           url(r'^ladies/$', views.ladies, name='ladies'),
            url(r'^gents/$', views.gents, name='gents'),
]
