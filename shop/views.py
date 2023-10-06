from django.shortcuts import render,redirect
from django.views import View
from .models import Customer,Product,Cart,OrderPlaced,BrandProduct,TopSeller,TopNew,RecentlyTopViews,BrandPicture
from .forms import CustomerRegistration,CustomerProfileForm
from django.contrib import messages
from django.db.models import Q
from django.http import JsonResponse



# Create your views here.

def home_page(request):
    totalitem=0
    shopproduct=Product.objects.filter(catagory='shopproduct')
    sam =TopSeller.objects.filter(catagory='samsung')
    sam1 =RecentlyTopViews.objects.filter(catagory='samsung')
    sam2=TopNew.objects.filter(catagory='samsung')
    if request.user.is_authenticated:
        totalitem=len(Cart.objects.filter(user=request.user))
    return render(request, 'home.html',{'shopproduct':shopproduct,'sam':sam,'sam1':sam1,'sam2':sam2, 'totalitem':totalitem})

#def shop_page(request):
   #return render(request, 'shoppage.html',)
   
class ShopPageView(View):
   def get(self,request):
    totalitem=0
    shopproduct=Product.objects.filter(catagory='shopproduct')
    if request.user.is_authenticated:
        totalitem=len(Cart.objects.filter(user=request.user))
    
    return render(request,'shoppage.html',{'shopproduct':shopproduct,'totalitem':totalitem
    })
    
class BrandProductView(View):
   def get(self,request):
    totalitem=0
    
    iphone = BrandProduct.objects.filter(catagory = 'iphone')
    samsung = BrandProduct.objects.filter(catagory = 'samsung')
    LG= BrandProduct.objects.filter(catagory = 'LG')
    htc= BrandProduct.objects.filter(catagory = 'htc')
    motorola= BrandProduct.objects.filter(catagory = 'motorola')
    nokia= BrandProduct.objects.filter(catagory = 'nokia')
    if request.user.is_authenticated:
        totalitem=len(Cart.objects.filter(user=request.user))
    
   
    return render(request, 'brandcategory.html', {'iphone':iphone, 'samsung':samsung, 'LG': LG,'htc':htc,'motorola':motorola,'nokia':nokia,'totalitem':totalitem})

    

#class BrandCategoryView(View):
    #def get(self, request):
        #totalitem = 0
        #iphone = Product.objects.filter(category = 'iphone')
        #samsung = Product.objects.filter(category = 'samsung')
        #LG= Product.objects.filter(category = 'LG')
        #htc= Product.objects.filter(category = 'htc')
        #motorola= Product.objects.filter(category = 'motorola')
        #nokia= Product.objects.filter(category = 'nokia')
        #if request.user.is_authenticated:
           #totalitem = len(Cart.objects.filter(user=request.user))
        
        #return render(request, 'brandcatagory.html', {'iphone':iphone, 'samsung':samsung, 'LG': LG,'htc':htc,'motorola':motorola,'nokia':nokia,'totalitem':totalitem})


#cusmoterregistrationview

class CustomerRegistrationView(View):
   def get(self,request):
      form=CustomerRegistration()
      return render(request,'customerregistration.html',{'form':form})
   def post(self,request):
      
      form=CustomerRegistration(request.POST)
      if form.is_valid:
         messages.success(request,'Successfully Registration')
         form.save()
      return render(request,'customerregistration.html',{'form':form})
      
   

class ProfileView(View):
      def get(self, request):
        totalitem=0
        form = CustomerProfileForm()
        if request.user.is_authenticated:
            totalitem=len(Cart.objects.filter(user=request.user))
        return render(request, 'profile.html', {'form':form, 'active':'btn-primary','totalitem':totalitem})
    
      def post(self, request):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            usr = request.user
            name = form.cleaned_data['name']
            divisions = form.cleaned_data['divisions']
            districts = form.cleaned_data['districts']
            thana = form.cleaned_data['thana']
            villorroad = form.cleaned_data['villorroad']
            zipcode = form.cleaned_data['zipcode']
            phone_number = form.cleaned_data['phone_number']
            
            
            reg = Customer(user=usr,name=name, divisions=divisions,districts=districts, thana=thana, villorroad=villorroad, zipcode=zipcode, phone_number = phone_number)
            reg.save()
            messages.success(request, 'Congratulations! Profile Updated Successfully')
        return render(request, 'profile.html', {'form':form, 'active':'btn-primary'})
    
class ProductDetailView(View):
  def get(self,request, pk):
      
    totalitem=0
    product = Product.objects.get(pk=pk)
    
    if request.user.is_authenticated:
        totalitem=len(Cart.objects.filter(user=request.user))
        
    
    return render(request, 'productdetail.html',{'product': product,'totalitem':totalitem})
     
def checkout(request):
            user = request.user
            add = Customer.objects.filter(user=user)
            cart_items = Cart.objects.filter(user=user)
            amount = 0.0
            shipping_amount = 100.0
            if request.user.is_authenticated:
                      totalitem = len(Cart.objects.filter(user=request.user))
            cart_product = [p for p in Cart.objects.all() if p.user == request.user]
            if cart_product:
                for p in cart_product:
                  tempamount = (p.quantity * p.product.discount_price)
                  amount += tempamount
                totalamount = amount +shipping_amount
               
            
            return render(request, 'checkout.html', {'add':add, 'totalamount':totalamount,'cart_items':cart_items,'totalitem':totalitem })
         

def address(request):
    totalitem = 0
    add = Customer.objects.filter(user = request.user)
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
    return render(request, 'address.html', {'add':add, 'active':'btn-primary', 'totalitem':totalitem})
 
 
def add_to_cart(request):
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
        user = request.user
        product_id = request.GET.get('prod_id')
        product = Product.objects.get(id=product_id)
      
        Cart(user=user, product=product).save()
        return redirect('/cart',{'totalitem': totalitem})


def show_cart(request):
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
        if request.user.is_authenticated:
            user= request.user
            amount=0.0
            shipping_amount=100
            total_amount = 0.0
            cart_product=[p for p in Cart.objects.all() if p.user==user]
            if cart_product:
                for p in cart_product:
                    tempamount = (p.quantity * p.product.discount_price)
                    amount += tempamount
                    totalamount = amount+shipping_amount
                cart = Cart.objects.filter(user=user)
                return render(request, 'addtocart.html', {'carts':cart, 'amount':amount, 'totalamount':totalamount,'totalitem':totalitem})
            else:
                return render(request, 'emptycart.html')
      
    


def plus_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.quantity +=1
        c.save()
        amount = 0.0
        shipping_amount = 100.0
        cart_product = [p for p in Cart.objects.all() if p.user == request.user]
        for p in cart_product:
            tempamount = (p.quantity * p.product.discount_price)
            amount += tempamount
        data={
            'quantity': c.quantity,
            'amount' : amount,
            'totalamount' : amount + shipping_amount
        }

        return JsonResponse(data)




    

def minus_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.quantity -=1
        c.save()
        amount = 0.0
        shipping_amount = 100.0
        cart_product = [p for p in Cart.objects.all() if p.user == request.user]
        for p in cart_product:
            tempamount = (p.quantity * p.product.discount_price)
            amount += tempamount
        data={
            'quantity': c.quantity,
            'amount' : amount,
            'totalamount' : amount + shipping_amount
        }

        return JsonResponse(data)
    

#Remove cart
def remove_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.delete()
        amount = 0.0
        shipping_amount = 100.0
        cart_product = [p for p in Cart.objects.all() if p.user == request.user]
        for p in cart_product:
            tempamount = (p.quantity * p.product.discount_price)
            amount += tempamount
        data={
            'amount' : amount,
            'totalamount' : amount + shipping_amount
        }

        return JsonResponse(data)
    
def orders(request):
    totalitem=0
    if request.user.is_authenticated:
        totalitem=len(Cart.objects.filter(user=request.user))
        op = OrderPlaced.objects.filter(user=request.user)
    
    return render(request, 'orders.html',{'order_placed':op,'totalitem':totalitem})



def payment_done(request):
    user = request.user
    custid = request.GET.get('custid')
    customer = Customer.objects.get(id=custid) 
    cart = Cart.objects.filter(user=user)
    for c in cart:
        OrderPlaced(user=user, customer=customer, product=c.product, quantity=c.quantity).save()
        c.delete()
    return redirect("orders")


def contact(request):
    
    return render(request,"contact.html")


def brand_view(request):
    def get(self,request):
      totalitem=0
    
    iphone = BrandPicture.objects.filter(catagory = 'iphone')
    samsung = BrandPicture.objects.filter(catagory = 'samsung')
    LG= BrandPicture.objects.filter(catagory = 'LG')
    htc= BrandPicture.objects.filter(catagory = 'htc')
    motorola= BrandPicture.objects.filter(catagory = 'motorola')
    nokia= BrandPicture.objects.filter(catagory = 'nokia')
    if request.user.is_authenticated:
        totalitem=len(Cart.objects.filter(user=request.user))
    
   
    return render(request, 'home.html', {'iphone':iphone, 'samsung':samsung, 'LG': LG,'htc':htc,'motorola':motorola,'nokia':nokia,'totalitem':totalitem})

class TopSellerView(View):

    
   def get(self,request):
    totalitem=0
    
    iphone = TopSeller.objects.filter(catagory = 'iphone')
    samsung = TopSeller.objects.filter(catagory = 'samsung')
    LG= TopSeller.objects.filter(catagory = 'LG')
    htc= TopSeller.objects.filter(catagory = 'htc')
    motorola= TopSeller.objects.filter(catagory = 'motorola')
    nokia= TopSeller.objects.filter(catagory = 'nokia')
    if request.user.is_authenticated:
        totalitem=len(Cart.objects.filter(user=request.user))
    
   
    return render(request, 'home.html', {'iphone':iphone, 'samsung':samsung, 'LG': LG,'htc':htc,'motorola':motorola,'nokia':nokia,'totalitem':totalitem})

class TopNewView(View):

    
   def get(self,request):
    totalitem=0
    
    iphone = TopNew.objects.filter(catagory = 'iphone')
    samsung = TopNew.objects.filter(catagory = 'samsung')
    LG= TopNew.objects.filter(catagory = 'LG')
    htc= TopNew.objects.filter(catagory = 'htc')
    motorola= TopNew.objects.filter(catagory = 'motorola')
    nokia= TopNew.objects.filter(catagory = 'nokia')
    if request.user.is_authenticated:
        totalitem=len(Cart.objects.filter(user=request.user))
    
   
    return render(request, 'home.html', {'iphone':iphone, 'samsung':samsung, 'LG': LG,'htc':htc,'motorola':motorola,'nokia':nokia,'totalitem':totalitem})

class RecentlyTopViewsView(View):

    
   def get(self,request):
    totalitem=0
    
    iphone = RecentlyTopViews.objects.filter(catagory = 'iphone')
    samsung = RecentlyTopViews.objects.filter(catagory = 'samsung')
    LG= RecentlyTopViews.objects.filter(catagory = 'LG')
    htc= RecentlyTopViews.objects.filter(catagory = 'htc')
    motorola= RecentlyTopViews.objects.filter(catagory = 'motorola')
    nokia= RecentlyTopViews.objects.filter(catagory = 'nokia')
    if request.user.is_authenticated:
        totalitem=len(Cart.objects.filter(user=request.user))
    
   
    return render(request, 'home.html', {'iphone':iphone, 'samsung':samsung, 'LG': LG,'htc':htc,'motorola':motorola,'nokia':nokia,'totalitem':totalitem})