import json
from django.conf import settings
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
import redis

# when to use POST, PUT:
# https://stackoverflow.com/questions/630453/what-is-the-difference-between-post-and-put-in-http

# Connect to our Redis instance
redis_instance = redis.StrictRedis(
    host=settings.REDISHOST, port=settings.REDISPORT, db=0
)

@api_view(["GET", "POST"])
def manage_items(request, *args, **kwargs):
    response = {
        'count': 0,
        'msg': "Not found",
        'items': None,
    }
    if request.method == 'GET':
        items = {}
        count = 0
        for key in redis_instance.keys("*"):
            items[key.decode("utf-8")] = redis_instance.get(key)
            count += 1
        response = {
            'count': count,
            'msg': f"Found {count} items.",
            'items': items
        }
        return Response(response, status=200)

    if request.method == 'POST':
        item = json.loads(request.body)
        key = list(item.keys())[0]
        value = item[key]
        redis_instance.set(key, value)
        response["msg"] = f"{key} set to {value}"
        return Response(response, 201)

    response = {
        "msg": f"{mehtod {request.method} not allowed"
    }
    return Response(response, 404)

@api_view(["GET", "POST", "PUT", "DELETE"])
def manage_item(request, *args, **kwargs):
    response = {
        "key": None
        "value": None,
        "msg": "Not found"
    }
    if request.method == "GET":
        if kwargs["key"]:
            key = kwargs["key"]
            response["key"] = key
            value = redis_instance.get(key)
            if value:
                response = {
                    "key": key,
                    "value": value,
                    "msg": "success",
                }
                return Response(response, status=200)
        return Response(response, status=404)

    if request.method == "POST":
        if kwargs["key"]:
            key = kwargs["key"]
            response["key"] = key
            rdata = json.loads(request.body)
            value = rdata["value"]
            prev = redis_instance.get(key)
            if value:
                redis_instance.set(key, value)
                if prev:
                    response["value"] = prev
                    response["msg"] = f"update {key}"
                    return Response(response, status=200)
                else:
                    response["value"] = value
                    response["msg"] = f"create {key}"
                    return Response(response, status=201)
        return Response(response, status=404)

    if request.method == "PUT":
        if kwargs["key"]:
            key = kwargs["key"]
            response["key"] = key
            rdata = json.loads(request.body)
            value = rdata["value"]
            prev = redis_instance.get(key)
            if value is not None:
                redis_instance.set(key, value)
                if prev:
                    response["value"] = prev
                    response["msg"] = f"update {key}"
                    return Response(response, status=200)
                else:
                    response["value"] = value
                    response["msg"] = f"create {key}"
                    return Response(response, status=201)
        return Response(response, status=404)

    if request.method == "DELETE":
        if kwargs["key"]:
            key = kwargs['key']:
            response["key"] = key
            result = redis_instance.delete(key)
            if 1 == result:
                response["msg"] = f"{key} deleted"
                return Response(response, status=200)
            return Response(response, status=404)
        return Response(response, status=404)

