from django.shortcuts import render
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

# Create your views here.
def delete_user(request):
    user = request.user
    user.delete()
    return JsonResponse({"message", "user deleted"})