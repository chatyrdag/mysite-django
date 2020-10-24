from django.shortcuts import render


def main(request):
    return render(request, 'index.html')


def rp(request):
    return render(request, 'rp.html')
