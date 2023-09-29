from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

def clear_file(name):
    f = open(name, "r+")
    f.seek(0)
    f.truncate()
    f.close()

def append_file_text(name, text):
	with open(name,'a+') as f:
		f.write(text)
	f.close()

@csrf_exempt
def index(request):
    return render(request, 'home.html')

@csrf_exempt
def calculate_expression(request):
    if request.method == "POST":
        expression = request.POST.get('expression')
        try:
            response = str(eval(expression))
            prevAns_file_name = "calculatorapp/DataFiles/prevAns.txt"
            clear_file(prevAns_file_name)
            append_file_text(prevAns_file_name, response)
        except Exception as error_message:
            response = f"Error: {str(error_message)}"
        return render(request, 'home.html', {'result': response, 'expression': expression})
    return render(request, 'home.html')


