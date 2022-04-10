import data_receiver
import logger


print(data_receiver.get_user_info(10))
logger.log_csv(data_receiver.get_user_info(10))
