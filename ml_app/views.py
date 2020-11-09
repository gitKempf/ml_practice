from django.shortcuts import render
from . import machine_learning_model as ml

def home(request):
    return render(request, 'index.html')


def contact(request):
    return render(request, 'contact.html')

# pclass, sex, age, sibsp, parch, fare, embarked, title
def result(request):
    pclass = int(request.GET['pclass'])
    sex = int(request.GET['sex'])
    age = int(request.GET['age'])
    sibsp = int(request.GET['sibsp'])
    parch = int(request.GET['parch'])
    fare = int(request.GET['fare'])
    embarked = int(request.GET['embarked'])
    title = int(request.GET['title'])
    prediction_result = ml.prediction_model(pclass, sex, age, sibsp, parch, fare, embarked, title)
    return render(request, 'result.html', {'prediction': prediction_result})
