from django.urls import path
from .views import *

urlpatterns = [

    path('reg', reg_view),
    path('login', login_view),
    path('logout', logout_view)

]
