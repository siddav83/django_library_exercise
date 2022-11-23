
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='library-home'), # route for /library/
    path('about/', views.about, name='library-about'), # route for /library/about
    # path('<id>/', views.show, name='library-show'), # route for /library/:id
    path('<int:id>/', views.show, name='library-show') # to accept only numbers as id param
]