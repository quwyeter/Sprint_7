import allure
import requests

from data import Data
from generator import generate_data


class TestCreateCourier:
    @allure.title('Тест успешного создания курьера')
    def test_create_courier_successful(self):
        payload = generate_data()
        response = requests.post(Data.URL + Data.CREATE_COURIER, data=payload)
        assert (response.status_code == 201 and response.text == Data.RESPONSE_CREATE_COURIER)

    @allure.title('Тест создания курьера без логина')
    def test_create_courier_without_login(self):
        payload = generate_data()
        response = requests.post(Data.URL + Data.CREATE_COURIER, data={
            'login': '',
            'password': payload['password'],
            'firstName': payload['firstName']
        })
        assert (response.status_code == 400 and response.json()['message']
                == Data.RESPONSE_CREATE_COURIER_WITHOUT_LOGIN_OR_PASSWORD)

    @allure.title("Тест создания курьера без пароля")
    def test_create_courier_without_password(self):
        payload = generate_data()
        response = requests.post(Data.URL + Data.CREATE_COURIER, data={
            'login': payload['login'],
            'password': '',
            'firstName': payload['firstName']
        })
        assert (response.status_code == 400 and response.json()['message']
                == Data.RESPONSE_CREATE_COURIER_WITHOUT_LOGIN_OR_PASSWORD)

    @allure.title('Тест создания двух одинаковых курьеров')
    def test_create_duplicate_courier(self):
        payload = Data.REQUEST_CREATE_COURIER
        requests.post(Data.URL + Data.CREATE_COURIER, data=payload)
        response = requests.post(Data.URL + Data.CREATE_COURIER, data=payload)
        assert (response.status_code == 409 and response.json()['message']
                == Data.RESPONSE_CREATE_COURIER_DUPLICATE_LOGIN)
