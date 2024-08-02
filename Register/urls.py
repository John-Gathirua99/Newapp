from django.urls import path
from . import views

from django.contrib.auth import views as auth_views
urlpatterns = [
    path('',views.home,name = 'home'),
    path('register/',views.register,name = 'register'),
    # path('login/',views.loginpage,name = 'login'),
    path('logout/',views.logoutpage,name = 'logout'),
    path('profile/',views.profile,name = 'profile'),
    # password change,
    path('password-change/',auth_views.PasswordChangeView.as_view(),name='password_change'),
    path('password-change-done/',auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('password-reset/',
         auth_views.PasswordResetView.as_view(template_name = 'Register/password_reset.html'),
         name='reset_password'
         ),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(template_name = 'Register/password_reset_done.html'),
         name='password_reset_done'
         ),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name = 'Register/password_reset_confirm.html'),
         name='password_reset_confirm'
         ),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(),
         name='password_reset_complete'
         )
]
