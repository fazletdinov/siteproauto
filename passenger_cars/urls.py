from django.urls import path
from .views import *

urlpatterns = [
    path('', IndexListView.as_view(), name='home'),
    path('detail/<slug:detail_slug>/', ShowPost.as_view(), name='detail'),
    path('category/<slug:cat_slug>/', AutoCategory.as_view(), name='category'),
    path('create/', create, name='create'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),
]