from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import *
from .forms import ItemForm, CommentForm
import xlwt
from urllib.parse import quote

def item_list(request):
    items = Item.objects.filter(owner=request.user).order_by('system')
    context = {
        'items': items,
    }
    return render(request, 'item_list.html', context)


def item_detail(request, item_id):
    item = Item.objects.get(pk=item_id)

    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                body=form.cleaned_data['body'],
                item=item
            )
            comment.save()

    comments = Comment.objects.filter(item=item)
    context = {
        'item': item,
        'comments': comments,
        'form': form
    }
    return render(request, 'item_detail.html', context)


def item_create(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.owner = request.user
            item.save()
            return redirect('item_list')
    else:
        form = ItemForm()
    context = {
        'form': form,
    }
    return render(request, 'item_create.html', context)


def item_delete(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    item.delete()
    return redirect('item_list')


def item_edit(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('item_list')
    else:
        form = ItemForm(instance=item)
    context = {
        'form': form
    }
    return render(request, 'item_edit.html', context)


def download_items(request, user_id):
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
        row = [item.system, item.name, item.quantity, item.quantity]
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response
