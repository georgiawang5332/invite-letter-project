from django.shortcuts import render

# Create your views here.
def calendar_view(request):
    templates_name = 'calendar/calendar.html'
    context = {
        'title': '日曆',
    }
    return render(request, templates_name, context)
