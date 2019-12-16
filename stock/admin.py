from django.contrib import admin

from django.contrib import admin
from .models import Stock
from .models import Performance
from .models import Shikiho

admin.site.register(Stock)
admin.site.register(Performance)
admin.site.register(Shikiho)