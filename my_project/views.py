from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def post(request):
	content = request.body.decode()
	response = json.loads(content)
	return HttpResponse(response['key'])
