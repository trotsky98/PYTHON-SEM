from loguru import logger
logger.add('log.csv', format="{time} - {level} - {message}", \
            level='DEBUG')