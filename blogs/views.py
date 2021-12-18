from django.shortcuts import render
from .models import CheckIn


# Create your views here.
def list_post(request):
    # data_post={"Post":Post.objects.all().order_by('-date')}
    data_post = {"CheckIn": CheckIn.objects.all()}
    return render(request, 'pages/testmodel.html', data_post)
