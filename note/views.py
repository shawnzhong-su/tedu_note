from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Note


def check_login(func):
    def wrap(request, *args, **kwargs):
        if 'username' not in request.session or 'uid' not in request.session:
            c_username = request.COOKIES.get('username')
            c_id = request.COOKIES.get('uid')
            if not c_id or not c_username:
                return HttpResponseRedirect('/user/login')
            else:
                request.session['uid'] = c_id
                request.session['username'] = c_username
        return func(request, *args, **kwargs)

    return wrap


@check_login
def add_note(request):
    if request.method == "GET":
        return render(request, 'add_note.html')
    elif request.method == "POST":

        cur_title = request.POST["title"]
        cur_content = request.POST["content"]
        cur_id = request.session.get('uid')
        try:
            note = Note.objects.filter(title=cur_title)
        except Exception as e:
            print("add note error %s" % e)
            return HttpResponse("There are same title Notes,Already.")
        Note.objects.create(title=cur_title, content=cur_content,
                            user_id=cur_id)
        return HttpResponse("Add Note Success")


def list_view(request):
    notes = Note.objects.filter()
    pass
