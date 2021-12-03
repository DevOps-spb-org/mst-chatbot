from environs import Env


env = Env()
env.read_env()
BOT_TOKEN = env.str('TEST_TOKEN_BOT')
admin_id = env.str('admin_id', 'admin_id_2')

URL_APPLES = "https://rozetka.com.ua/champion_a00225/p27223057"
URL_PEAR = "https://freshmart.com.ua/product/yabloko-gala-116.html"