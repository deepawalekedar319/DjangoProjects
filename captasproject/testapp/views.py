from django.shortcuts import render
from testapp.forms import CaptchaTestForm

def some_view(request):
    if request.POST:
        form = CaptchaTestForm(request.POST)

        # Validate the form: the captcha field will automatically
        # check the input
        if form.is_valid():
            human = True
    else:
        form = CaptchaTestForm()

    return render(request, 'testapp/template.html', {'form': form})
