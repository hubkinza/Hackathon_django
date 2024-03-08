from django.shortcuts import render, get_object_or_404, redirect
from .models import Review
from .forms import ReviewForm, CommentForm

def review_list(request):
    reviews = Review.objects.all()
    return render(request, 'yourapp/review_list.html', {'reviews': reviews})

def review_detail(request, pk):
    review = get_object_or_404(Review, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.review = review
            comment.author = request.user
            comment.save()
            return redirect('review_detail', pk=review.pk)
    else:
        form = CommentForm()
    return render(request, 'yourapp/review_detail.html', {'review': review, 'form': form})
