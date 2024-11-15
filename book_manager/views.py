from django.middleware.csrf import get_token
from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render,redirect, get_object_or_404
from .models import BookData
import json
# Create your views here.

def book_list(request):
    allbook = BookData.objects.all()

    templist = []
    for book in allbook:
        templist.append({
            'id': book.id,
            'name': book.name,
            'author': book.author,
            'date': book.date,
            'price': book.price,
        })
    return JsonResponse(templist, safe=False)

def author_input(request, author_name):
    request.session['author_name'] = author_name
    return redirect('author_filter')

def author_filter(request):
    # if request.method == "POST":
    #     ser_author = request.POST.get("author_input")
    ser_author = request.session.get('author_name', None)
    if ser_author:
        author_filter_book =  BookData.objects.filter(author = ser_author).values("name", "author", "date", "price")
        if author_filter_book.exists():
            return JsonResponse(list(author_filter_book), safe=False)
        else:
            return JsonResponse({'Error': 'Sorry, the author cannot be found'})
    else:
        return JsonResponse({'Error': 'Please enter the author'})
    # else:
    #     return JsonResponse("")           

def addbook(request, name, author, date, price):
    book = BookData(
        name=name,
        author=author,
        date=date,
        price=price
    )
    book.save()
    return redirect("/list")
    

def del_book_name(request, d_name):
    dbook = BookData.objects.filter(name = d_name)
    if dbook.exists():
        if dbook.count() == 1:
            dbook.delete()
            return redirect("/list")
        else:
            return JsonResponse({'Error': 'Sorry, there is more than one book that matches your request. Please add its sequence number to the URL to delete a specific one, like:/title/1.'})
    else:
        return JsonResponse({'Error': 'No books found with this title'})    

def del_book_author(request, d_author):
    dbook = BookData.objects.filter(author = d_author)
    if dbook.exists():
        if dbook.count() == 1:
            dbook.delete()
            return redirect("/list")
        else:
            return JsonResponse({'Error': 'Sorry, there is more than one book that matches your request. Please add its sequence number to the URL to delete a specific one, like:/author/1.'})
    else:
        return JsonResponse({'Error': 'No books found with this author'})

def del_book_name_m(request, d_name, d_num):
    dbook = list(BookData.objects.filter(name = d_name))
    if d_num > 0 and d_num <= len(dbook):
        tem_dbook = dbook[d_num - 1]
        tem_dbook.delete()
        return redirect("/list")
    else:
        return JsonResponse({'Error': "Sorry, the book you want to delete could not be found."})

def del_book_author_m(request, d_author, d_num):
    dbook = list(BookData.objects.filter(author = d_author))
    if d_num > 0 and d_num <= len(dbook):
        tem_dbook = dbook[d_num - 1]
        tem_dbook.delete()
        return redirect("/list")
    else:
        return JsonResponse({'Error': 'Sorry, the book you want to delete could not be found.'})

def update_book_data(request, u_id, u_name, u_author, u_date, u_price):
    book = get_object_or_404(BookData, pk=u_id)
    book.name = u_name
    book.author = u_author
    book.date = u_date
    book.price = u_price
    try:
        book.save()
    except:
        return JsonResponse({'Error': 'Sorry, please enter the correct data.'})

    return JsonResponse({'message': 'Book details updated successfully', 
                         'Updated book': {
                             'name': book.name,
                             'author': book.author,
                             'date': book.date,
                             'price': book.price
                        }
                    })








def save_book_data(request):
    book_name = request.POST.get('book_name')
    book_author = request.POST.get('book_author')
    book_date = request.POST.get('book_date')
    book_price = request.POST.get('book_price')

    book = BookData(
        name=book_name,
        author=book_author,
        date=book_date,
        price=book_price
    )
    book.save()

    return redirect('/home')

# def author_input(request):
#     csrf_token = get_token(request)
#     html_page = f"""
#     <html>
#     <body>
#     <h3>Please enter the Author</h3>
#     <form method="POST" action="author_filter">
#         <input type="hidden" name="csrfmiddlewaretoken" value="{csrf_token}">
#         <label>Author:</label>
#         <input type = "text" name="author_input">
#         <button type = "submit">Search</button>
#     </form>
#     </body>
#     </html>
#     """
#     return HttpResponse(html_page)  

def home(request):
   return render(request, "index.html", context={})

# def home(request):
#     csrf_token = get_token(request)
#     html_page = f"""
#     <html>
#     <body>
#     <h3>Please enter the massage of your book(Book name; Author; Date"2001-01-01"; price)</h3>
#     <form method = "POST" action = "/save">
#     <input type="hidden" name="csrfmiddlewaretoken" value="{csrf_token}">
#         <label>Name<label>
#         <input type = "text" name="book_name">

#         <label>Author<label>
#         <input type = "text" name="book_author">

#         <label>date<label>
#         <input type = "text" name="book_date">

#         <label>price<label>
#         <input type = "text" name="book_price">
#     <button type = "submit">next</button>

#     <a href="/list">BookList</a>
#     <a href="/author">SearchAuthor</a>
#     </body>
#     </html>
#     """
#     return HttpResponse(html_page)
