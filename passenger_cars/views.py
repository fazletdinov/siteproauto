from django.contrib.auth import logout, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from django.urls import reverse_lazy
from .models import *
from .forms import *
from django.views.generic import ListView, CreateView, DetailView

class IndexListView(ListView):
    paginate_by = 3
    model = Auto
    template_name = 'passenger_cars/index.html'

class ShowPost(DetailView):
    model = Auto
    template_name = 'passenger_cars/detail.html'
    slug_url_kwarg = 'detail_slug'
    context_object_name = 'data'


#def detail(request, detail_slug):
#    data = get_object_or_404(Auto, slug=detail_slug)
#    return render(request, 'passenger_cars/detail.html', {'data': data})

class AutoCategory(ListView):
    model = Auto
    template_name = 'passenger_cars/index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_queryset(self):
        return Auto.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True)



def create(request):
    if request.method == "post":
        form = AddPostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AddPostForm()
    return render(request, 'passenger_cars/add_auto.html', {'form': form})

class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'passenger_cars/register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class LoginUser(LoginView):
    form_class = LogonUserForm
    template_name = 'passenger_cars/login.html'

    def get_success_url(self):
        return reverse_lazy('home')

def logout_user(request):
    logout(request)
    return redirect('login')