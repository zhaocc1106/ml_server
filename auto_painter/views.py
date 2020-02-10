from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.http import Http404
from django.views import generic
from .models import AutoPainter


def index(request):
    latest_auto_painter_list = AutoPainter.objects.all()
    context = {
        'latest_auto_painter_list': latest_auto_painter_list
    }
    return render(request, template_name='auto_painter/app_index.html',
                  context=context)


class IndexView(generic.ListView):
    template_name = 'auto_painter/app_index.html'
    context_object_name = 'latest_auto_painter_list'

    def get_queryset(self):
        return AutoPainter.objects.all()


def detail(request, auto_painter_id):
    # try:
    #     response = AutoPainter.objects.get(id=auto_painter_id)
    # except AutoPainter.DoesNotExist:
    #     raise Http404
    response = get_object_or_404(AutoPainter, pk=auto_painter_id)
    return HttpResponse(str(response))


class DetailView(generic.DetailView):
    model = AutoPainter
    # Default context object name is the model name. Default template view
    # name is the model_name_detail.html
    # context_object_name = 'autopainter'
    # template_name = 'auto_painter/autopainter_detail.html'
