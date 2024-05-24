from environs import Env

# Теперь используем вместо библиотеки python-dotenv библиотеку environs
env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")  # Забираем значение типа str
ADMINS = env.list("ADMINS")  # Тут у нас будет список из админов
IP = env.str("ip")  # Тоже str, но для айпи адреса хоста

DB_IP = env.str("DB_IP")
PGUSER = env.str("PGUSER")
PGPASSWORD = env.str("PGPASSWORD")
DATABASE = env.str("DATABASE")
POSTGRES_URI = f"postgresql://{PGUSER}:{PGPASSWORD}@{DB_IP}/{DATABASE}"

# webhook settings
WEBHOOK_HOST = f"https://{IP}"
WEBHOOK_PORT = int(8443)
WEBHOOK_PATH = f"/bot/{BOT_TOKEN}"
WEBHOOK_URL = f"{WEBHOOK_HOST}:{WEBHOOK_PORT}{WEBHOOK_PATH}"

WEBHOOK_SSL_CERT = "webhook_cert.pem"
WEBHOOK_SSL_PRIV = "webhook_pkey.pem"

# webserver settings
WEBAPP_HOST = '0.0.0.0'
WEBAPP_PORT = env.int("WEBAPP_PORT")
