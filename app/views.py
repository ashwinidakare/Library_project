from django.shortcuts import render, redirect

# Create your views here.
from .models import Book

def home(request):
    if request.method == "POST":
        bid = request.POST.get("book_id")
        name = request.POST.get("book_name")
        qty = request.POST.get("book_qty")
        price = request.POST.get("book_price")
        author = request.POST.get("book_author")
        is_pub = request.POST.get("book_is_pub")
        # print(name, qty, price, author, is_pub)
        if is_pub == "Yes":
            is_pub = True
        else:
            is_pub = False
        if not bid:   
            Book.objects.create(name=name, qty=qty, price=price, author=author, is_published=is_pub)
        else:
            book_obj = Book.objects.get(id=bid)
            book_obj.name = name
            book_obj.qty = qty
            book_obj.price = price
            book_obj.author = author
            book_obj.is_published = is_pub
            book_obj.save()
        return redirect('home_page')
        # return HttpResponse("success")
    elif request.method == "GET":
        return render(request, "home.html", context={"book": Book.objects.all()})


def show_book(request):
    return render(request, "show_book.html", context={"books":Book.objects.filter(is_active=True), "active":True})


def update_book(request, pk):
    book_obj = Book.objects.get(id=pk)
    return render(request, "home.html", context={'single_book': book_obj})

# 
def hard_delete_book(request,pk):
    Book.objects.get(id=pk).delete()
    return redirect("active_book")

def soft_delete_book(request,pk):
    book_obj = Book.objects.get(id=pk)
    book_obj.is_active =False
    book_obj.save()
    return redirect('inactive_book')

def restore_book(request, pk):
    book_obj = Book.objects.get(id=pk)
    # print(book_obj)
    book_obj.is_active = True
    book_obj.save()
    return redirect("active_book")




def inactive_book(request):
    return render(request, "show_book.html", context={"books": Book.objects.filter(is_active=False),"inactive": True})  



