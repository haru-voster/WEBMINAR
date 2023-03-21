from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import loader
from .models import HW

# Create your views her
def main(request):
    ac=HW.objects.all()
    template=loader.get_template('voster/index.html ')
    context={
        'ac':ac,
    }
    return HttpResponse(template.render(context, request))
def detail(request, couse_id):
    try:
        main=HW.objects.get(pk=couse_id)
    except HW.DoesNotExist:
        raise Http404 ("SUCH HARDWARE NOT FOUND TRY AGAIN LATER")
    return render(request, 'voster/tool.html',{'tool':HW})