from django.shortcuts import render


def main(request):
    return render(request, 'base.html')


def train(request):
    return render(request, 'train.html')