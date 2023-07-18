from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name='name'),
    path('about/',views.about,name='about'),
    path('agent/<str:pk>/',views.agent,name='agent'),
    path('agentGrid/',views.agentGrid,name='agentGrid'),
    path('blog/<str:pk>/',views.blog,name='blog'),
    path('blogGrid/',views.blogGrid,name='blogGrid'),
    path('property/<str:pk>/',views.prop,name='property'),
    path('propertyGrid/',views.propertyGrid,name='propertyGrid'),
    path('contact/',views.contact,name='contact'),
    path('comment/',views.comment,name='comment'),
    path('searchFilter/',views.searchFilter,name='searchFilter'),
    path('filter/',views.filter,name='filter'),
]