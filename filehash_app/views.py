from django.shortcuts import render
from django.contrib import messages
from .forms import UploadFileForm
from .models import UploadedFile
from django.http import JsonResponse
# Create your views here.


def upload_file(request):
    if request.method == "POST" and request.FILES.get("file"):
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = form.save(commit=False)
            file_hash = uploaded_file.calculate_hash()

            # Check if the file is already in the database
            if UploadedFile.objects.filter(hash=file_hash).exists():
                return JsonResponse({"status": "error", "message": "This file has already been uploaded."})

            uploaded_file.hash = file_hash
            uploaded_file.save()
            return JsonResponse({"status": "success", "message": "File uploaded and hashed successfully!"})

    return render(request, "upload_file.html")
