from django.http import HttpResponse
from django.shortcuts import render


def hello(request):
    # render(request,'picture.html',{})
    return HttpResponse("Hello world! from views.py")


def postget(request):
    outp = """
        form action = "/postget/" method="post">
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
    if request.method == 'GET':
        param = request.GET.get('param')
        return HttpResponse("Get " + str(param))


def main(request):
    #if request.method == 'GET':
    #    regVariant = request.GET.get('regVariant')
    #    context = {'regVariant' : regVariant}
    return render(request, 'main.html', {})


def ask(request):
    return render(request, 'ask.html', {})


def question(request):
    return render(request, 'question.html', {})


def image(request):
    return render(request, 'image.html', {})