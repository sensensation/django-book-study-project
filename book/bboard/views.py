from django.http import HttpResponse

from .models import Bb

def index(request):
   in_stock_list = 'Щебень оптом \r\n\r\n\r\n Доступное в продаже \n\r\n\r\n'
   for bb in Bb.objects.order_by('-published'):
      in_stock_list += bb.title + '\r\n' + bb.content + '\r\n\r\n'
      
   return HttpResponse(in_stock_list, content_type= 'text/plain; charset=utf-8')