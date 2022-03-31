from django.shortcuts import render
from utils.parsing import *
from django.core.files.storage import FileSystemStorage

def upload(request):

    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()

        fs.save(uploaded_file.name, uploaded_file)    

        parseScript(uploaded_file.name)
        

    return render(request, "homepage.html")

