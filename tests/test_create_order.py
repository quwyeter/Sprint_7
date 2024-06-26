import allure
import requests
from data import Data
import pytest


class TestCreateOrder:

    @allure.title('Тест создания заказа')
    @pytest.mark.parametrize('order_data', [Data.ORDER_DATA_1, Data.ORDER_DATA_2, Data.ORDER_DATA_3, Data.ORDER_DATA_4])
    def test_create_order(self, order_data):
        response = requests.post(Data.URL + Data.CREATE_ORDER, data=order_data)
        assert response.status_code == 201 and "track" in response.json()
