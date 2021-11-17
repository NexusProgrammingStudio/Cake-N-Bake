from django.contrib import messages
from django.shortcuts import *
from .forms import Cart1, Cart2, Wish1, Wish2
from .models import Product

# Create your views here.
IMAGE_FILE_TYPES = ['png', 'jpg', 'jpeg']

Login = "Login!"
Error = "Error.html"


def Product_Index_Cakes(request):
    coke = Product.objects.filter(Category='Cake')
    return render(request, 'Index_Cake.html', {'coke': coke})


def Product_Index_Parents(request):
    coke = Product.objects.filter(Relation__icontains='Parents').filter(Category__icontains='Cake')
    choc = Product.objects.filter(Relation__icontains='Parents').filter(Category__icontains='Chocolate')
    gif = Product.objects.filter(Relation__icontains='Parents').filter(Category__icontains='Gift')
    return render(request, 'Index_Parents.html', {'coke': coke, 'choc': choc, 'gif': gif})


def Product_Index_Siblings(request):
    coke = Product.objects.filter(Relation__icontains='Siblings').filter(Category__icontains='Cake')
    choc = Product.objects.filter(Relation__icontains='Siblings').filter(Category__icontains='Chocolate')
    gif = Product.objects.filter(Relation__icontains='Siblings').filter(Category__icontains='Gift')
    return render(request, 'Index_Siblings.html', {'coke': coke, 'choc': choc, 'gif': gif, })


def Product_Index_Kids(request):
    coke = Product.objects.filter(Relation__icontains='Kids').filter(Category__icontains='Cake')
    choc = Product.objects.filter(Relation__icontains='Kids').filter(Category__icontains='Chocolate')
    gif = Product.objects.filter(Relation__icontains='Kids').filter(Category__icontains='Gift')
    return render(request, 'Index_Kids.html', {'coke': coke, 'choc': choc, 'gif': gif})


def Product_Index_Boyfriend(request):
    coke = Product.objects.filter(Relation__icontains='Boyfriend').filter(Category__icontains='Cake')
    choc = Product.objects.filter(Relation__icontains='Boyfriend').filter(Category__icontains='Chocolate')
    gif = Product.objects.filter(Relation__icontains='Boyfriend').filter(Category__icontains='Gift')
    return render(request, 'Index_Boyfriend.html', {'coke': coke, 'choc': choc, 'gif': gif})


def Product_Index_Girlfriend(request):
    coke = Product.objects.filter(Relation__icontains='Girlfriend').filter(Category__icontains='Cake')
    choc = Product.objects.filter(Relation__icontains='Girlfriend').filter(Category__icontains='Chocolate')
    gif = Product.objects.filter(Relation__icontains='Girlfriend').filter(Category__icontains='Gift')
    return render(request, 'Index_Girlfriend.html', {'coke': coke, 'choc': choc, 'gif': gif})


def Product_Index_Chocolates(request):
    coke = Product.objects.filter(Category='Chocolate')
    return render(request, 'Index_Chocolate.html', {'coke': coke})


def Product_Index_Gifts(request):
    coke = Product.objects.filter(Category='Gift')
    return render(request, 'Index_Gift.html', {'coke': coke})


def Product_Index_Birthday(request):
    coke = Product.objects.filter(Occasion__icontains='Birthday').filter(Category__icontains='Cake')
    choc = Product.objects.filter(Occasion__icontains='Birthday').filter(Category__icontains='Chocolate')
    gif = Product.objects.filter(Occasion__icontains='Birthday').filter(Category__icontains='Gift')
    return render(request, 'Index_Birthday.html', {'coke': coke, 'choc': choc, 'gif': gif})


def Product_Index_Weddings(request):
    coke = Product.objects.filter(Occasion__icontains='Weddings').filter(Category__icontains='Cake')
    choc = Product.objects.filter(Occasion__icontains='Weddings').filter(Category__icontains='Chocolate')
    gif = Product.objects.filter(Occasion__icontains='Weddings').filter(Category__icontains='Gift')
    return render(request, 'Index_Weddings.html', {'coke': coke, 'choc': choc, 'gif': gif})


def Product_Index_Anniversary(request):
    coke = Product.objects.filter(Occasion__icontains='Anniversary').filter(Category__icontains='Cake')
    choc = Product.objects.filter(Occasion__icontains='Anniversary').filter(Category__icontains='Chocolate')
    gif = Product.objects.filter(Occasion__icontains='Anniversary').filter(Category__icontains='Gift')
    return render(request, 'Index_Anniversary.html', {'coke': coke, 'choc': choc, 'gif': gif})


def View_Product(request, Product_id):
    if not request.user.is_authenticated:
        messages.add_message(request, messages.INFO, Login)
        return render(request, Error)
    else:
        user = request.user
        chocolate = get_object_or_404(Product, P_ID=Product_id)
        forms = Cart2()
    return render(request, 'Add_Product_Cart_Wish.html', {'forms': forms, 'chocolate': chocolate, 'user': user})


def View_Cake(request, Product_id):
    if not request.user.is_authenticated:
        messages.add_message(request, messages.INFO, Login)
        return render(request, Error)
    else:
        user = request.user
        chocolate = get_object_or_404(Product, P_ID=Product_id)
        forms = Cart1()
    return render(request, 'Add_Cake_Cart_Wish.html', {'forms': forms, 'chocolate': chocolate, 'user': user})


def View_Product_Wishlist(request, Product_id):
    if not request.user.is_authenticated:
        messages.add_message(request, messages.INFO, Login)
        return render(request, Error)
    else:
        user = request.user
        chocolate = get_object_or_404(Product, P_ID=Product_id)
        forms = Wish1()
    return render(request, 'Wish_Product.html', {'forms': forms, 'chocolate': chocolate, 'user': user})


def View_Cake_Wishlist(request, Product_id):
    if not request.user.is_authenticated:
        messages.add_message(request, messages.INFO, Login)
        return render(request, Error)
    else:
        user = request.user
        chocolate = get_object_or_404(Product, P_ID=Product_id)
        forms = Wish2()
    return render(request, 'Wish.html', {'forms': forms, 'chocolate': chocolate, 'user': user})


def Sleepy(request, Product_id):
    if int(Product_id) in range(100000, 200200):
        user = request.user
        chocolate = get_object_or_404(Product, P_ID=Product_id)
        forms = Cart1()
        return render(request, 'Add_Cake_Cart_Wish.html', {'forms': forms, 'chocolate': chocolate, 'user': user})
    else:
        user = request.user
        chocolate = get_object_or_404(Product, P_ID=Product_id)
        forms = Cart2()
    return render(request, 'Add_Product_Cart_Wish.html', {'forms': forms, 'chocolate': chocolate, 'user': user})
