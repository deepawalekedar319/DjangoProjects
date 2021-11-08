from django.shortcuts import render
from translate import Translator

def homeView(request):
	data=''
	fromText=''
	toText=''
	translation=''
	try:
		if request.method=='POST':
			data = request.POST.get('userText')
			fromText = request.POST.get('toLang')
			toText = request.POST.get('fromLang')
			translator = Translator(from_lang=fromText,to_lang=toText)
			translation = translator.translate(data)
		return render(request,'Language/home.html',{'data':data,'translator':translation})
	except Exception  as e:
		print(e)
		return render(request,'Language/error.html')
