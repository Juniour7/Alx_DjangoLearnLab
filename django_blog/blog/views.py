from django.shortcuts import render, redirect
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import RegisterForm, PostForm, ProfileUpdateForm, UserUpdateForm
from .models import Post



# Views for user and profile management

# -----------ENDPOINT FOR THE HOMEPAGE-----------------

def home_view(request):
    return render(request, 'base.html')

# -----------VIEW TO HANDLE SIGNUPS TO THE APP-----------------

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile')
    
    else:
        form = RegisterForm()

    return render(request, 'blog/register.html', {'form': form})

# -----------VIEW TO HANDLE LOGIN TO THE APP-----------------

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('profile')
    else:
        form = AuthenticationForm()
    return render(request, 'blog/login.html', {'form': form})


# -----------VIEW TO HANDLE logout FROM THE APP-----------------


def logout_view(request):
    logout(request)
    return render(request, 'blog/logout.html')


# -----------ENPOINT FOR USER PROFILE-----------------
@login_required
def profile_view(request):
    user = request.user

    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('profile')  # refresh page after saving
    else:
        u_form = UserUpdateForm(instance=user)
        p_form = ProfileUpdateForm(instance=user.profile)

    return render(request, 'blog/profile.html', {
        'u_form': u_form,
        'p_form': p_form
    })

# View for Blog Post managements

# --------CREATE A NEW BLOG---------

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'  # templates/blog/post_form.html
    # redirect to login if unauthenticated
    login_url = 'login'

    def form_valid(self, form):
        # Automatically set the author to the logged-in user before saving
        form.instance.author = self.request.user
        return super().form_valid(form)
    

# --------LISTVIEW TO LIST ALL AVAILABLE BLOGS---------

class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'  # templates/blog/post_list.html
    context_object_name = 'posts'
    paginate_by = 10


# --------DETAILVIEW TO VIEW DETAILS OF PARTICULAR BLOG---------

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'  # templates/blog/post_detail.html
    context_object_name = 'post'


# --------UPDATE ENDPOINT FOR BLOGS---------

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'
    login_url = 'login'

    def test_func(self):
        post = self.get_object()
        return post.author == self.request.user  # only author allowed


# --------DELETE VIEW FOR A PARTICULAR BLOG---------

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'  # templates/blog/post_confirm_delete.html
    success_url = reverse_lazy('post-list')
    login_url = 'login'

    def test_func(self):
        post = self.get_object()
        return post.author == self.request.user  # only author allowed