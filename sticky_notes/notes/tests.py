
from django.test import TestCase
from .models import Note, BulletinBoardPost
from .forms import NoteForm, BulletinBoardPostForm

class NoteModelTest(TestCase):
    def setUp(self):
        self.note = Note.objects.create(title="Test Note", content="Test Content")

    def test_note_creation(self):
        self.assertEqual(self.note.title, "Test Note")
        self.assertEqual(self.note.content, "Test Content")

class BulletinBoardPostModelTest(TestCase):
    def setUp(self):
        self.post = BulletinBoardPost.objects.create(title="Test Post", content="Test Content")

    def test_post_creation(self):
        self.assertEqual(self.post.title, "Test Post")
        self.assertEqual(self.post.content, "Test Content")

class NoteFormTest(TestCase):
    def test_valid_form(self):
        form = NoteForm(data={'title': "Test Note", 'content': "Test Content"})
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        form = NoteForm(data={'title': "", 'content': "Test Content"})
        self.assertFalse(form.is_valid())

class BulletinBoardPostFormTest(TestCase):
    def test_valid_form(self):
        form = BulletinBoardPostForm(data={'title': "Test Post", 'content': "Test Content"})
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        form = BulletinBoardPostForm(data={'title': "", 'content': "Test Content"})
        self.assertFalse(form.is_valid())
