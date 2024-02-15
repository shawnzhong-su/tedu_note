
from django.urls import path, include

from note.views import add_note

urlpatterns = [
    path('add_note', add_note)
]
