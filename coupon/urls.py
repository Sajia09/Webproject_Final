from django.urls import path
from .views import Index,signup,Login,home,pay,download,loginhome,purchase

urlpatterns = [
    path('', home, name='home-page'),
    path('home', loginhome, name='login-home'),
    path('signup', signup, name='signup'),
    # path('purchase', Index.as_view(), name='purchase-page'),
    path('buy',Index.as_view() ,name='buy'),
    path('login', Login.as_view(), name='login'),
    path('pay', pay, name='payment'),
    path('download',download , name='download'),
]
