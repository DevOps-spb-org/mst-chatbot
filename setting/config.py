from environs import Env


env = Env()
env.read_env()
BOT_TOKEN = env.str('TEST_TOKEN_BOT')
admin_id = env.str('admin_id')
admin_id_2 = env.str('admin_id_2')
