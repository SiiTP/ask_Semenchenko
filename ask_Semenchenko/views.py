from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
	return HttpResponse("Hello world! from views.py")

def postget(request):
	outp =  """
		<form action = "/postget/" method="post">
			<label for="hello">Say hello!!!: </label>
			<input id="hello" type="str" name="hello" value=""><br>
			<button type="submit"> 
				OK
			</button>
	    	</form>
		%s
		"""
	if request.method == 'POST':
		param = request.POST['hello']
		outp = outp % ("You said :  " + str(param) + '\n')
		return HttpResponse(outp)
	return HttpResponse(outp)

def myHello(request):
	if request.method =='GET':
		param=request.GET.get('param')
		return HttpResponse("Get " + str(param))

def main(request):
	return render(request,'main.html',{})
	
