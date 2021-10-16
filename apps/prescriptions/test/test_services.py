from apps.prescriptions.services import RequestEndPoint

request_endpoint = RequestEndPoint()


def test_clinics():
    data = request_endpoint.clinics(id=1)

    assert data['name'] == 'Shaun Ledner'


def test_patients_sucess():
    data = request_endpoint.patients(id=1)

    assert data['name'] == 'Claude Funk'
    assert data['email'] == 'Ross49@gmail.com'
    assert data['phone'] == '(263) 369-7435 x40648'


def test_patients_not_found():
    data = request_endpoint.patients(id=100)

    assert data['error']['message'] == "patient not found"
    assert data['error']['code'] == "03"


def test_physicians_sucess():
    data = request_endpoint.physicians(id=1)

    assert data['name'] == 'Mrs. Janie Schuppe'
    assert data['crm'] == '871ab521-13e9-4a8f-9f35-a03641ac652a'


def test_physicians_not_found():
    data = request_endpoint.physicians(id=150)

    assert data['error']['message'] == "physician not found"
    assert data['error']['code'] == "02"


def test_metrics():
    data = request_endpoint.metrics_request(clinics_id=1, patients_id=1, physicians_id=1)

    assert data["clinic_id"] == "1"
    assert data["clinic_name"] == "Shaun Ledner"
    assert data["physician_id"] == "1"
    assert data["physician_name"] == "Mrs. Janie Schuppe"
    assert data["physician_crm"] == "871ab521-13e9-4a8f-9f35-a03641ac652a"
    assert data["patient_id"] == "1"
    assert data["patient_email"] == "Ross49@gmail.com"
    assert data["patient_phone"] == "(263) 369-7435 x40648"
    assert data["patient_name"] == "Claude Funk"
