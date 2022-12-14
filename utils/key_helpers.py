import django
django.setup()

import datetime
import time

from api_app.models import SomeKeys

from secrets import randbelow

from multiprocessing import Process, Queue


def increment_key(request, increment_amount=0):
    """
    Increment a random key by the users input.
    - Multiprocess instances of incrementing value once && incrementing value for 10 seconds
    :param increment_amount:
    :param request:
    :return: HttpResponse with String to display on page
    """
    Q = Queue()
    all_keys = SomeKeys.objects.all()
    if not all_keys:
        return 'No keys currently exist'
    total_keys = len(all_keys)
    value_to_pick = randbelow(total_keys)

    message = ''

    # pick a random key from the list
    key_to_change = all_keys[value_to_pick]

    # multiprocess before a return cause why not :)
    first_proc = Process(target=increment_value_once, args=(key_to_change, increment_amount, Q))
    first_proc.start()
    message += Q.get()  # grab message
    message += ' -=-=-=-=-=-=-=-=- '
    sec_proc = Process(target=increment_value_ten_seconds, args=(key_to_change, increment_amount, Q))
    sec_proc.start()
    message += Q.get()  # grab message
    first_proc.join()
    sec_proc.join()

    return message


def increment_value_ten_seconds(selected_key, increment_value, Q):
    start_time = datetime.datetime.now()
    end_time = start_time + datetime.timedelta(seconds=10)

    initial_key_string = 'Key Name: ' + selected_key.name + ' | Old Key Value: ' + str(selected_key.default_value)

    while end_time > datetime.datetime.now():
        time.sleep(.5)
        selected_key.default_value += int(increment_value)
    selected_key.save()

    new_key_string = ' --> New Key Value: ' + str(selected_key.default_value)

    message = initial_key_string + new_key_string

    Q.put(message)


def increment_value_once(selected_key, increment_value, Q):
    initial_key_string = 'Key Name: ' + selected_key.name + ' | Old Key Value: ' + str(selected_key.default_value)

    selected_key.default_value += int(increment_value)
    selected_key.save()

    new_key_string = ' --> New Key Value: ' + str(selected_key.default_value)

    message = initial_key_string + new_key_string

    Q.put(message)
