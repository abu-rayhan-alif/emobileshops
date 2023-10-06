from django.urls import path
from shop import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .forms import LoginFrom,MyPasswordChangeForm,MyPasswordResetForm , MySetPasswordForm

urlpatterns=[
    
    path('',views.home_page,name="home"),
    path('shoppage/',views.ShopPageView.as_view(),name="shoppage"),
    #path('category/',views.BrandCategoryView.as_view(),name="category"),
    #path('category/',views.CategoryView.as_view(),name="category"),
    path('brandcategory/',views.BrandProductView.as_view(),name="brandcategory"),
    
    path('registration/',views.CustomerRegistrationView.as_view(),name='customerregistration'),
    path('accounts/login/',auth_views.LoginView.as_view(template_name='login.html',authentication_form=LoginFrom),name='login'),
    path('logout/',auth_views.LogoutView.as_view(next_page='login'),name='logout'),
    path('profile/', views.ProfileView.as_view() ,name='profile'),
    
    path('passwordchange/', auth_views.PasswordChangeView.as_view(template_name = 'passwordchange.html', form_class=MyPasswordChangeForm, success_url='/passwordchangedone/'), name='passwordchange'),
    path('passwordchangedone/', auth_views.PasswordChangeView.as_view(template_name = 'passwordchangedone.html'), name='passwordchangedone'),
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='password_reset.html', form_class=MyPasswordResetForm), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html', form_class=MySetPasswordForm), name='password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),
    
    path('checkout/', views.checkout, name='checkout'),
    
    path('address/', views.address, name='address'),
    path('add-to-cart/', views.add_to_cart, name='add-to-cart'),
    path('cart/', views.show_cart, name='showcart'),
    path('product-detail/<int:pk>', views.ProductDetailView.as_view(), name='product-detail'),
    path('pluscart/', views.plus_cart),
    path('minuscart/', views.minus_cart),
    path('removecart/', views.remove_cart),
    path('orders/', views.orders, name='orders'),
    path('paymentdone/', views.payment_done, name='paymentdone'),
    path('contact/', views.contact, name='contact'),
    path('brandviews/', views.brand_view, name='brandviews'),
    path('TopNewView/', views.TopNewView.as_view(), name='TopNew'),
    path('RecentlyTopViews/', views.RecentlyTopViewsView.as_view(), name='RecentlyTop'),
    path('TopSellerView/', views.TopSellerView.as_view(),name='TopSeller'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)