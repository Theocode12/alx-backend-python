from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def delete_user(request):
    user = request.user
    user.delete()
    return JsonResponse({"message", "user deleted"})