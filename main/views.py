from django.shortcuts import render
from .models import Price

def index(request):
    return render(request, 'main/index.html')

def menu(request):
    # Получаем все цены из базы
    prices = Price.objects.all()
    
    # Создаем словарь
    price_dict = {}
    for price in prices:
        price_dict[price.item_name] = price.price
    
    # Для отладки (посмотри в консоль)
    print("="*50)
    print("Цены из БД:", price_dict)
    print("="*50)
    
    return render(request, 'main/menu.html', {'prices': price_dict})