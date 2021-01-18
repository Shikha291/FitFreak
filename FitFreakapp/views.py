from django.shortcuts import render


# Create your views here.
def result(request):
    if request.method == "POST":
        ex1 = request.POST['11']
        ex2 = request.POST['12']
        ex3 = request.POST['13']
        ex4 = request.POST['14']
        ex5 = request.POST['15']
        ex6 = request.POST['16']

    return render(request, 'result.html')


def fit(request):
    return render(request, 'fit.html')
