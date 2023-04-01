from django.urls import path
from . import views
app_name='seller'
urlpatterns = [
    # seller START
    path('',views.index,name='index'),
    path('sellerregister',views.sellerregister,name='sellerregister'),
    path('sellerlogin',views.sellerlogin,name='sellerlogin'),
    path('seller_dashboard/<int:id>',views.seller_dashboard,name='seller_dashboard'),
    path('seller_update/<int:id>',views.seller_update,name='seller_update'),
    path('seller_changepassword/<int:id>',views.seller_changepassword,name='seller_changepassword'),
    path('seller_delete/<int:id>',views.seller_delete,name='seller_delete'),
    path('seller_logout',views.seller_logout,name='seller_logout'),

    path('add_product/<int:id>',views.add_product,name='add_product'),    
    path('show_listedproduct/<int:id>',views.show_listedproduct,name='show_listedproduct'),    
    path('seller_productupdate/<int:id>/<int:pid>',views.seller_productupdate,name='seller_productupdate'),
    path('seller_productdelete/<int:uid>/<int:pid>',views.seller_productdelete,name='seller_productdelete'),
    path('seller_showprofile/<int:id>',views.seller_showprofile,name='seller_showprofile'),
    path('feedback/<int:id>',views.feedback,name='feedback'),
    path('mail',views.mail,name="mail"),





    


]