from django.urls import path, reverse
from django.conf import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('register/login/',views.Userlogin, name='login'),
    path('register/', views.register, name='register'),
    path('review/', views.review, name='review' ),
    path('review/contact/review', views.review, name='movies'),
    path('review/contact/', views.contact, name='contact'),
    path('review/search/', views.search, name='search'),
    path('review/contact/', views.contact, name='contact')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)