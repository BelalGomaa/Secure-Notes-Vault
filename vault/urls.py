from django.contrib import admin
from django.urls import path, include # لازم تتأكد إن include مكتوبة هنا

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('notes.urls')), # السطر ده هو اللي بيربط تطبيق الملاحظات بالموقع
]