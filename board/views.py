from django.shortcuts import render

# Create your views here.
class IndexCreateView(CreateView):
    model = Index
    template_name = ".html"
