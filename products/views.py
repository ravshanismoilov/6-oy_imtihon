from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from .models import Books, Review
from django.urls import reverse_lazy
from products.forms import AddReviewForm


# class BookListView(View):
#     def get(self, request):
#         book = Books.objects.all().order_by('-created_at')
#         return render(request, 'book/book_list.html', context={'book': book})


class BookListView(ListView):
    model = Books
    template_name = 'book/book_list.html'
    context_object_name = 'book'

class BookDetailView(View):
    def get(self, request, pk):
        book = Books.objects.get(pk=pk)
        reviews = Review.objects.filter(book=pk)
        context = {
            'book': book,
            'reviews': reviews
        }
        return render(request, 'book/book_detail.html', context=context)


class BookCreateView(CreateView):
    model = Books
    template_name = 'book/book_create.html'
    fields = '__all__'
    success_url = reverse_lazy('products:book-list')


class BookDeleteView(DeleteView):
    model = Books
    template_name = 'book/book_delete.html'
    success_url = reverse_lazy('products:book-list')


class AddReviewView(LoginRequiredMixin, View):
    def get(self, request, pk):
        books = Books.objects.get(pk=pk)
        add_review_form = AddReviewForm()
        context = {
            'books': books,
            'add_review_form': add_review_form
        }
        return render(request, 'book/add_review.html', context=context)

    def post(self, request, pk):
        books = Books.objects.get(pk=pk)
        add_review_form = AddReviewForm(request.POST)
        if add_review_form.is_valid():
            review = Review.objects.create(
                comment=add_review_form.cleaned_data['comment'],
                book=books,
                user=request.user,
                star_given=add_review_form.cleaned_data['star_given']
            )

            review.save()
            messages.success(request, 'Review added successfully.')
            return redirect('products:book-detail', pk=pk)
        else:
            messages.error(request, 'Failed to add review. Please check the form.')
            return render(request, 'book/add_review.html', {'book': books, 'add_review_form': add_review_form})