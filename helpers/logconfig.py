import logging

# Configuração do logger
logger = logging.getLogger('carga_api_logger')
logger.setLevel(logging.DEBUG)

# Formato do log
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Configuração para o log de sucessos
success_handler = logging.FileHandler('success_requests.log')
success_handler.setLevel(logging.INFO)
success_handler.setFormatter(formatter)

# Configuração para o log de erros
error_handler = logging.FileHandler('error_requests.log')
error_handler.setLevel(logging.ERROR)
error_handler.setFormatter(formatter)

# Adicionando os handlers ao logger
logger.addHandler(success_handler)
logger.addHandler(error_handler)
