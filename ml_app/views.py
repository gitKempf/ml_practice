from django.shortcuts import render
from .ml_models import titanic_prediction
from .ml_models import fit_fat_prediction


def home(request):
    return render(request, 'index.html')


def contact(request):
    return render(request, 'contact.html')


def titanic(request):
    return render(request, 'titanic.html')


def titanic_result(request):
    pclass = int(request.GET['pclass'])
    sex = int(request.GET['sex'])
    age = int(request.GET['age'])
    sibsp = int(request.GET['sibsp'])
    parch = int(request.GET['parch'])
    fare = int(request.GET['fare'])
    embarked = int(request.GET['embarked'])
    title = int(request.GET['title'])
    prediction_result = titanic_prediction.titanic_prediction_model(pclass, sex, age, sibsp, parch, fare, embarked, title)
    return render(request, 'titanic_result.html', {'prediction': prediction_result})


def fit_fat(request):
    return render(request, 'fit_fat.html')


def fit_fat_result(request):
    prediction_result = ' '
    if request.method == 'POST':
        image = request.FILES['fileToUpload']
        prediction_result = fit_fat_prediction.fit_fat_predict(image)
    return render(request, 'fit_fat_result.html', {'prediction': prediction_result})



