from django.shortcuts import redirect, render

from django.http import HttpResponseNotFound

from django.views import View

from . import models

# Create your views here.

# homepage view
class home(View):

    def get(self, request):
        datas = []
        try:
            # get all blogs order by date
            data = models.Blog.objects.all().order_by('-date')
            for item in data:
                datas.append({
                    'id': item.id,
                    'title': item.title,
                    'author': item.author,
                    'date': item.date
                })
        except:
            pass
        return render(request, 'index.html', {
            'datas': datas
        })

# aboutpage view
class about(View):

    def get(self, request):
        return render(request, 'about.html')

# contact page view
class contact(View):

    def get(self, request):
        return render(request, 'contact.html')

    # form submission
    def post(self, request):
        try:
            data = models.Contact()
            data.name = request.POST['name']
            data.email = request.POST['email']
            data.message = request.POST['message']
            data.save()
            return redirect('/')
        except:
            return redirect('/')

# particular blog page view
class blog_post(View):

    def get(self, request, id):
        try:
            # get blog details
            item = models.Blog.objects.get(id=id)
            data = {
                'title': item.title,
                'desc': item.desc,
                'author': item.author,
                'date': item.date
            }
            return render(request, 'post.html', {
                'data': data
            })
        except:
            return HttpResponseNotFound()