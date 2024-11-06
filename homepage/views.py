from django.shortcuts import render

navbarContext = {
    'nav_links':{
        'home': {
            'title': 'Home',
            'link': '/',
            'icon': 'fa-regular fa-house',
        },
        'about': {
            'title': 'About',
            'link': '/about',
            'icon': 'fa-regular fa-user',
        },
        'resume': {
            'title': 'Resume',
            'link': '/resume',
            'icon': 'fa-regular fa-paperclip',
        },
        'contact': {
            'title': 'Contact',
            'link': '/contact',
            'icon': 'fa-regular fa-phone',
        },
    }
}

# Create your views here.
def home(request):
    return render(request, 'base.html', navbarContext)