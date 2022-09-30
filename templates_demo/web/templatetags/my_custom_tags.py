from django.template import Library

from templates_demo.web.views import Student

register = Library()


# Put name="....."
@register.simple_tag(name='student_info')
def show_student_info(student: Student):
    return f'Hi, my name is {student.name} and I am {student.age} years old'


@register.inclusion_tag('tags/nav.html', name='my_nav')
def generate_nav_elements(*args_of_urls):
    context = {
        'url_names': args_of_urls,
    }

    return context
