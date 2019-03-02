from django.urls import path
from .import views

urlpatterns =[
    path('',views.login_page, name='login_page'),
    path('guest/',views.guest, name='guest'),
    path('Willy/',views.Willy, name='Willy'),
    path('Jose/',views.Jose, name='Jose'),
    path('Rony/',views.Rony, name='Rony'),
    path('Jeny/',views.Jeny, name='Jeny'),
    path('Elsamma/',views.Elsamma, name='Elsamma'),
    path('familyphotos/',views.familyphotos, name='familyphotos'),
    path('addImage/',views.addImage, name='addImage'),
    path('back/<int:pageno>/',views.back, name='back'),
    path('signup_page/',views.signup_page,name='signup_page'),
]