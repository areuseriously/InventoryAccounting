from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from inventory.models import Item
from .models import UserProfile
from .forms import LoginForm, UserRegistrationForm
import xlwt
from urllib.parse import quote


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('item_list')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'accounts/login.html', {'form': form})


@login_required
def profile(request):
    user_profile = UserProfile.objects.get(user=request.user)
    return render(request, 'account/profile.html', {'section': 'profile', 'user_profile': user_profile})


def register_request(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            department = form.cleaned_data['department']
            position = form.cleaned_data['position']

            form.save()
            user_model = UserProfile(user.id)
            user_model.user = user
            user_model.department = department
            user_model.position = position

            user_model.save()

            return redirect('profile')
        else:
            return render(request, 'registration/registration.html', {'form': form})
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/registration.html', {'form': form})


def users_list(request):
    users = User.objects.all().order_by('last_name')
    return render(request, 'users_list.html', {'users': users})


def user_detail(request, user_id):
    user = get_object_or_404(User, id=user_id)
    user_profile = UserProfile.objects.get(pk=user_id)
    user_inventory = Item.objects.filter(owner=user).order_by('system')
    return render(request, 'user_detail.html',
                  {'user': user, 'user_profile': user_profile, 'user_inventory': user_inventory})


def download_user_items(request, user_id):
    user = get_object_or_404(User, id=user_id)
    items = Item.objects.filter(owner=user).order_by('system')

    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = f'attachment; filename="{quote(user.last_name)}_items.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Список ТМЦ')

    row_num = 0
    columns = ['Система', 'Наименование', 'Количество', 'Расположение']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], xlwt.easyxf('font: bold on'))

    font_style = xlwt.XFStyle()

    for item in items:
        row_num += 1
        row = [item.system, item.name, item.quantity, item.placement]
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response



