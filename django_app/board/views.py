from django.shortcuts import render
from django.http import HttpResponse
from board.models import Board
# Create your views here.

def list(request):
    boardList = Board.objects.order_by()
    params = {{'boardList':boardList},}
    #return render(request, 'hello/index.html', params)
    return render(request, 'board/list.html', params)