import allure
from faker import Faker

def format_string(text: str, value):
    return text.format(value)

class Generator:
    # @allure.step('Generate fake e-mail')
    @staticmethod
    def email():
        fake = Faker()
        return fake.email(domain='y.co')
    
    # @allure.step('Generate fake name')
    @staticmethod
    def name():
        fake = Faker()
        return fake.name()
    
    # @allure.step('Generate fake password')
    @staticmethod
    def password():
        fake = Faker()
        return fake.password()