from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import Book, Rate
from .forms import BookForm, RateForm


class DisplayBooks(View):

    def get(self, request):
        books = Book.objects.all()
        return render(request, 'Library/main.html', {'books': books})


class NewBook(View):

    def get(self, request):
        book_form = BookForm(request.POST or None, request.FILES or None)

        return render(request, 'Library/new_form.html', {'book_form': book_form, 'new': True})

    def post(self, request):
        book_form = BookForm(request.POST or None, request.FILES or None)

        if book_form.is_valid():
            book = book_form.save()
            book.save()
            return redirect('main')

        return render(request, 'Library/new_form.html', {'book_form': book_form, 'new': True})


class EditBook(View):

    def get(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        book_form = BookForm(request.POST or None, instance=book)
        average_rate = round(Book.get_average_rate(book), 2)

        context = {
            'average_rate': average_rate,
            'book_form': book_form,
            'new': False, 'book': book
        }

        return render(request, 'Library/edit_form.html', context)

    def post(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        book_form = BookForm(request.POST or None, instance=book)

        if book_form.is_valid():
            book.save()
            return redirect('main')

        return render(request, 'Library/edit_form.html', {'book_form': book_form, 'new': False})


class RateBook(View):

    def get(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        rate_form = RateForm(request.POST or None)

        context = {
            'book': book,
            'rate_form': rate_form,
        }

        return render(request, 'Library/rate_book.html', context)

    def post(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        rate_form = RateForm(request.POST or None)

        if rate_form.is_valid():
            rate = rate_form.save(commit=False)
            rate.rated_book = book
            rate.save()
            return redirect('edit_book', pk=pk)

        return render(request, 'Library/rate_book.html', {'rate_form': rate_form, 'book': book})


class DeleteBook(View):

    def get(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        return render(request, 'Library/confirmation.html', {'book': book})

    def post(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        book.delete()
        return redirect('main')


class SortedBooks(View):

    def get(self, request):
        books = Book.sorted_list()

        return render(request, 'Library/sorted_books.html', {'books': books})

class OftenRate(View):

    def get(self, request):
        books = Book.sorted_by_amount_of_rates()


        return render(request, 'Library/often_rated.html', {'books': books})

class Search(View):

    def get(self, request):
        searching = request.GET.get('searching') if request.GET.get('searching') else "asd@#!#$fsdfs#@SAD@#$dasfa@#"
        result = Book.search_item(searching)
        return render(request, 'Library/search.html', {'result': result})



