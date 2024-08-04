from django.urls import path
# from django.contrib import admin
from . import views


urlpatterns=[
    # path("home/",views.inputField),
    path("index",views.index, name='index'),
    path("sign-up",views.UserSignUp, name='sign-up'),
    path("add_student",views.add_student, name='add_student'),
    path("all_student",views.all_student, name='all_student'),
    path("add_item",views.add_item, name='add_item'),
    path("all_item",views.all_item, name='all_item'),
    path("payment_item/<item>",views.payment_item, name='payment_item'),
    path("student_item/<studID>",views.student_item, name='student_item'),
    # path("logout",views.logout, name='logout')

]
   