from locust import between, task, HttpUser
from json import loads
import os
from dotenv import load_dotenv
from helpers.bodycreator import BodyCreator

mensagemFalha = "Nao foi possivel acessar ou visualizar o valor de data"
load_dotenv()


class CargaApiPrice(HttpUser):
    host = os.environ["GRAPHIQL_URL_UAT"]
    wait_time = between(1.0, 3.0)
    prefix_price = os.environ["PREFIX_PRICE"]

    @task
    def busca_price_sku(self):
        consult_price_endpoint = f"{self.prefix_price}"
        body = BodyCreator.create()

        with self.client.post(url=consult_price_endpoint,
                              name="CargaApiPriceYgg - Consulta preços por SKU",
                              catch_response=True, json=body) as response:
            resposta = loads(response.text or "None")

            try:
                print(
                    f"============= \n- SUCESSO NA CONSULTA \n {resposta['data']} \n STATUS CODE: {response.status_code}")
                if resposta['data'] is None:
                    response.failure(
                        mensagemFalha
                    )
            except KeyError:
                print(
                    f"============= \n- FALHA NA CONSULTA DE PREÇO \n {response.text} \n STATUS CODE: {response.status_code}")
                response.failure(
                    mensagemFalha
                )
