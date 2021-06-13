from django.urls import path
from app6.views import SignIn, Singup, HomePage, Home, Dashboard, Profile,Viewprofile,Disprofile_data, loginlog, complaint,Viewcomplaint,Discomplaint_data, Notice,Viewnotice,Disnotice_data, Forget, Otp, newpassword, Admindash, Admindashboard

urlpatterns = [
    # path('index/', Index),
    path('SignIn/', SignIn,name='sign'),
    path('Signup/', Singup,name='signup'),
    path('Home/', Home,name='home'),

    path('Forget/', Forget,name='forget'),
    path('Otp/', Otp,name='Otp'),
    path('newpassword/', newpassword,name='newpassword'),

    path('Admindashboard/', Admindashboard,name='admindashboard'),
    path('Admindash/', Admindash,name='admindash'),

    path('complaint/', complaint,name='complaint'),
    path('Viewcomplaint/', Viewcomplaint,name='viewcomplaint'),
    path('Discomplaint_data/',Discomplaint_data,name='discomplaint_data'),

    path('loginlog/', loginlog,name='loginlog'),

    path('Viewnotice/', Viewnotice,name='viewnotice'),
    path('Notice/', Notice,name='notice'),
    path('Disnotice_data/',Disnotice_data,name='disnotice_data'),

    path('Profile/', Profile,name='profile'),
    path('Viewprofile/', Viewprofile,name='viewprofile'),
    path('Disprofile_data/',Disprofile_data,name='disprofile_data'),

    path('HomePage/',HomePage,name='homepage'),
    path('Dashboard/', Dashboard,name='dashboard'),

]