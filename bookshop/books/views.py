from django.shortcuts import render, HttpResponse
from books.models import Contact,AddBook
from django.contrib import messages
from django.db.models import Q
# Create your views here.
def index(request):
    allBooks=AddBook.book_objects.all().order_by('-id')[:9]
    context={'allBooks':allBooks }
    if request.method=="POST":
        firstname=request.POST.get('firstname')
        lastname=request.POST.get('lastname')
        email=request.POST.get('email')
        phonenumber=request.POST.get('phonenumber')
        comments=request.POST.get('comments')
        contact=Contact(firstname=firstname,lastname=lastname,email=email,phonenumber=phonenumber,comments=comments)
        contact.save()
        messages.success(request,'Welcome to My BookStore!')
 
    return render(request, 'index.html',context)
    
def bookstore2(request):
    allBooks=AddBook.book_objects.all().order_by('-id')[9:18]
    context={'allBooks':allBooks}
    if request.method=="POST":
        firstname=request.POST.get('firstname')
        lastname=request.POST.get('lastname')
        email=request.POST.get('email')
        phonenumber=request.POST.get('phonenumber')
        comments=request.POST.get('comments')
        contact=Contact(firstname=firstname,lastname=lastname,email=email,phonenumber=phonenumber,comments=comments)
        contact.save()
        messages.success(request,'Your Message has been sent')
 
        
    return render(request, 'bookstore2.html',context)
    
def bookstore3(request):
    allBooks=AddBook.book_objects.all().order_by('-id')[18:]
    context={'allBooks':allBooks}
    if request.method=="POST":
        firstname=request.POST.get('firstname')
        lastname=request.POST.get('lastname')
        email=request.POST.get('email')
        phonenumber=request.POST.get('phonenumber')
        comments=request.POST.get('comments')
        contact=Contact(firstname=firstname,lastname=lastname,email=email,phonenumber=phonenumber,comments=comments)
        contact.save()
        messages.success(request,'Your Message has been sent')
 
        
    return render(request, 'bookstore3.html',context)       
    
def addbook(request):     
    if request.method=="POST":
        author=request.POST.get('author')
        title=request.POST.get('title')
        price=request.POST.get('price')
        description=request.POST.get('description') 
        addbook=AddBook(author=author,title=title,price=price,description=description)  
        addbook.save()
        messages.success(request,'Your Book has been Saved!')
 
    
    return render(request, 'addbook.html')



def search(request):
    query=request.GET['query']
    allBooks=AddBook.book_objects.filter(Q(title__icontains=query) | Q(author__icontains=query))
    params={'allBooks':allBooks}
    return render(request,'search.html',params)