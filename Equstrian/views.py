from django.shortcuts import render

def main(request):
    data = {
        'title': 'Конный двор "Ветер в гриве"'
    }
    return render(request, 'main/main_page.html', data)


def about(request):
    return render(request, 'main/about_page.html')


def offer(request):
    return render(request, 'main/offer_page.html')


def contacts(request):
    return render(request, 'main/contacts.html')
