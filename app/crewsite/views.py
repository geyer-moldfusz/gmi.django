from django.shortcuts import redirect


def index(request):
    return redirect('zinnia:entry_archive_index', permanent=True)
