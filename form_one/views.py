from django.shortcuts import render
from . import forms

def index(request):
    return render(request, "form_one/home.html")


def form_name_view(request):
    form = forms.FormName()

    if request.method == 'POST':
        form = forms.FormName(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            text = form.cleaned_data['text']

            print(name, email, text)
            form.save(commit=True)
            return index(request)
        else:
            print("Error Accounted there !!! ")

    return render(request, "form_one/form_page.html", context={"form" : form})
