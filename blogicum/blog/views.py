from django.shortcuts import render

# Create your views here.
def index(request):
    template_name = 'index.html'
    return render(request, template_name)

def post_detail(request):
    template_name = 'detail.html'
    return render(request, template_name)

def category_posts(request):
    template_name = 'category.html'
    return render(request, template_name)