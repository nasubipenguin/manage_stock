from django.urls import path
from . import views

urlpatterns = [
    path('', views.stock_list, name='stock_list'),
    path('list/', views.stock_list, name='stock_list'),
    path('new/', views.stock_new, name='stock_new'),
    path('<int:stock_code>/', views.stock_info, name='stock_info'),
    path('<int:stock_code>/edit/', views.stock_edit, name='stock_edit'),
    path('<int:stock_code>/detail/', views.stock_detail, name='stock_detail'),
    path('<int:stock_code>/delete/', views.stock_delete, name='stock_delete'),
    path('<int:stock_code>/performance/new/', views.performance_new, name='performance_new'),
    path('<int:stock_code>/performance/all/', views.performance_all, name='performance_all'),
    path('<int:stock_code>/performance/<int:source>/<int:pub_year>/<int:pub_month>/<int:target_period>/', views.performance_info, name='performance_info'),
    path('<int:stock_code>/performance/<int:source>/<int:pub_year>/<int:pub_month>/<int:target_period>/edit/', views.performance_edit, name='performance_edit'),
    path('<int:stock_code>/performance/<int:source>/<int:pub_year>/<int:pub_month>/<int:target_period>/delete/', views.performance_delete, name='performance_delete'),
    path('<int:stock_code>/shikiho/new/', views.shikiho_new, name='shikiho_new'),
    path('<int:stock_code>/shikiho/all/', views.shikiho_all, name='shikiho_all'),
    path('<int:stock_code>/shikiho/<int:pub_year>/<int:pub_month>/', views.shikiho_info, name='shikiho_info'),
    path('<int:stock_code>/shikiho/<int:pub_year>/<int:pub_month>/edit/', views.shikiho_edit, name='shikiho_edit'),
    path('<int:stock_code>/shikiho/<int:pub_year>/<int:pub_month>/delete/', views.shikiho_delete, name='shikiho_delete'),
    path('<int:stock_code>/note/new/', views.note_new, name='note_new'),
    path('<int:stock_code>/note/all/', views.note_all, name='note_all'),
    path('<int:stock_code>/note/<int:id>/', views.note_info, name='note_info'),
    path('<int:stock_code>/note/<int:id>/edit/', views.note_edit, name='note_edit'),
    path('<int:stock_code>/note/<int:id>/delete/', views.note_delete,
         name='note_delete'),
]
