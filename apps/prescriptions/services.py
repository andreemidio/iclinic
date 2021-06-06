import requests
from prettyconf import Configuration

config = Configuration()


class RequestEndPoint:

    def __init__(self):
        self.ENDPOINT = config('ENDPOINT')

    def clinics_request(self, sigla='clinics', id=1):
        url = f"{self.ENDPOINT}/{sigla}/{id}"
        print(url)

        request = requests.get(url)
        print(request.status_code)
        print(request.json())

        return request.json()

    def patients_request(self, sigla='patients', id=1):
        url = f"{self.ENDPOINT}/{sigla}/{id}"
        print(url)

        request = requests.get(url)
        print(request.status_code)
        print(request.json())

        return request.json()

    def physicians_request(self, sigla='physicians', id=1):
        url = f"{self.ENDPOINT}/{sigla}/{id}"
        print(url)

        request = requests.get(url)
        print(request.status_code)
        print(request.json())

        return request.json()

    def metrics_request(self, sigla='metrics'):
        url = f"{self.ENDPOINT}/{sigla}"

        print(url)

        clinics = self.clinics_request()
        patients = self.patients_request()
        physicians = self.physicians_request()

        payload = dict(
            clinic_id=1,
            clinic_name="Clínica A",
            physician_id=1,
            physician_name="José",
            physician_crm="SP293893",
            patient_id=1,
            patient_name="Rodrigo",
            patient_email="rodrigo@gmail.com",
            patient_phone="(16)998765625"

        )
        print(payload)

        request = requests.post(url, data=payload)
        print(request.status_code)
        print(request.json())

        return request


if __name__ == "__main__":
    r = RequestEndPoint()
    r.clinics_request()
    r.patients_request()
    r.physicians_request()
    r.metrics_request()
