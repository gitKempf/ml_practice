

def titanic_prediction_model(pclass, sex, age, sibsp, parch, fare, embarked, title):
    """
    Predicting if a person with specified parameters would be dead on titanic.
    :param pclass:
    :param sex:
    :param age:
    :param sibsp:
    :param parch:
    :param fare:
    :param embarked:
    :param title:
    :return:
    """
    import pickle
    x = [[pclass, sex, age, sibsp, parch, fare, embarked, title]]
    randomforest = pickle.load(open('ml_app/ml_models/titanic_model.sav', 'rb'))
    prediction = randomforest.predict(x)
    if prediction == 1:
        return 'Survived'
    elif prediction == 0:
        return 'Dead'
    else:
        return 'Error'
