from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
import datetime as dt
from .models import Editor, Category, Image


# Create your views here.
def welcome(request):
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")

def todays_images(request):
    date = dt.date.today()
    images = Image.todays_images()
    # FUNCTION TO CONVERT DATE OBJECT TO FIND EXACT DAY
    # day = convert_dates(date)
    return render(request, 'today-images.html', {"date": date, "images": images})

def convert_dates(dates):

    # Function that gets the weekday number for the date.
    day_number = dt.date.weekday(dates)

    days = ['Monday', 'Tuesday', 'Wednesday',
            'Thursday', 'Friday', 'Saturday', "Sunday"]

    # Returning the actual day of the week
    day = days[day_number]
    return day


def past_days_images(request, past_date):
    #Converts data from the string to url
    try:

        date = dt.datetime.strptime(past_date, '%Y-%m-%d').date()

    except ValueError:
         # Raise 404 error when ValueError is thrown
        raise Http404()
        assert False

    day = convert_dates(date)
    if date == dt.date.today():
        return redirect(todays_images)

    images = Image.days_images(date)
    return render(request, 'past-images.html', {"date": date, "images": images})


def search_results(request):

    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_images = Image.search_by_title(search_term)
        image = Image.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'search.html', {"message": message, "images": searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html', {"message": message})


def image(request, image_id):
    try:
        image = Image.objects.get(id=image)
    except DoesNotExist:
        raise Http404()
    return render(request, "image.html", {"image": image})
