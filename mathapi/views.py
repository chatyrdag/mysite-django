from django.shortcuts import render
from django.http import JsonResponse
from random import randint
from .functions.lineareq import make_lineareq
from . functions.squareroot import make_squareroot_task


def multtab(request):
    if request.method == 'OPTIONS':
        response = JsonResponse('', status=200)
        response['Access-Control-Allow-Origin'] = '*'
        response['Access-Control-Allow-Headers'] = 'X-API-KEY, Origin, X-Requested-With, Content-Type, Accept, Access-Control-Request-Method, Access-Control-Request-Headers, Authorization'
    elif request.method == 'GET':
        first_number, second_number = randint(2, 9), randint(2, 9)
        ans = first_number * second_number
        problem_text = f"{first_number} \\times {second_number}"
        response_text = {'problemText': problem_text, 'answer': ans}
        response = JsonResponse(response_text, status=201)
        response['Access-Control-Allow-Origin'] = '*'
        response['Access-Control-Allow-Methods'] = 'GET, OPTIONS'
        response['Access-Control-Allow-Headers'] = 'Origin, X-Requested-With, Content-Type, Accept'

    return response


def lineareq(request, level):
    if request.method == 'OPTIONS':
        response = JsonResponse('', status=200)
        response['Access-Control-Allow-Origin'] = '*'
        response['Access-Control-Allow-Headers'] = 'X-API-KEY, Origin, X-Requested-With, Content-Type, Accept, Access-Control-Request-Method, Access-Control-Request-Headers, Authorization'
    elif request.method == 'GET':
        problem_text, ans = make_lineareq(level)
        response_text = {'problemText': problem_text, 'answer': ans}
        response = JsonResponse(response_text, status=201)
        response['Access-Control-Allow-Origin'] = '*'
        response['Access-Control-Allow-Methods'] = 'GET, OPTIONS'
        response['Access-Control-Allow-Headers'] = 'Origin, X-Requested-With, Content-Type, Accept'

    return response


def squareroot(request, level):
    if request.method == 'OPTIONS':
        response = JsonResponse('', status=200)
        response['Access-Control-Allow-Origin'] = '*'
        response['Access-Control-Allow-Headers'] = 'X-API-KEY, Origin, X-Requested-With, Content-Type, Accept, Access-Control-Request-Method, Access-Control-Request-Headers, Authorization'
    elif request.method == 'GET':
        problem_text, ans = make_squareroot_task(level)
        response_text = {'problemText': problem_text, 'answer': ans}
        response = JsonResponse(response_text, status=201)
        response['Access-Control-Allow-Origin'] = '*'
        response['Access-Control-Allow-Methods'] = 'GET, OPTIONS'
        response['Access-Control-Allow-Headers'] = 'Origin, X-Requested-With, Content-Type, Accept'

    return response
