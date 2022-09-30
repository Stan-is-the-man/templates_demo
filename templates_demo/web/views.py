import random
from datetime import datetime

from django.shortcuts import render, redirect


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_info(self):
        return f'Name:{self.name} is {self.age} years old'


def index(request):
    context = {
        'title': 'softUni Homepage',
        'value': random.random(),
        'info': {'address': 'Sofia'},
        'student': Student('Stanislav', 38),
        # the better syntax
        'student_info': Student('Doncho', 39).get_info(),
        'now': datetime.now(),
        'students': [
            'Yoshi',
            'Tate',
            'Tedi',
            'Mama',
        ],
        'cars': [
            'Honda',
            'Toyota',
            'Subaru'
        ],
        'numbers': list(range(20))

    }
    return render(request, 'index.html', context)


def redirect_to_home(request):
    return redirect('index')


def about(request):
   return render(request, 'about.html')