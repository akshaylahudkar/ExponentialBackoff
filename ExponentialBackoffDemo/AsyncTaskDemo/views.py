from rest_framework import generics, response
import requests
from celery import shared_task
import random
import time


class calculateMystery(generics.GenericAPIView):

    def get(self, request, *kwargs):
        ran_num = random.randint(1, 10000000000)
        return response.Response({"number": ran_num})


class checkMystery(generics.GenericAPIView):

    def get(self, request, *kwargs):
        callerFun.delay()

        return response.Response({"request is been processed"})


@shared_task(name="exp_backoff_task")
def callerFun():
    return exp_backoff(f)


def exp_backoff(f, x=0, retries=50, backoff_in_seconds=1):
    while True:
        try:
            return f()

        except:
            if x == retries - 1:
                raise
            else:
                sleep = (backoff_in_seconds * 2 ** x + random.uniform(0, 1))
                time.sleep(sleep)

                print('failed to assert')

                x += 1


def f() -> int:
    r = requests.get('http://127.0.0.1:8000/calc_mystery')
    print(r.json())
    if r.json()['number'] % 5:
        raise Exception("Invalid number.")

    return r.json()['number']
