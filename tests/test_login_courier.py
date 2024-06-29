import allure
import requests

from data import Data
from generator import generate_data


class TestLoginCourier:

    @allure.title('Тест успешного входа')
    def test_log_in_successful(self):
        payload = generate_data()
        requests.post(Data.URL + Data.CREATE_COURIER, data=payload)
        response = requests.post(Data.URL + Data.LOGIN_COURIER, data=payload)
        assert response.status_code == 200 and 'id' in response.json()

    @allure.title('Тест входа без логина')
    def test_log_in_without_login(self):
        payload = generate_data()
        requests.post(Data.URL + Data.CREATE_COURIER, data=payload)
        response = requests.post(Data.URL + Data.LOGIN_COURIER, data={
            'login': '',
            'password': payload['password']
        })
        assert (response.status_code == 400
                and response.json()['message'] == Data.RESPONSE_LOGIN_COURIER_WITHOUT_LOGIN_OR_PASSWORD)

    @allure.title('Тест входа без пароля')
    def test_log_in_without_password(self):
        payload = generate_data()
        response = requests.post(Data.URL + Data.LOGIN_COURIER, data={
            "login": payload["login"],
            "password": ""
        })
        assert (response.status_code == 400
                and response.json()['message'] == Data.RESPONSE_LOGIN_COURIER_WITHOUT_LOGIN_OR_PASSWORD)

    @allure.title('Тест входа в несуществующий аккаунт')
    def test_login_non_existent(self):
        response = requests.post(Data.URL + Data.LOGIN_COURIER, data={
            "login": "abcd",
            "password": "abcd"
        })
        assert response.status_code == 404 and response.json()['message'] == Data.RESPONSE_NON_EXISTENT_COURIER

    @allure.title('Тест входа с некорректным логином')
    def test_log_in_with_incorrect_login(self):
        payload = generate_data()
        requests.post(Data.URL + Data.CREATE_COURIER, data=payload)
        response = requests.post(Data.URL + Data.LOGIN_COURIER, data={
            'login': 'abcccc',
            'password': payload['password']
        })
        assert (response.status_code == 404
                and response.json()['message'] == Data.RESPONSE_LOGIN_COURIER_WITH_INCORRECT_LOGIN_OR_PASSWORD)

    @allure.title('Тест входа с некорректным паролем')
    def test_log_in_with_incorrect_password(self):
        payload = generate_data()
        requests.post(Data.URL + Data.CREATE_COURIER, data=payload)
        response = requests.post(Data.URL + Data.LOGIN_COURIER, data={
            'login': payload["login"],
            'password': 'abcccc'
        })
        assert (response.status_code == 404
                and response.json()['message'] == Data.RESPONSE_LOGIN_COURIER_WITH_INCORRECT_LOGIN_OR_PASSWORD)
