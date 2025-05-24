from django.shortcuts import render
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
import random
from .models import User

def user_list(request):
    users = User.objects.all().order_by('id')  # Добавлено order_by
    paginator = Paginator(users, 20)  # 20 пользователей на страницу
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'users/list.html', {'page_obj': page_obj})

def user_detail(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    return render(request, 'users/detail.html', {'user': user})

def random_user(request):
    random_id = random.choice(User.objects.values_list('id', flat=True))
    return user_detail(request, random_id)
