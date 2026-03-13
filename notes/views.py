from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .models import Note # تأكد إن السطر ده موجود عشان نستخدم قاعدة البيانات

# 1. دالة إنشاء حساب جديد
def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user) # تسجيل دخول تلقائي بعد التسجيل
            return redirect('dashboard')
    else:
        form = UserCreationForm()
    return render(request, 'notes/signup.html', {'form': form})

# 2. دالة لوحة التحكم (إضافة وعرض الملاحظات)
@login_required
def dashboard(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        # بنحفظ الملحوظة ونربطها بالمستخدم اللي فاتح الحساب حالياً
        Note.objects.create(user=request.user, title=title, content=content)
        return redirect('dashboard')

    # بنجيب الملاحظات اللي تخص المستخدم ده "فقط" عشان الخصوصية
    user_notes = Note.objects.filter(user=request.user)
    return render(request, 'notes/dashboard.html', {'notes': user_notes})
def delete_note(request, note_id):
    # بنجيب الملحوظة بشرط تكون تخص المستخدم اللي فاتح بس (عشان السكيوريتي)
    note = Note.objects.get(id=note_id, user=request.user)
    note.delete()
    return redirect('dashboard')