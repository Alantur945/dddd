from django.shortcuts import render


def main_page(request):
    return render(request, 'fourth_task/main.html', {'pagename': 'Главная страница'})


def shop_page(request):
    items = {'item1': 'Носки', 'item2': 'Трусы', 'item3': 'Майка'}
    return render(request, 'fourth_task/shop.html', {'pagename': 'Магазин', 'items': items})


def cart_page(request):
    return render(request, 'fourth_task/cart.html', {'pagename': 'Корзина'})


