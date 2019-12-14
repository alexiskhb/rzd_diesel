from django.views.generic import View
from django.http import HttpResponse
from django.core.handlers.wsgi import WSGIRequest
import json

from .cache import DG


class MyView(View):
    def get(self, request: WSGIRequest, *args, **kwargs):
        loco_id = int(''.join([c for c in request.GET.get('train') if c.isdigit()]))
        request = {
            'train': loco_id,
            'from_time': int(request.GET.get('from_time')),
            'to_time': int(request.GET.get('to_time')),
        }
        data_dict = DG.get(request)
        return HttpResponse(json.dumps(data_dict))
