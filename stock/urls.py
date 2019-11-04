from django.urls import path
from . import views

urlpatterns = [
    path('', views.stock_list, name='stock_list'),
    path('list/', views.stock_list, name='stock_list'),
    path('new/', views.stock_new, name='stock_new'),
    path('<int:stock_code>/', views.stock_info, name='stock_info'),
    path('<int:stock_code>/edit/', views.stock_edit, name='stock_edit'),
    path('<int:stock_code>/detail/', views.stock_detail, name='stock_detail'),
    path('<int:stock_code>/performance/new/', views.performance_new, name='performance_new'),
    path('<int:stock_code>/performance/<int:pk>/', views.performance_info, name='performance_info'),
    path('<int:stock_code>/performance/<int:pk>/edit/', views.performance_edit, name='performance_edit'),
    path('<int:stock_code>/shikiho/new/', views.shikiho_new, name='shikiho_new'),
    path('<int:stock_code>/shikiho/<int:pub_year>/<int:pub_month>/', views.shikiho_info, name='shikiho_info'),
    path('<int:stock_code>/shikiho/<int:pub_year>/<int:pub_month>/edit/', views.shikiho_edit, name='shikiho_edit'),
]
