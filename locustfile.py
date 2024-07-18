from locust import between, task, HttpUser
from json import loads
import os
from dotenv import load_dotenv
from helpers.bodycreator import BodyCreator
from typing import Dict, Any
from helpers.logconfig import logger

mensagemFalha: str = "Nao foi possivel acessar ou visualizar o valor de data"
load_dotenv()


class CargaApiPrice(HttpUser):
    host: str = os.getenv("GRAPHIQL_URL_UAT")
    wait_time = between(1.0, 3.0)
    prefix_price: str = os.getenv("PREFIX_PRICE")

    @task
    def busca_price_sku(self) -> None:
        consult_price_endpoint: str = f"{self.prefix_price}"
        body: Dict[str, Any] = BodyCreator.create()

        with self.client.post(url=consult_price_endpoint,
                              name="CargaApiPriceYgg - Consulta preços por SKU",
                              catch_response=True, json=body) as response:
            try:
                resposta: Dict[str, Any] = loads(response.text or "{}")
                if response.status_code == 200:
                    logger.info(f"SUCESSO NA CONSULTA - STATUS CODE: {response.status_code}")
                    print(f"============= \n- SUCESSO NA CONSULTA \n STATUS CODE: {response.status_code}")
                    if resposta['data'] is None:
                        response.failure(mensagemFalha)
                else:
                    logger.error(f"ERRO NA CONSULTA - STATUS CODE: {response.status_code} - RESPOSTA: {response.text}")
                    print(f"============= \n- ERRO NA CONSULTA DE PREÇO \n RESPONSE: {response.text} \n PAYLOAD "
                          f"ENVIADO: {resposta['data']} \n STATUS CODE: {response.status_code}")
                    response.failure(mensagemFalha)
            except KeyError as e:
                logger.error(f"EXCEÇÃO NA CONSULTA - STATUS CODE: {response.status_code} - EXCEÇÃO: {str(e)} - "
                             f"RESPOSTA: {response.text}")
                print(f"============= \n- FALHA NA CONSULTA DE PREÇO \n {response.text} \n "
                      f"STATUS CODE: {response.status_code}")
                response.failure(mensagemFalha)
