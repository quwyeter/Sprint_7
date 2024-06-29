class Data:
    URL = 'https://qa-scooter.praktikum-services.ru'

    CREATE_COURIER = '/api/v1/courier'
    LOGIN_COURIER = '/api/v1/courier/login'
    CREATE_ORDER = '/api/v1/orders'
    GET_ORDERS_LIST = '/api/v1/orders'

    RESPONSE_CREATE_COURIER = '{"ok":true}'
    RESPONSE_CREATE_COURIER_WITHOUT_LOGIN_OR_PASSWORD = "Недостаточно данных для создания учетной записи"
    RESPONSE_CREATE_COURIER_DUPLICATE_LOGIN = "Этот логин уже используется. Попробуйте другой."
    RESPONSE_LOGIN_COURIER_WITHOUT_LOGIN_OR_PASSWORD = "Недостаточно данных для входа"
    RESPONSE_LOGIN_COURIER_WITH_INCORRECT_LOGIN_OR_PASSWORD = "Учетная запись не найдена"
    RESPONSE_NON_EXISTENT_COURIER = "Учетная запись не найдена"

    REQUEST_CREATE_COURIER = {
        "login": "ninja",
        "password": "1234",
        "firstName": "saske"
    }
    REQUEST_LOGIN_COURIER = {
        "login": "ninja",
        "password": "1234"
    }

    ORDER_DATA_1 = {
        "firstName": "Naruto",
        "lastName": "Uchiha",
        "address": "Konoha, 142 apt.",
        "metroStation": 4,
        "phone": "+7 800 355 35 35",
        "rentTime": 5,
        "deliveryDate": "2020-06-06",
        "comment": "Saske, come back to Konoha",
        "color": [
            "BLACK"
        ]
    }

    ORDER_DATA_2 = {
        "firstName": "Naruto",
        "lastName": "Uchiha",
        "address": "Konoha, 142 apt.",
        "metroStation": 4,
        "phone": "+7 800 355 35 35",
        "rentTime": 5,
        "deliveryDate": "2020-06-06",
        "comment": "Saske, come back to Konoha",
        "color": [
            "GREY"
        ]
    }

    ORDER_DATA_3 = {
        "firstName": "Naruto",
        "lastName": "Uchiha",
        "address": "Konoha, 142 apt.",
        "metroStation": 4,
        "phone": "+7 800 355 35 35",
        "rentTime": 5,
        "deliveryDate": "2020-06-06",
        "comment": "Saske, come back to Konoha",
        "color": [
            "BLACK", "GREY"
        ]
    }

    ORDER_DATA_4 = {
        "firstName": "Naruto",
        "lastName": "Uchiha",
        "address": "Konoha, 142 apt.",
        "metroStation": 4,
        "phone": "+7 800 355 35 35",
        "rentTime": 5,
        "deliveryDate": "2020-06-06",
        "comment": "Saske, come back to Konoha",
        "color": []
    }
