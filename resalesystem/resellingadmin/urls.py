from django.urls import path
from . import views
app_name='resellingadmin'
urlpatterns=[
    path('adminlogin/',views.adminlogin,name='adminlogin'),

    path('adminloginhome/<int:id>',views.adminloginhome,name='adminloginhome'),
    
    path('admin_logout',views.admin_logout,name='admin_logout'),
    path('adminupdateseller/<int:id>',views.adminupdateseller,name='adminupdateseller'),
    path('adminseller_delete/<int:id>',views.adminseller_delete,name='adminseller_delete'),
    path('show_seller',views.show_seller,name='show_seller'),
    path('show_sellerproducts',views.show_sellerproducts,name='show_sellerproducts'),
    path('adminupdateproduct/<int:id>',views.adminupdateproduct,name='adminupdateproduct'),
    
    
    path('adminsellerproduct_delete/<int:id>',views.adminsellerproduct_delete,name='adminsellerproduct_delete'),
    
    
    
    
    path('adminupdatebuyer/<int:id>',views.adminupdatebuyer,name='adminupdatebuyer'),
    path('show_buyer',views.show_buyer,name='show_buyer'),
    path('adminbuyer_delete/<int:id>',views.adminbuyer_delete,name='adminbuyer_delete'),
    path('show_feedbacks',views.show_feedbacks,name='show_feedbacks'),
    
    

]