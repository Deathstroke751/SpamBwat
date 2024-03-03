from logging.handlers import RotatingFileHandler
import logging
from telethon import TelegramClient
from dotenv import dotenv_values
from modules.env_utils import env_list
import time

logfile = "spamlog.log"

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s [%(filename)s:%(lineno)d]",
    datefmt="%d-%b-%y %H:%M:%S",
    handlers=[
        RotatingFileHandler(
            logfile, maxBytes=100000000, backupCount=10
        ),
        logging.StreamHandler(),
    ],
)

logging.getLogger('telethon').setLevel(logging.CRITICAL)

dotenv_file = "config.env"
config_env = dotenv_values(dotenv_file)

api_id = config_env["API_ID"]
api_hash = config_env["API_HASH"]
chat_id = int(config_env["CHAT_ID"])

# msg = config_env["MSG"]

msg_interval = float(config_env["INTERVAL_BTW_MSG"])
session_interval = float(config_env["INTERVAL_BTW_SESSION"])
session_duration = float(config_env["SESSION_DURATION"])
total_time = float(config_env["TOTAL_TIME"])*60


LOGGER = logging.getLogger(__name__)
logging.info("Bot Started")
client = TelegramClient('PRIME', api_id, api_hash)


async def main():
    await client.start()
    logging.info("Logged in")
    current_time = int(time.time())

    if chat_id != 484506892:
        count = 1
        _index = 0

        while int(time.time()) < current_time + total_time:  # Runtime
            # for i in range(500):
            time_now = int(time.time())
            msgs = env_list('MSG')

            _total_msgs = len(msgs)
            if _index >= _total_msgs:
                _index = 0

            msg = msgs[_index]

            logging.info(f"Session {count} : Started")
            while int(time.time()) < time_now + session_duration:  # Session
                await client.send_message(chat_id, msg)
                time.sleep(msg_interval)
            logging.info(f"Session {count} : Ended")
            time.sleep(session_interval)
            count += 1
            _index += 1

    await client.disconnect()

if __name__ == '__main__':
    try:
        with client:
            client.loop.run_until_complete(main())
    except KeyboardInterrupt:
        logging.info("Force Exited")
