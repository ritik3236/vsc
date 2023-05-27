from django.views.generic import TemplateView
from django.http import JsonResponse
from django.core import serializers
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Count

from api.models import *
from api.forms import *

import random

# Create your views here.

def quote_record(request):
    image_url = []
    q = list(QuotesApi.objects.all())
    rq = random.sample(q, 4) if len(q) > 4 else q
    for i in rq:
        try:
            image_url.append(i.author_img.url)
        except Exception as e:
            image_url.append('img not found')
    randomized_quote = serializers.serialize('json', rq)
    context = {
        'data': randomized_quote,
        'image_url': image_url
    }
    return JsonResponse(
        {'context': context}, status=200
    )

@method_decorator(csrf_exempt, name = 'dispatch')
class TestView(TemplateView):
    
    template_name = 'upload.html'
    
    def get(self, request, *args, **kwargs):

        contributors = FileUpload.objects.values("name").annotate(count = Count("name")).order_by("-count")[:20]
        context = {'form': TestForm(), 'contributors': contributors}
        return render(request, self.template_name, context)
    
    def post(self, request, *args, **kwargs):
        count = 0
        upload_result = ''

        form = TestForm(request.POST, request.FILES)
        files = request.FILES.getlist('document')
        if form.is_valid():
            for file in files:
                file_upload = FileUpload()
                file_upload.name = form.cleaned_data['name']
                file_upload.email = form.cleaned_data['email']
                file_upload.type = form.cleaned_data['type']
                file_upload.document = file
                file_upload.description = form.cleaned_data['description']
                file_upload.save()
                count = count + 1
            upload_result = "Upload Successful"
            data = {"is_valid": True, "count": count, "upload_result": upload_result}
        else:
            data = {"is_valid": False, "count": count, "upload_result": upload_result}
        return JsonResponse(data)
