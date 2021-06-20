from apps.prescriptions.services import RequestEndPoint

request_endpoint = RequestEndPoint()


def test_clinics():
    data = request_endpoint.clinics(id=1)

    assert data['name'] == 'Dr. Kennith Bednar'


def test_patients_sucess():
    data = request_endpoint.patients(id=1)

    assert data['name'] == 'Walter Ziemann'
    assert data['email'] == 'Muriel4@gmail.com'
    assert data['phone'] == '1-853-068-7209 x379'


def test_patients_not_found():
    data = request_endpoint.patients(id=50)

    assert data['error']['message'] == "patient not found"
    assert data['error']['code'] == "03"


def test_physicians_sucess():
    data = request_endpoint.physicians(id=1)

    assert data['name'] == 'Eduardo Wiza MD'
    assert data['crm'] == 'de7099b8-f56d-480e-ab6d-6257773063e6'


def test_physicians_not_found():
    data = request_endpoint.physicians(id=150)

    assert data['error']['message'] == "physician not found"
    assert data['error']['code'] == "02"


def test_metrics():
    data = request_endpoint.metrics_request(clinics_id=1, patients_id=1, physicians_id=1)

    assert data["clinic_id"] == "1"
    assert data["clinic_name"] == "Dr. Kennith Bednar"
    assert data["physician_id"] == "1"
    assert data["physician_name"] == "Eduardo Wiza MD"
    assert data["physician_crm"] == "de7099b8-f56d-480e-ab6d-6257773063e6"
    assert data["patient_id"] == "1"
    assert data["patient_email"] == "Muriel4@gmail.com"
    assert data["patient_phone"] == "1-853-068-7209 x379"
    assert data["patient_name"] == "Walter Ziemann"
