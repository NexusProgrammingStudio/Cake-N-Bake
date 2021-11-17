from django.contrib import messages
from django.shortcuts import *
from django.db.models import Q
from .forms import Cart1, Cart2, Wish, Forders, Check
from .models import Wishlist, Cart, Order, Checkout
from Cataloge.models import Product
from instamojo_wrapper import Instamojo
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.

Error = "Error.html"
Wl = "Wishlist.html"
Ca = "Cart.html"
Login_Mess = "Please Login!"
SCartView = "/Services/Cart_View/%s"
Cake_Mess = "Cake Already Exist"
Vasu = "Vasu-2.html"
CPath = "/Cataloge/Product_Cake/"
Type_Mess = "Please Select Product Weight or Type!"


def Wishlist_View(request, d):
    if not request.user.is_authenticated:
        messages.add_message(request, messages.INFO, 'Login!')
        return render(request, Error)
    else:
        wish = Wishlist.objects.filter(fkuser=d)
        return render(request, Wl, {'wish': wish})


def Delete_From_Wishlist(request, d, u):
    g = Wishlist.objects.get(W_P_ID=d)
    g.delete()
    wish = Wishlist.objects.filter(fkuser=u)
    return render(request, Wl, {'wish': wish})


def Cart_View(request, d):
    if not request.user.is_authenticated:
        messages.add_message(request, messages.INFO, 'Login!')
        return render(request, Error)
    else:
        cart = Cart.objects.filter(Q(fkuser=d))
        return render(request, Ca, {'cart': cart})


def Delete_From_Cart(request, d, u, f):
    g = Cart.objects.get(C_P_ID=d, Weight=f)
    g.delete()
    cart = Cart.objects.filter(Q(fkuser=u))
    return render(request, Ca, {'cart': cart})


def Myorder(request, d):
    if not request.user.is_authenticated:
        messages.add_message(request, messages.INFO, Login_Mess)
        return render(request, Error)
    else:
        wish = Order.objects.filter(fkuser=d).order_by('-Date_of_Purchase')
    return render(request, 'orders.html', {'wish': wish})


def View_Order(request, d):
    if not request.user.is_authenticated:
        messages.add_message(request, messages.INFO, 'Login!')
        return render(request, 'Error.html')
    else:
        check = Checkout.objects.filter(fkuser=request.user.username)
        cart = Order.objects.filter(Q(fkuser=request.user.username) & Q(Order_id=d))
        return render(request, 'Invoice.html', {'cart': cart, 'check': check})


# -------------------------------------------------------------------------------------------------------------------------------------
def Add_Product_To_Cart(request, Product_id, u):
    if not request.user.is_authenticated:
        messages.add_message(request, messages.INFO, Login_Mess)
        return render(request, Error)
    else:
        ca = Product.objects.get(P_ID=Product_id)
        if request.method == "POST":
            abc = Cart.objects.filter(Q(C_P_ID=Product_id) & Q(fkuser=u))
            if not abc:
                forms = Cart2(request.POST)
                if forms.is_valid():
                    n = forms.save(commit=False)
                    n.Product_Name = ca
                    n.C_P_ID = n.Product_Name.P_ID
                    n.fkuser = request.user.username
                    n.Weight = "NaN"
                    n.Price = n.Product_Name.Price_Other_Products
                    n.T_Price = int(n.Qty) * n.Product_Name.Price_Other_Products
                    forms.save()
                    AutoDelete_From_Wishlist(request, Product_id, u)
                    cart = Cart.objects.filter(Q(fkuser=u))
                    return render(request, Ca, {'cart': cart})
            else:
                messages.success(request, 'Product Already Exist')
            return HttpResponseRedirect(SCartView % request.user.username)


def AutoDelete_From_Wishlist(request, id, u):
    if Wishlist.objects.filter(Q(W_P_ID=id) & Q(fkuser=u)):
        n = Wishlist.objects.filter(Q(W_P_ID=id) & Q(fkuser=u))
        n.delete()


def Add_Product_To_Wishlist(request, Product_id, u):
    if not request.user.is_authenticated:
        messages.add_message(request, messages.INFO, Login_Mess)
        return render(request, Error)
    else:
        ca = Product.objects.get(P_ID=Product_id)
        if request.method == "POST":
            abc = Wishlist.objects.filter(Q(W_P_ID=Product_id) & Q(fkuser=u))
            if not abc:
                forms = Wish(request.POST)
                if forms.is_valid():
                    n = forms.save(commit=False)
                    n.Product_Name = ca
                    n.W_P_ID = n.Product_Name.P_ID
                    n.desc = n.Product_Name.desc
                    n.cid = Product_id
                    n.fkuser = request.user.username
                    n.Price = n.Product_Name.Price_Other_Products
                    forms.save()
                    wish = Wishlist.objects.filter(fkuser=u)
                    return render(request, Wl, {'wish': wish, 'ca': ca})
            else:
                messages.success(request, 'Product Already Exist')
            return HttpResponseRedirect('/Services/Wishlist/%s' % request.user.username)


def Add_Cake_To_Wishlist(request, Product_id, u):
    if not request.user.is_authenticated:
        messages.add_message(request, messages.INFO, Login_Mess)
        return render(request, Error)
    else:
        ca = Product.objects.get(P_ID=Product_id)
        if request.method == "POST":
            abc = Wishlist.objects.filter(Q(W_P_ID=Product_id) & Q(fkuser=u))
            if not abc:
                forms = Wish(request.POST)
                if forms.is_valid():
                    n = forms.save(commit=False)
                    choice = forms.cleaned_data.get("Weight")
                    n.Product_Name = ca
                    n.W_P_ID = n.Product_Name.P_ID

                    n.fkuser = request.user.username
                    if choice == "500gms":
                        n.Price = n.Product_Name.Price_500gms
                    elif choice == "1kg":
                        n.Price = n.Product_Name.Price_1kg
                    elif choice == "2kg":
                        n.Price = n.Product_Name.Price_2kg
                    forms.save()
                    wish = Wishlist.objects.filter(fkuser=u)
                    return render(request, Wl, {'wish': wish})
            else:
                messages.success(request, Cake_Mess)
            return HttpResponseRedirect('/Services/Wishlist/%s' % request.user.username)


def Add_Cake_To_Cart(request, Product_id, u):
    if not request.user.is_authenticated:
        messages.add_message(request, messages.INFO, Login_Mess)
        return render(request, Error)
    else:
        ca = Product.objects.get(P_ID=Product_id)
        forms = Cart1(request.POST)
        if forms.is_valid():
            forms.save(commit=False)
            choice = forms.cleaned_data.get("Weight")
            Type = forms.cleaned_data.get("Egg_or_Eggless")
            if choice == "500gms":
                if request.method == "POST":
                    abc = Cart.objects.filter(Q(C_P_ID=Product_id) & Q(fkuser=u) & Q(Weight='500gms'))
                    if not abc:
                        n = forms.save(commit=False)
                        n.Product_Name = ca
                        n.C_P_ID = n.Product_Name.P_ID
                        n.desc = n.Product_Name.desc
                        n.fkuser = request.user.username
                        n.Qty = int(n.Qty)
                        n.Price = n.Product_Name.Price_500gms
                        n.T_Price = int(n.Qty) * n.Product_Name.Price_500gms
                        forms.save()
                        if Wishlist.objects.filter(Q(W_P_ID=Product_id) & Q(fkuser=u) & Q(Weight='500gms')):
                            n = Wishlist.objects.filter(Q(W_P_ID=Product_id) & Q(fkuser=u) & Q(Weight='500gms'))
                            n.delete()
                        if Type == "Egg":
                            cart = Cart.objects.filter(Q(fkuser=u))
                            return render(request, Ca, {'cart': cart})
                        elif Type == "Eggless":
                            cart = Cart.objects.filter(Q(fkuser=u))
                            return render(request, Ca, {'cart': cart})
                        else:
                            messages.add_message(request, messages.INFO, Type_Mess)
                            return HttpResponseRedirect(CPath + Product_id)
                    else:
                        messages.success(request, Cake_Mess)
                        return HttpResponseRedirect(SCartView % request.user.username)
            elif choice == "1kg":
                if request.method == "POST":
                    abc = Cart.objects.filter(Q(C_P_ID=Product_id) & Q(fkuser=u) & Q(Weight='1kg'))
                    if not abc:
                        n = forms.save(commit=False)
                        n.Product_Name = ca
                        n.C_P_ID = n.Product_Name.P_ID
                        n.desc = n.Product_Name.desc
                        n.fkuser = request.user.username
                        n.Price = n.Product_Name.Price_1kg
                        n.T_Price = int(n.Qty) * n.Product_Name.Price_1kg
                        forms.save()
                        if Wishlist.objects.filter(Q(W_P_ID=Product_id) & Q(fkuser=u) & Q(Weight='1kg')):
                            n = Wishlist.objects.filter(Q(W_P_ID=Product_id) & Q(fkuser=u) & Q(Weight='1kg'))
                            n.delete()
                        if Type == "Egg":
                            cart = Cart.objects.filter(Q(fkuser=u))
                            return render(request, Ca, {'cart': cart})
                        elif Type == "Eggless":
                            cart = Cart.objects.filter(Q(fkuser=u))
                            return render(request, Ca, {'cart': cart})
                        else:
                            messages.add_message(request, messages.INFO, Type_Mess)
                            return HttpResponseRedirect(CPath + Product_id)
                    else:
                        messages.success(request, Cake_Mess)
                        return HttpResponseRedirect(SCartView % request.user.username)
            elif choice == "2kg":
                if request.method == "POST":
                    abc = Cart.objects.filter(Q(C_P_ID=Product_id) & Q(fkuser=u) & Q(Weight='2kg'))
                    if not abc:
                        n = forms.save(commit=False)
                        n.Product_Name = ca
                        n.C_P_ID = n.Product_Name.P_ID
                        n.desc = n.Product_Name.desc
                        n.fkuser = request.user.username
                        n.Price = n.Product_Name.Price_2kg
                        n.T_Price = int(n.Qty) * n.Product_Name.Price_2kg
                        forms.save()
                        if Wishlist.objects.filter(Q(W_P_ID=Product_id) & Q(fkuser=u) & Q(Weight='2kg')):
                            n = Wishlist.objects.filter(Q(W_P_ID=Product_id) & Q(fkuser=u) & Q(Weight='2kg'))
                            n.delete()
                        if Type == "Egg":
                            cart = Cart.objects.filter(Q(fkuser=u))
                            return render(request, Ca, {'cart': cart})
                        elif Type == "Eggless":
                            cart = Cart.objects.filter(Q(fkuser=u))
                            return render(request, Ca, {'cart': cart})
                        else:
                            messages.add_message(request, messages.INFO, Type_Mess)
                            return HttpResponseRedirect(CPath + Product_id)
                    else:
                        messages.success(request, Cake_Mess)
                        return HttpResponseRedirect(SCartView % request.user.username)
            else:
                messages.add_message(request, messages.INFO, 'Please Select all the Required Option! ')
                return HttpResponseRedirect(CPath + Product_id)


def pay(request):
    price = 0
    for s in Cart.objects.filter(Q(fkuser=request.user.username)):
        price = price + s.T_Price
    api = Instamojo(api_key="5e20a438146f7770701113f3cff1d4f4", auth_token="7962320bc33ba76b11e42a4ec67f00b8",
                    endpoint='https://test.instamojo.com/api/1.1/');

    response = api.payment_request_create(
        purpose='Cake_n_Bake',
        amount=price,
        buyer_name=request.user.get_full_name(),
        email=request.user.email,
        phone='9810832975',
        redirect_url='http://127.0.0.1:8000/Services/Invoice',
        send_email='True',
        send_sms='True',
        webhook='http://www.example.com/webhook/',
        allow_repeated_payments='False',
    )
    response['payment_request']['longurl']
    print(response['payment_request']['status'])

    return HttpResponseRedirect(response['payment_request']['longurl'])


def Invoice(request):
    if not request.user.is_authenticated:
        messages.add_message(request, messages.INFO, Login_Mess)
        return render(request, Error)
    else:
        if request.user:
            vasu = Order.objects.latest('Order_id')
            abc = int(vasu.Order_id) + 1
        for a in Checkout.objects.filter(fkuser=request.user.username):
            add = a.Address
            mob = a.contact_no
            email = a.email
        cart = Cart.objects.filter(Q(fkuser=request.user.username))
        for i in cart:
            forms = Forders(request.POST)
            if forms.is_valid():
                n = forms.save(commit=False)
                n.Product_Name = i.Product_Name
                n.Price = i.Price
                n.Qty = int(i.Qty)
                n.T_Price = int(i.Qty) * i.Price
                n.fkuser = request.user.username
                n.Order_id = abc
                forms.save()
            i.delete()
        if request.user:
            vasu = Order.objects.latest('Order_id')
            abc = int(vasu.Order_id)
        check = Checkout.objects.filter(fkuser=request.user.username)
        cart = Order.objects.filter(Q(fkuser=request.user.username) & Q(Order_id=abc))
        html_content = "Your order no is %s \n\nShipping address: %s \n\nMobile No. %s\n\nInvoice: http://127.0.0.1:8000/Services/View_Order/%s/ \n\n" % (abc, add, mob, abc)
        notification = "Name: %s  %s \n\nOrder no is %s \n\nShipping address: %s \n\nMobile No. %s \n\nInvoice: http://127.0.0.1:8000/Services/View_Order/%s/" % (
            request.user.first_name, request.user.last_name, abc, add, mob, abc)
        send_mail('Order Confirmation', html_content, settings.EMAIL_HOST_USER, [request.user.email],
                  fail_silently=False)
        send_mail('Order Confirmation', notification, settings.EMAIL_HOST_USER, [email], fail_silently=False)
        return render(request, 'Invoice.html', {'cart': cart, 'check': check})
        pyautogui.hotkey('ctrl', 'p')


def Checkout_Option(request, d):
    if not request.method == "POST":
        abc = Checkout.objects.filter(fkuser=request.user.username)
        if not abc:
            form = Check(request.POST)
            if form.is_valid():
                n = form.save(commit=False)
                form.save()
                return redirect('/Services/Pay')
        else:
            form = Check(instance=Checkout.objects.get(fkuser=request.user.username))
            check = Checkout.objects.filter(fkuser=request.user.username)
            return render(request, Vasu, {'form': form, 'check': check})
    else:
        form = Check(instance=Checkout.objects.get(fkuser=request.user.username))
        check = Checkout.objects.filter(fkuser=request.user.username)
        return render(request, Vasu, {'form': form, 'check': check})


def Choice(request, d):
    ch = Checkout.objects.filter(fkuser=d)
    if not ch:
        return redirect('/Services/New/' + d)
    else:
        return redirect('/Services/Old/' + d)


def New(request, d):
    if request.method == 'POST':
        form = Check(request.POST)
        if form.is_valid():
            n = form.save(commit=False)
            n.fkuser = request.user.username
            form.save()
        return redirect('/Services/Pay')
    else:
        form = Check()
        check = Checkout.objects.filter(fkuser=request.user.username)
        return render(request, Vasu, {'form': form, 'check': check})


def Old(request, d):
    if request.method == 'POST':
        form = Check(request.POST)
        if form.is_valid():
            n = form.save(commit=False)
            n.fkuser = request.user.username
            form.save()
            return redirect('/Services/Pay')
    else:
        form = Check(instance=Checkout.objects.get(fkuser=request.user.username))
        check = Checkout.objects.filter(fkuser=request.user.username)
        return render(request, Vasu, {'form': form, 'check': check})
