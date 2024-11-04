from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('menu/', views.menu, name='menu'),
    path('menu/<int:pk>', views.display_menu_item, name="menu_item"),
    path('book', views.book, name='book'),
    path('bookings', views.bookings, name='bookings'),
    path('reservations', views.reservations, name="reservations"),
    path('booking', views.BookingItemView.as_view(), name='booking'),
    path('menu/admin/<int:pk>', views.SingleMenuItemView.as_view()),
    path('menu/admin/bookings/<int:pk>', views.BookingItemView.as_view()),
    path('api-token-auth/', obtain_auth_token),
]