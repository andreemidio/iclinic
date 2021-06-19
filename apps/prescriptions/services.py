import logging

import requests
from prettyconf import Configuration

config = Configuration()


class RequestEndPoint:

    def __init__(self):
        self.ENDPOINT = config('ENDPOINT')

    def clinics(self, sigla='clinics', id=None):
        url = f"{self.ENDPOINT}/{sigla}/{id}"
        request = requests.get(url)
        return request.json()

    def patients(self, sigla='patients', id=None):
        try:
            url = f"{self.ENDPOINT}/{sigla}/{id}"
            request = requests.get(url)

            if request.text == "Not found":
                not_found = dict(
                    error=dict(
                        message="patient not found",
                        code="03"
                    )

                )
                return not_found
            return request.json()
        except ConnectionError as connection:
            logging.error(str(connection))
            _connection = dict(
                error="patients service not available",
                code="06"
            )
            return _connection

    def physicians(self, sigla='physicians', id=None):

        try:

            url = f"{self.ENDPOINT}/{sigla}/{id}"
            request = requests.get(url)

            if request.text == "Not found":
                not_found = dict(
                    error=dict(
                        message="physician not found",
                        code="02"
                    )

                )
                return not_found

            return request.json()

        except ConnectionError as connection:

            logging.error(str(connection))
            _connection = dict(
                error="physicians service not available",
                code="05"
            )

            return _connection

    def metrics_request(self, sigla='metrics'):

        try:
            url = f"{self.ENDPOINT}/{sigla}"

            clinics = self.clinics()
            patients = self.patients()
            physicians = self.physicians()

            payload = dict(
                clinic_id=clinics['id'],
                clinic_name=clinics['name'],
                physician_id=physicians['id'],
                physician_name=physicians['name'],
                physician_crm=physicians['crm'],
                patient_id=patients['id'],
                patient_name=patients['name'],
                patient_email=patients['email'],
                patient_phone=patients['phone']

            )

            request = requests.post(url, data=payload)

            return request.json()
        except ConnectionError as connection:
            logging.error(str(connection))
            _connection = dict(
                error="metrics service not available"
            )
            return _connection


if __name__ == "__main__":
    r = RequestEndPoint()
    r.metrics_request()
