from django.urls import path
from . import views
app_name='buyer'
urlpatterns = [
   path('buyer_register',views.buyer_register,name='buyer_register'),
   path('buyer_login/',views.buyer_login,name='buyer_login'),
   path('show_all_products/<int:id>',views.show_all_products,name='show_all_products'),    
   path('show_profile/<int:id>',views.show_profile,name='show_profile'),    
   path('buyer_dashboard/<int:id>',views.buyer_dashboard,name='buyer_dashboard'),    
   path('buyer_update/<int:id>',views.buyer_update,name='buyer_update'),
   path('buyer_changepassword/<int:id>',views.buyer_changepassword,name='buyer_changepassword'),
   path('buyer_logout',views.buyer_logout,name='buyer_logout'),
   path('buyer_delete/<int:id>',views.buyer_delete,name='buyer_delete'),
   path('readcategory/<int:id>/<int:uid>',views.readcategory,name='readcategory'),
   path('show_productdetail/<int:userid>/<int:proid>',views.show_productdetail,name='show_productdetail'),


   path('add_to_wishlist/<int:uid>/<int:pid>',views.add_to_wishlist,name='add_to_wishlist'),
   path('wishlist/<int:id>',views.wishlist,name='wishlist'),
   path('b_feedback/<int:id>',views.b_feedback,name='b_feedback'),





]