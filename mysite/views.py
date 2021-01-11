from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def main(request):
    return render(request, 'base.html')


@login_required
def train(request, train_type):
    return render(request, 'train.html', {'train_type': train_type})
