import json

import pytest


# def python_string_slicer(str):
#    if len(str) < 50 or "python" in str:
#        return str
#    else:
#        return str[0:50]
#
# def generate_id(val):
#    return "params: {0}".format(str(val))
#
#
# @pytest.fixture(scope="function", params=[
#    ("Короткая строка", "Короткая строка"),
#    ("Длинная строка, не то чтобы прям очень длинная, но достаточно для нашего теста, и в ней нет названия языка"
#     , "Длинная строка, не то чтобы прям очень длинная, но"),
#    ("Короткая строка со словом python", "Короткая строка со словом python"),
#    ("Длинная строка, нам достаточно будет для проверки, и в ней есть слово python"
#     , "Длинная строка, нам достаточно будет для проверки, и в ней есть слово python")
# ],  ids=generate_id)
# def param_fun_generated(request):
#    return request.param
#
#
# def test_python_string_slicer_generated(param_fun_generated):
#     (input, expected_output) = param_fun_generated
#     result = python_string_slicer(input)
#     print("Входная строка: {0}\nВыходная строка: {1}\nОжидаемое значение: {2}".format(input, result, expected_output))
#     assert result == expected_output






# @pytest.mark.parametrize("x", [1, 2, 3])
# @pytest.mark.parametrize("y", [10, 11])
# def test_multiply_params(x, y):
#    print("x: {0}, y: {1}".format(x, y))
#    assert True


# @pytest.mark.parametrize("x", [-1, 0, 1], ids=["negative", "zero", "positive"])
# @pytest.mark.parametrize("y", [100, 1000], ids=["3 digit", "4 digit"])
# def test_multiply_params(x, y):
#    print("x: {0}, y: {1}".format(x, y))
#    assert True




# def ids_x(val):
#    return "x=({0})".format(str(val))
#
#
# def ids_y(val):
#    return "y=({0})".format(str(val))
#
#
# @pytest.mark.parametrize("x", [-1, 0, 1], ids=ids_x)
# @pytest.mark.parametrize("y", [100, 1000], ids=ids_y)
# def test_multiply_params(x, y):
#    print("x: {0}, y: {1}".format(x, y))
#    assert True

import json
import requests
from requests_toolbelt import MultipartEncoder


@pytest.fixture(autouse=True)
def ket_api_key():
   """ Проверяем, что запрос api-ключа возвращает статус 200 и в результате содержится слово key"""

   # Отправляем запрос и сохраняем полученный ответ с кодом статуса в status, а текст ответа в result
   status, pytest.key = pf.get_api_key(valid_email, valid_password)

   # Сверяем полученные данные с нашими ожиданиями
   assert status == 200
   assert 'key' in pytest.key

   yield

   # Проверяем что статус ответа = 200 и имя питомца соответствует заданному
   assert pytest.status == 200


def add_new_pet_simple(self, auth_key: json, name: str, animal_type: str, age: str) -> json:
   """Метод отправляет (постит) на сервер данные о добавляемом питомце и возвращает статус
   запроса и результат в формате JSON с данными добавленного питомца"""

   data = MultipartEncoder(
       fields={
           'name': name,
           'animal_type': animal_type,
           'age': age
       })
   headers = {'auth_key': auth_key['key'], 'Content-Type': data.content_type}

   res = requests.post(self.base_url + 'api/create_pet_simple', headers=headers, data=data)
   status = res.status_code
   result = ""
   try:
       result = res.json()
   except json.decoder.JSONDecodeError:
       result = res.text
   print(result)
   return status, result

def generate_string(num):
   return "x" * num

def russian_chars():
   return 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

# Здесь мы взяли 20 популярных китайских иероглифов
def chinese_chars():
   return '的一是不了人我在有他这为之大来以个中上们'

def special_chars():
   return '|\\/!@#$%^&*()-_=+`~?"№;:[]{}'


def is_age_valid(age):
   # Проверяем, что возраст - это число от 1 до 49 и целое
   return age.isdigit() \
          and 0 < int(age) < 50 \
          and float(age) == int(age)


@pytest.mark.parametrize("name"
   , ['', generate_string(255), generate_string(1001), russian_chars(), russian_chars().upper(), chinese_chars(), special_chars(), '123']
   , ids=['empty', '255 symbols', 'more than 1000 symbols', 'russian', 'RUSSIAN', 'chinese', 'specials', 'digit'])
@pytest.mark.parametrize("animal_type"
   , ['', generate_string(255), generate_string(1001), russian_chars(), russian_chars().upper(), chinese_chars(), special_chars(), '123']
   , ids=['empty', '255 symbols', 'more than 1000 symbols', 'russian', 'RUSSIAN', 'chinese', 'specials', 'digit'])
@pytest.mark.parametrize("age"
   , ['', '-1', '0', '1', '100', '1.5', '2147483647', '2147483648', special_chars(), russian_chars(), russian_chars().upper(), chinese_chars()]
   , ids=['empty', 'negative', 'zero', 'min', 'greater than max', 'float', 'int_max', 'int_max + 1', 'specials', 'russian', 'RUSSIAN', 'chinese'])
def test_add_new_pet_simple(name, animal_type, age):
   """Проверяем, что можно добавить питомца с различными данными"""

   # Добавляем питомца
   pytest.status, result = pf.add_new_pet_simple(pytest.key, name, animal_type, age)

   # Сверяем полученный ответ с ожидаемым результатом
   if name == '' or animal_type == '' or is_age_valid():
       assert pytest.status == 400
   else:
       assert pytest.status == 200
       assert result['name'] == name
       assert result['age'] == age
       assert result['animal_type'] == animal_type









