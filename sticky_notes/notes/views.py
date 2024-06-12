
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.db.models import Q  # For search functionality
from django.contrib import messages
from .models import Note, BulletinBoardPost
from .forms import NoteForm, BulletinBoardPostForm

def note_list(request):
    query = request.GET.get('q')
    if query:
        notes = Note.objects.filter(Q(title__icontains=query) | Q(content__icontains=query))
    else:
        notes = Note.objects.all()

    paginator = Paginator(notes, 10)  # Paginate by 10 notes per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'notes/note_list.html', {'page_obj': page_obj})

def note_detail(request, pk):
    note = get_object_or_404(Note, pk=pk)
    return render(request, 'notes/note_detail.html', {'note': note})

def note_create(request):
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Note created successfully!')
            return redirect('note_list')
    else:
        form = NoteForm()
    return render(request, 'notes/note_form.html', {'form': form})

def note_update(request, pk):
    note = get_object_or_404(Note, pk=pk)
    if request.method == "POST":
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            messages.success(request, 'Note updated successfully!')
            return redirect('note_list')
    else:
        form = NoteForm(instance=note)
    return render(request, 'notes/note_form.html', {'form': form})

def note_delete(request, pk):
    note = get_object_or_404(Note, pk=pk)
    if request.method == "POST":
        note.delete()
        messages.success(request, 'Note deleted successfully!')
        return redirect('note_list')
    return render(request, 'notes/note_confirm_delete.html', {'note': note})

def bulletin_board_post_list(request):
    posts = BulletinBoardPost.objects.all()
    return render(request, 'notes/bulletin_board_post_list.html', {'posts': posts})

def bulletin_board_post_detail(request, pk):
    post = get_object_or_404(BulletinBoardPost, pk=pk)
    return render(request, 'notes/bulletin_board_post_detail.html', {'post': post})

def bulletin_board_post_create(request):
    if request.method == "POST":
        form = BulletinBoardPostForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Post created successfully!')
            return redirect('bulletin_board_post_list')
    else:
        form = BulletinBoardPostForm()
    return render(request, 'notes/bulletin_board_post_form.html', {'form': form})

def bulletin_board_post_update(request, pk):
    post = get_object_or_404(BulletinBoardPost, pk=pk)
    if request.method == "POST":
        form = BulletinBoardPostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'Post updated successfully!')
            return redirect('bulletin_board_post_list')
    else:
        form = BulletinBoardPostForm(instance=post)
    return render(request, 'notes/bulletin_board_post_form.html', {'form': form})

def bulletin_board_post_delete(request, pk):
    post = get_object_or_404(BulletinBoardPost, pk=pk)
    if request.method == "POST":
        post.delete()
        messages.success(request, 'Post deleted successfully!')
        return redirect('bulletin_board_post_list')
    return render(request, 'notes/bulletin_board_post_confirm_delete.html', {'post': post})
