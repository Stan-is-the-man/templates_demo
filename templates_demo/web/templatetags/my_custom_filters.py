# Custom filter making process
from django.template import Library

register = Library()



@register.filter('odd_only')
def find_odd_numbers(numbers):
    return [num for num in numbers if num % 2 != 0]


@register.filter('even_only')
def find_even_numbers(nums):
    return [x for x in nums if x % 2 == 0]


@register.filter('custom_date')
def custom_date_format(date):
    return date.strftime('%d-%m-%Y')
