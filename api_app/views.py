from django.views import View
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

import json
from .models import DogsModel, SomeKeys
from utils import dog_api_helpers, key_helpers
from secrets import randbelow


class DogInfo(APIView):
    def post(self, request):
        # save 24 random dogs to database instead of user input
        dog_list = dog_api_helpers.save_dog_pics_to_database()
        message = "Added the following images: "

        for dog in dog_list:
            message += dog.imgsrc + " | "

        return Response(message)

    def get(self, request):
        # get two random dogs for page
        image_list = dog_api_helpers.get_two_random_dogs()

        data = {
            'items': image_list,
        }

        return JsonResponse(data)


@method_decorator(csrf_exempt, name='dispatch')
class KeyInfo(View):
    def post(self, request):
        data = json.loads(request.body.decode("utf-8"))
        k_default_value = randbelow(90000)
        k_name = data.get('name')

        key_data = {
            'default_value': k_default_value,
            'name': k_name,
        }

        key_item = SomeKeys.objects.create(**key_data)

        data = {
            "message": f"New key entry added with id: {key_item.id}"
        }
        return JsonResponse(data, status=201)

    def get(self, request):
        items_count = SomeKeys.objects.count()
        items = SomeKeys.objects.all()

        items_data = []
        for item in items:
            items_data.append({
                'default_value': item.default_value,
                'name': item.name,
            })

        data = {
            'items': items_data,
            'count': items_count,
        }

        return JsonResponse(data)


class IncrementKeys(View):
    def get(self, request, value):
        # should probably be a PUT
        message = key_helpers.increment_key(request, value)

        data = {
            "message": message
        }
        return JsonResponse(data, status=201)


def blank_page(request):
    return HttpResponse("There's nothing here...")
