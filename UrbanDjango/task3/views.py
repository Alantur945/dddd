from django.shortcuts import render


def main_page(request):
    return render(request, 'third_task/main.html')


def shop_page(request):
    items = {
        'games': ['Atomic Heart', 'Cyberpunk 2077', 'The Witcher 3']
    }
    return render(request, 'third_task/shop.html', context=items)


def cart_page(request):
    return render(request, 'third_task/cart.html')
