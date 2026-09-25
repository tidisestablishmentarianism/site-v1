from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

# listaa=["abcd", 5, False, (128, 'dcba', {'0':4, '1':2147483647})]
context = {
    "username": "pneumonoultramicroscopicsilivolcanoconiosis",
    "age": 19,
    "location": ("Nowhere", "Antarctica"),
    "email": "pneumonoultramicroscopicsilivolcanoconiosis@example.com",
    "bio": {
        "username": "pneumonoultramicroscopicsilivolcanoconiosis",
        "age": 19,
        "location": ("Nowhere", "Antarctica"),
        "email": "pneumonoultramicroscopicsilivolcanoconiosis@example.com",
    },
}


def hello_world(request: HttpRequest) -> HttpResponse:
    return render(request, "index.html", context)
