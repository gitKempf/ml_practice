from PIL import Image
import numpy as np
from keras.models import load_model


def crop_to_square(img, new_width=None, new_height=None):
    """
    Getting the image cropped to square with the lesser of specified side length
    or the one side of image that lesser then other if not specified
    :param img:
    :param new_width:
    :param new_height:
    :return: cropped image
    """

    width, height = img.size  # Get dimensions

    if new_width is None:
        new_width = min(width, height)
    if new_height is None:
        new_height = min(width, height)

    left = np.ceil((width - new_width) / 2)
    right = width - np.floor((width - new_width) / 2)

    top = int(np.ceil((height - new_height) / 2))
    bottom = height - np.floor((height - new_height) / 2)

    center_cropped_img = img.crop((left, top, right, bottom))

    return center_cropped_img


def fit_fat_predict(image_loaded):
    """
    Predicting if the person on loaded picture is fit or fat
    :param image_loaded:
    :return:
    """
    name_encode = {"fat_man": 0, "fit_man": 1, "fat_woman": 2, "fit_woman": 3}

    model = load_model('ml_app/ml_models/fit_fat_CNN_v1.h5')

    image = Image.open(image_loaded)
    croped_image = crop_to_square(image)
    resized_image = Image.Image.resize(croped_image, (200, 200))
    image_normalized = (np.array(resized_image) - 127.5) / 127.5
    reshaped_img = image_normalized.reshape(1, 200, 200, 3)
    prediction = model.predict_classes(reshaped_img)
    for key, value in name_encode.items():
        if value == prediction:
            return key
