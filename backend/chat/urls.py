from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views

# указываем по каким адресам использовать наши методы реализации полученных данных
# для защиты от просмотра страниц незарегестрированных пользователей оборачиваем методы в метод login_required, в котором указываем адрес перенаправления в случае попытки доступа к странице
check_email = views.PasswordRecoveryViewSet.as_view({
    'post': 'check_email'
})
check_key = views.PasswordRecoveryViewSet.as_view({
    'post': 'check_key'
})
password_recovery = views.PasswordRecoveryViewSet.as_view({
    'post': 'password_recovery'
})

urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register_user_url'),

    path('base/<str:pk>/', views.BaseViewPerson.as_view(), name='base_url'),
    path('filter/', views.UsersListView.as_view(), name='filter_url'),

    path('password/email/', check_email, name='check-email'),
    path('password/key/', check_key, name='check-key'),
    path('password/recovery/', password_recovery, name='password-recovery')
]

