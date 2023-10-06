from django.contrib import admin



# Register your models here.

from .models import(
    
    Customer,
    Product,
    Cart,
    OrderPlaced,
    BrandProduct,
    TopNew,
    TopSeller,
    RecentlyTopViews,
    BrandPicture,
    
    
)


@admin.register(Customer)

class CustomerModelAmin(admin.ModelAdmin):
    
    list_display=[
        'id',
    'user',
    'name',
    'divisions',
    'districts',
    'thana',
   'villorroad',
    'zipcode',
    'phone_number'
    ]
    
@admin.register(Product)

class ProductModelAdmin(admin.ModelAdmin):
    list_display=[ 
    'id',              
    'product_title',
    'selling_price',
    'discount_price',
    'discription',
    'catagory',
    'product_image',
    'brand'
    ]
    
    
@admin.register(BrandProduct)

class BrandProductAdmin(admin.ModelAdmin):
    list_display=[ 
    'id',              
    'product_title',
    'selling_price',
    'discount_price',
    'discription',
    'catagory',
    'product_image'
    
    ]
    
    


@admin.register(Cart)
    
class CartModelAdmin(admin.ModelAdmin):
    
    list_display=[ 'id',
   'user','product','quantity'
    ]
    
@admin.register(OrderPlaced)
    
class OrderPlacedModelAdmin(admin.ModelAdmin):
    
    list_display=[  
    'id',
    'user',
    'customer',
    'product',
    'quantity',
    'ordered_date',
    'status'
    ]

@admin.register(TopNew)

class TopNewAdmin(admin.ModelAdmin):
    list_display=[ 
    'id',              
    'product_title',
    'selling_price',
    'discount_price',
    'product_image',
    
    
    
    ]
    
@admin.register(TopSeller)

class TopSellerAdmin(admin.ModelAdmin):
    list_display=[ 
    'id',              
    'product_title',
    'selling_price',
    'discount_price',
    'catagory',
    'product_image',
    
    
    
    
    ]
@admin.register(RecentlyTopViews)

class RecentlyTopViewsAdmin(admin.ModelAdmin):
    list_display=[
         
     'id',              
    'product_title',
    'selling_price',
    'discount_price',
    'catagory',
    'product_image',
    
    
    
    ]

@admin.register(BrandPicture)

class BrandPictureAdmin(admin.ModelAdmin):
    list_display=[ 
                  
    'id', 
    'brand_image',
    'catagory',
                 
    
   ]