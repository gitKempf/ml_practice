

def multiplier(num):
    return int(num) * 100


def fake_prediction(age):
    if int(age) > 10:
        return "Survive"
    else:
        return "Super survive"


def prediction_model(pclass, sex, age, sibsp, parch, fare, embarked, title):
    import pickle
    x = [[pclass, sex, age, sibsp, parch, fare, embarked, title]]
    randomforest = pickle.load(open('ml_app/titanic_model.sav', 'rb'))
    prediction = randomforest.predict(x)
    if prediction == 1:
        return 'Survived'
    elif prediction == 0:
        return 'Dead'
    else:
        return 'Error'