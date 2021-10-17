from django.conf.urls import url

from stock.views import stock_list


urlpatterns = [
    url('list/', stock_list)
]
