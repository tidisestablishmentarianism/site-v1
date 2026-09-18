from django.http import HttpRequest, HttpResponse

def my_page(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Hello World")
