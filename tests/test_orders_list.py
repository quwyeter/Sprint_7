import allure
import requests

from data import Data


class TestOrdersList:
    @allure.title('Тест получения списка заказов')
    def test_get_order_list(self):
        response = requests.get(Data.URL + Data.GET_ORDERS_LIST)
        assert response.status_code == 200 and 'orders' in response.json()
