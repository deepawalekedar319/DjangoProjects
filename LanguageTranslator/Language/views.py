from django.shortcuts import render
from translate import Translator

def homeView(request):
	data=''
	translation=''
	try:
		if request.method=='POST':
			data = request.POST.get('userText')
			lang = request.POST.get('lang')
			translator = Translator(to_lang=lang)
			translation = translator.translate(data)
		return render(request,'Language/home.html',{'data':data,'translator':translation})
	except:
		return render(request,'Language/error.html')
