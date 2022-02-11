from django.http import HttpResponse

class HealthCheck:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path == "/health":
            return HttpResponse("ok")
        else:
            return self.get_request(request)

