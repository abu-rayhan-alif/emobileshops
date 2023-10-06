

# Create your models here.
from django.db import models

# Create your models here.
from django.contrib.auth.models import User



DIVISION_CHOICES=(
    
    ('DHAKA' , 'DHAKA'),
    
    ('Rajshahi' , 'Rajshahi'),
    ('Rangpur' , 'Rangpur'),
    
    ('Barisal' , 'Barisal'),
    ('sylhet' , 'sylhet'),
    
    ('Mymansingh' , 'Mymansingh'),
    
    ('Chittagong' , 'Chittagong'),
    ('Khulna' , 'Khulna'),
    
    )

class Customer(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=20)
    divisions=models.CharField(choices=DIVISION_CHOICES,max_length=100)
    districts=models.CharField(max_length=100)
    thana=models.CharField(max_length=100)
    villorroad=models.CharField(max_length=1000)
    zipcode=models.IntegerField()
    #phone_number = PhoneNumberField(blank=True)
    phone_number = models.CharField(max_length=12)
    
    def __str__(self):
        return str( self.id)
    
Brand_CHOICSES=(
    ('iphone','iphone'),
    ('samsung','samsung'),
    ('sony','sony'),
   ('blackberry','blackberry'),
    ('LG','LG' ) ,
    ('htc','htc' ) ,
    ('motorola','motorola' ) ,
    ('nokia','nokia' ) ,
)
Catagory_CHOICSES=(
    ("shopproduct","shopproduct")
   ,)

class Product(models.Model):
    
    product_title=models.CharField(max_length=100)
    selling_price=models.FloatField(max_length=100)
    discount_price=models.FloatField(max_length=100)
    discription=models.CharField(max_length=1000)
    catagory=models.CharField(choices=Catagory_CHOICSES,max_length=20)
    product_image=models.ImageField(upload_to='productimg')
    brand=models.CharField(choices=Brand_CHOICSES,max_length=20)
    
    
    def __str__(self) :
        return str(self.id)
    
BrandCatagory_CHOICSES=(
    
    ('iphone','iphone'),
    ('samsung','samsung'),
    ('sony','sony'),
    ('blackberry','blackberry'),
    ('LG','LG' ) ,
    ('htc','htc' ) ,
    ('motorola','motorola' ) ,
    ('nokia','nokia' ) ,)
    
class BrandProduct(models.Model):
    
    product_title=models.CharField(max_length=100)
    selling_price=models.FloatField(max_length=100)
    discount_price=models.FloatField(max_length=100)
    discription=models.CharField(max_length=1000)
    catagory=models.CharField(choices=BrandCatagory_CHOICSES,max_length=20)
    product_image=models.ImageField(upload_to='productimg')
    
    
    
    def __str__(self) :
        return str(self.id)
    
class Cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)
    
    def __str__(self):
        return str(self.id)
    


STATUS_CHOICE=(
    
    ('Accepted','Accepted'),
    ('Packed' ,'Packed'),
    ('On the Way','On the Way'),
    ('Deliveres','Delivered'),
    ('Cancel','Cancel')
    
)

class OrderPlaced(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)
    ordered_date=models.DateTimeField(auto_now_add=True)
    status=models.CharField(max_length=45,choices=STATUS_CHOICE,default='Pending')
    
    

Brand_CHOICSES=(
    ('iphone','iphone'),
    ('samsung','samsung'),
    ('sony','sony'),
   ('blackberry','blackberry'),
    ('LG','LG' ) ,
    ('htc','htc' ) ,
    ('motorola','motorola' ) ,
    ('nokia','nokia' ) ,  )
    
    
class TopSeller(models.Model):
    
    product_title=models.CharField(max_length=100)
    selling_price=models.FloatField(max_length=100)
    discount_price=models.FloatField(max_length=100)
    catagory=models.CharField(choices=BrandCatagory_CHOICSES,max_length=20)
    product_image=models.ImageField(upload_to='productimg')
    
   
    
    
    
    def __str__(self) :
        return str(self.id)
    
    
    
    
Brand_CHOICSES=(
    ('iphone','iphone'),
    ('samsung','samsung'),
    ('sony','sony'),
   ('blackberry','blackberry'),
    ('LG','LG' ) ,
    ('htc','htc' ) ,
    ('motorola','motorola' ) ,
    ('nokia','nokia' ) ,  )

class RecentlyTopViews(models.Model):
    
    product_title=models.CharField(max_length=100)
    selling_price=models.FloatField(max_length=100)
    discount_price=models.FloatField(max_length=100)
    catagory=models.CharField(choices=BrandCatagory_CHOICSES,max_length=20)
    product_image=models.ImageField(upload_to='productimg')
    
    
    
    
    def __str__(self) :
        return str(self.id)
    
    
Brand_CHOICSES=(
    ('iphone','iphone'),
    ('samsung','samsung'),
    ('sony','sony'),
   ('blackberry','blackberry'),
    ('LG','LG' ) ,
    ('htc','htc' ) ,
    ('motorola','motorola' ) ,
    ('nokia','nokia' ) ,  )
class TopNew(models.Model):
    
    product_title=models.CharField(max_length=100)
    selling_price=models.FloatField(max_length=100)
    discount_price=models.FloatField(max_length=100)
    catagory=models.CharField(choices=BrandCatagory_CHOICSES,max_length=20)
    product_image=models.ImageField(upload_to='productimg')
    
    
    
    
    
    def __str__(self) :
        return str(self.id)
    
    
BrandCatagory_CHOICSES=(
    
    ('iphone','iphone'),
    ('samsung','samsung'),
    ('sony','sony'),
    ('blackberry','blackberry'),
    ('LG','LG' ) ,
    ('htc','htc' ) ,
    ('motorola','motorola' ) ,
    ('nokia','nokia' ) ,)
    
class BrandPicture(models.Model):
    
    
    brand_image=models.ImageField(upload_to='productimg')
    catagory=models.CharField(choices=BrandCatagory_CHOICSES,max_length=20)
    
    
    def __str__(self) :
        return str(self.id)
        
