from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.shortcuts import render
from .forms import SignUpForm,ProfileForm
from .models import User_Profile

def db_view(request):
    user = request.user
    
    profiles = User_Profile.objects.filter(username = user)
    return render(request,'registration/index.html', {
        'profiles':profiles,
    })
    

#サインアップ
class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
    
    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_active = True
        user.save()
        return super().form_valid(form)

