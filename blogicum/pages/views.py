from django.shortcuts import render

# Create your views here.
def about(request):
    template_name = 'about.html'
    return render(request, template_name)

def rules(request):
    template_name = 'rules.html'
    return render(request, template_name)