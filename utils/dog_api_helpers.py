import json

from api_app.models import DogsModel

from urllib import request as urlrequest, parse as urlparse

from secrets import randbelow

try:
    from PIL import Image
except ModuleNotFoundError as e:
    print('I dont want to be found -- ' + str(e))
    pass


def api_request(endpoint):
    """
    Combine endpoint with dog.ceo url

    :param endpoint: directory location for api
    :var endpoint: string
    :return:
    """
    return json.loads(
        urlrequest.urlopen(urlparse.urljoin("https://dog.ceo/api/", endpoint)).read().decode("utf-8")
    )


def get_twodozen_random_dog_pics():
    """ 2 baker dozen """
    return api_request('breeds/image/random/24')


def save_dog_pics_to_database():
    """ Save 24 random dog pictures to object """
    dog_list = []
    image_dict = get_twodozen_random_dog_pics()
    if image_dict['status'] == 'success':
        for single_img in image_dict['message']:
            dogs = DogsModel()
            dogs.default_value = randbelow(90000)
            dogs.description = image_dict['status']
            dogs.imgsrc = single_img
            dogs.save()
            dog_list.append(dogs)

    return dog_list


def get_two_random_dogs():
    """
    Obtain a random dog picture from database. Edit the image. Return both the original and edited image.

    :return: list of both the original and edited image.
    """
    imgsrc_list = []
    two_dogs = []
    all_dogs_list = DogsModel.objects.all()
    total_dogs = len(all_dogs_list)

    two_dogs.append(all_dogs_list[randbelow(total_dogs)])

    # attempt to edit the two images and display to user
    try:
        image1 = Image.open(two_dogs[0])
        r, g, b = image1.split()
        new_image1 = Image.merge("RGB", (b, r, g))
        new_image1.save('rgb_edit_dog.jpg')
        two_dogs.append('rgb_edit_dog.jpg')
    except NameError as e:
        print("Error during image manipulation -- {error}".format(error=str(e)))

    for dog in two_dogs:
        imgsrc_list.append(dog.imgsrc)

    # always return two images
    while len(imgsrc_list) < 2:
        imgsrc_list.append(all_dogs_list[randbelow(total_dogs)].imgsrc)

    return imgsrc_list

