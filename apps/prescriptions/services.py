import requests
from prettyconf import Configuration

config = Configuration()


class RequestEndPoint:

    def __init__(self):
        self.ENDPOINT = config('ENDPOINT')

    def clinics(self, sigla='clinics', id=1):
        url = f"{self.ENDPOINT}/{sigla}/{id}"
        request = requests.get(url)
        return request.json()

    def patients(self, sigla='patients', id=1):
        url = f"{self.ENDPOINT}/{sigla}/{id}"
        request = requests.get(url)
        return request.json()

    def physicians(self, sigla='physicians', id=1):
        url = f"{self.ENDPOINT}/{sigla}/{id}"
        request = requests.get(url)
        return request.json()

    def metrics_request(self, sigla='metrics'):
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

        print(request.json())

        return request


if __name__ == "__main__":
    r = RequestEndPoint()
    r.metrics_request()
