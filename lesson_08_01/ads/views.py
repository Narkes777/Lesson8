import imp
from django.http import HttpResponse, HttpRequest
from django.template import loader
from .models import Ad
from django.views.generic.edit import CreateView
from .forms import AdForm


# Create your views here.

def search_by_name(request: HttpRequest, name: str) -> HttpResponse:
    ad = Ad.objects.get(name=name)
    return HttpResponse(ad.name)


class AdCreateView(CreateView):
    form_class = AdForm
    template_name = 'ad_form.html'
    success_url = '/app/'


def index(request: HttpRequest, pk: int) -> HttpResponse:
    try:
        ad = Ad.objects.get(pk=pk)
    except Ad.DoesNotExist:
        return HttpResponse('Not found')
    template = loader.get_template('index.html')
    context = {"ad": ad}
    return HttpResponse(template.render(context, request))


def ad_list(request: HttpRequest) -> HttpResponse:
    ads = Ad.objects.all()
    template = loader.get_template('ad_list.html')
    context = {"ads": ads}
    return HttpResponse(template.render(context, request))


    # result = "Объявления:\n\n"
    # for ad in Ad.objects.all():
    #     result += str(ad.name) + ' ' + str(ad.content) + ' ' + str(ad.price) + '\n'
    # return HttpResponse(result, content_type="text/plain; charset=utf-8")



