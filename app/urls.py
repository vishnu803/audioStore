from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.upload, name='upload'),
    path('viewuploaded/', views.viewuploaded, name = 'viewuploaded'),
    # path('verifyUrl/<str:phoneNo>/<str:token>', views.verifyUrl, name='verifyUrl'),
    # path('generateUrl/<str:phoneNo>', views.generateUrl, name= 'generateUrl'),
    # path('createUser/<str:name>/<str:phoneNo>',views.createUser,name="createUser")
]