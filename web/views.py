from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404
from .cart import Cart
from .forms import OrderForm,LoginForm,RegistrationForm
from .models import Category,Product,Order,OrderItem
from django.contrib.auth import login,authenticate,logout



# Create your views here.
def index(request):
    products = Product.objects.all()
    categorys = Category.objects.all()
    
    context = {'products':products,
                'categorys': categorys, 
                }
    return render(request,'index.html',context)
    

def cart(request):
    cart = Cart(request)
    return render(request,'cart.html',{'cart':cart})

def productsingle(request,id):
    productdetail = Product.objects.get(id=id)
    # form=CartAddProductForm()
    
    return render(request,'productsingle.html',{'productdetail':productdetail})

def order(request):
    orders = Order.objects.filter(user= request.user)
    return render(request,'order.html',{'orders':orders})

def product(request,id=None):
    if id:
        category = get_object_or_404(Category,id=id)
        descrips = Product.objects.filter( Category  = category)
        return render(request,'products.html',{'descrips': descrips})
    else:
        descrips =Product.objects.all()
        return render(request,'products.html',{'descrips':descrips}  )

def checkout(request):
    cart = Cart(request)

    if request.method=='POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            
            order = form.save(commit=False)
            order.user = request.user
            order.save()
            for item in cart:
                OrderItem.objects.create(
                    order=order,
                    product=item['product'],
                    quantity=item['quantity'])
            
            cart.clear()

            return redirect('success')
        
        

    form = OrderForm()
    
    context = {'form':form,
                'cart':cart}
    return render(request, 'Checkout.html',context)

def success(request):
    return render(request,'success.html')
def ordersingle(request,id):
    order = Order.objects.get(id=id)
    singles = OrderItem.objects.filter(order=order)
    return render(request, 'ordersingle.html',{'singles':singles})  

def cart_add(request,pk):
    cart = Cart(request) 
    
    cart.add(pk)
    return redirect('cart')

def cart_remove(request,pk):
    cart = Cart(request)
    cart.remove(pk)
    return redirect('cart')

def signin(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            username = cd['username']
            password = cd['password']
            user = authenticate(request,username=username, password=password)
            if user is not None:
                login(request,user)
                return redirect('index')
            
            else:
                print('invalid credentails!')

    form = LoginForm()
    return render(request, 'accounts/login.html', {'form':form})
    

def signup(request):
    if request.method == 'POST':

        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return render(request,'index.html')

    form = RegistrationForm()
    return render(request,'accounts/sign_up.html',{'form':form})

def signout(request):
    logout(request)
    return render(request,'index.html')
    