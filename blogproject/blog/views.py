from django.shortcuts import render
from models import blog
# Create your views here.

def blog_list(request):
    blog = blog.objects.all()
    return render(request, 'blog/blog_list.html', {'blog': blog})

def blog_detail(request, pk):
    blog = blog.objects.get(pk=pk)
    return render(request, 'blog/blog_detail.html', {'blog': blog})

def blog_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        new_blog = blog.objects.create(title=title, content=content)
        return redirect('blog_detail', pk=new_blog.pk)
    return render(request, 'blog/blog_form.html')

def blog_update(request, pk):
    blog = blog.objects.get(pk=pk)
    if request.method == 'POST':
        blog.title = request.POST.get('title')
        blog.content = request.POST.get('content')
        blog.save()
        return redirect('blog_detail', pk=blog.pk)
    return render(request, 'blog/blog_form.html', {'blog': blog})