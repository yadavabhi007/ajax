from django.shortcuts import render, HttpResponseRedirect
from .forms import StudentRegistration
from .models import User
from django.views.generic.base import TemplateView, RedirectView 
from django.views import View
from django.views.generic.list import ListView
# Create your views here.


class add_data(TemplateView):
    template_name = 'myapp/add.html'
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        fm = StudentRegistration()
        context = {'form':fm}
        return context
    def post(self, request):
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            fm.save()
            fm = StudentRegistration()
            return HttpResponseRedirect('/')
        return HttpResponseRedirect('/')


class update_data(View):
    def get(self, request, id):
        pi = User.objects.get(pk=id)
        fm = StudentRegistration(instance=pi)
        return render (request, 'myapp/update.html', {'form':fm})
    def post(self, request, id):
        pi = User.objects.get(pk=id)
        fm = StudentRegistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
        return render (request, 'myapp/update.html', {'form':fm})


class show_data(ListView):
    model = User
    template_name = 'myapp/show.html'
    context_object_name = 'st'
    paginate_by = 5
    student = User.objects.all().order_by('-id')
    context = {'st':student}  


class delete_data(RedirectView):
    url = '/show/'
    def get_redirect_url(self, *args, **kwargs):
        del_id = kwargs['id']
        User.objects.get(pk=del_id).delete()
        return super().get_redirect_url(*args, **kwargs)
        