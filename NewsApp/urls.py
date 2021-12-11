from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('account/', views.accountSettings, name="account"),
    # path('customer/<str:pk_test>/', views.customer, name="customer"),
    path('register/', views.registerPage, name="register"),
	path('login/', views.loginPage, name="login"),
	path('logout/', views.logoutUser, name="logout"),

    path('general', views.general, name='general'),
    path('sports', views.sports, name='sports'),
    path('politics', views.politics, name='politics'),
    path('entertainment', views.entertainment, name='entertainment'),
    path('music', views.music, name='music'),
    path('technology', views.technology, name='technology'),
    path('science', views.science, name='science'),
    path('business', views.business, name='business'),
    path('health', views.health, name='health'),
    path('summarize_page', views.summarize_page, name='summarize_page'),

    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="NewsApp/password_reset.html"),
         name="reset_password"),
    path('reset_password_sent/',
         auth_views.PasswordResetDoneView.as_view(template_name="NewsApp/password_reset_sent.html"),
         name="password_reset_done"),
    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name="NewsApp/password_reset_form.html"),
         name="password_reset_confirm"),
    path('reset_password_complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name="NewsApp/password_reset_done.html"),
         name="password_reset_complete"),
]