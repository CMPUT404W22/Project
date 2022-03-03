import React, {useState} from "react";

import {Button, Card, Col, Container, FloatingLabel, Form, Modal, Row, Toast, ToastContainer} from "react-bootstrap";
import {Link} from "react-router-dom";
import {Helmet} from "react-helmet";
import Global from "../utility/Global";
import {Ajax} from "../utility/Ajax";
import LoadingIndicator from "../component/LoadingIndicator/LoadingIndicator";


function SignUp(prop) {
    // region participant sign up
    const [participantSignUpModal, setParticipantSignUpModal] = useState(false);
    const [showToast, setShowToast] = useState(false);
    const [toastMessage, setToastMessage] = useState("");

    const [firstName, setFirstName] = useState("");
    const [lastName, setLastName] = useState("");
    const [emailAddress, setEmailAddress] = useState("");
    const [phoneNumber, setPhoneNumber] = useState("");
    const [emergencyContactName, setEmergencyContactName] = useState("");
    const [emergencyContactNumber, setEmergencyContactNumber] = useState("");
    const [profileHeader, setProfileHeader] = useState("");
    const [pronoun, setPronoun] = useState("");
    const [password1, setPassword1] = useState("");
    const [password2, setPassword2] = useState("");

    const [loading, setLoading] = useState(false);

    const [validated, setValidated] = useState(false);

    const handleSubmit = (event) => {
        const form = event.currentTarget;
        if (form.checkValidity() === true) {
            signUpParticipants();
        } else {
            setToastMessage("Please complete sign up form.")
            setShowToast(true);
        }

        event.preventDefault();
        event.stopPropagation();
        setValidated(true);
    };

    function signUpParticipants() {
        if (password1 !== password2) {
            setToastMessage("The 2 passwords your provided does not match");
            setShowToast(true);
        } else if (firstName) {

        }

        let data = {
            "email": emailAddress,
            "first_name": firstName,
            "last_name": lastName,
            "phone": phoneNumber,
            "emergency_contact_name": emergencyContactName,
            "emergency_contact_number": emergencyContactName,
            "profile_header": profileHeader,
            "pronoun": pronoun,
            "password": password1,
        }

        setLoading(true);

        Ajax.postNoAuth(
            "api/auth/register-user/0/",
            JSON.stringify(data),
            () => {
                setToastMessage("Sign Up complete! Our team is currently reviewing your registration, once completed, you will receive an email.")
                setShowToast(true);
                setLoading(false);

                window.setTimeout(
                    () => {
                        window.location.assign("/home");
                    },
                    15000
                );
            },
            (resp) => {
                setToastMessage(resp.responseJSON.message);
                setShowToast(true);
                setLoading(false);
            }
        )
    }

    // end region

    return (
        <Container style={{maxWidth: 1200}}>
            {/* region helmet */}
            <Helmet>
                <title>{Global.TITLE} | Sign Up</title>
            </Helmet>
            {/* endregion */}

            {/* region role selection */}
            <Card>
                <Card.Body>
                    <br/>
                    <div className="d-grid gap-2">
                        <Button onClick={() => setParticipantSignUpModal(true)}>
                            I want to be a participant
                        </Button>
                    </div>
                    <br/>
                    <div className="d-grid gap-2">
                        <Button>
                            I want to be a volunteer
                        </Button>
                    </div>
                    <br/>
                    <Row>
                        <Link to="/about" className="text-muted" style={{textAlign: "center"}}>
                            Learn more
                        </Link>
                    </Row>
                </Card.Body>
            </Card>
            {/* endregion */}

            {/* region participant sign up */}
            <Modal show={participantSignUpModal} fullscreen={true} onHide={() => setParticipantSignUpModal(false)}>
                <Modal.Header closeButton>
                    <Modal.Title>Participant Sign Up</Modal.Title>
                </Modal.Header>
                <Modal.Body>
                    <Card>
                        <Card.Body>
                            <Form noValidate validated={validated} onSubmit={handleSubmit}>
                                <Row>
                                    <Col>
                                        <FloatingLabel controlId="firstName" label="First Name">
                                            <Form.Control required
                                                          type="text"
                                                          value={firstName}
                                                          onChange={(e) => setFirstName(e.target.value)}
                                            />
                                            <Form.Control.Feedback type="invalid">
                                                Please provide a valid first name
                                            </Form.Control.Feedback>
                                        </FloatingLabel>
                                    </Col>
                                    <Col>
                                        <FloatingLabel controlId="lastName" label="Last Name">
                                            <Form.Control required
                                                          type="text"
                                                          value={lastName}
                                                          onChange={(e) => setLastName(e.target.value)}
                                            />
                                            <Form.Control.Feedback type="invalid">
                                                Please provide a valid last name
                                            </Form.Control.Feedback>
                                        </FloatingLabel>
                                    </Col>
                                </Row><br/>
                                <Row>
                                    <Col>
                                        <FloatingLabel controlId="pronoun" label="Pronoun">
                                            <Form.Control required
                                                          type="text"
                                                          value={pronoun}
                                                          onChange={(e) => setPronoun(e.target.value)}
                                            />
                                            <Form.Control.Feedback type="invalid">
                                                Please provide your pronoun
                                            </Form.Control.Feedback>
                                        </FloatingLabel>
                                    </Col>
                                </Row><br/>
                                <Row>
                                    <Col>
                                        <FloatingLabel controlId="emailAddress" label="Email Address">
                                            <Form.Control required
                                                          type="email"
                                                          value={emailAddress}
                                                          onChange={(e) => setEmailAddress(e.target.value)}
                                            />
                                            <Form.Control.Feedback type="invalid">
                                                Please provide a valid email
                                            </Form.Control.Feedback>
                                        </FloatingLabel>
                                    </Col>
                                </Row><br/>
                                <Row>
                                    <Col>
                                        <FloatingLabel controlId="password1" label="Password">
                                            <Form.Control required
                                                          type="password"
                                                          value={password1}
                                                          pattern="(?=(.*[0-9]))(?=.*[a-z])(?=(.*[A-Z]))(?=(.*)).{8,}"
                                                          onChange={(e) => setPassword1(e.target.value)}
                                            />
                                            <Form.Control.Feedback type="invalid">
                                                Password must contain at least 1 uppercase, 1 lowercase, a number and
                                                must be at least 8 characters long.
                                            </Form.Control.Feedback>
                                        </FloatingLabel>
                                    </Col>
                                </Row><br/>
                                <Row>
                                    <Col>
                                        <FloatingLabel controlId="password2" label="Confirm Password">
                                            <Form.Control required
                                                          type="password"
                                                          value={password2}
                                                          isInvalid={password1 !== password2}
                                                          pattern="(?=(.*[0-9]))(?=.*[a-z])(?=(.*[A-Z]))(?=(.*)).{8,}"
                                                          onChange={(e) => setPassword2(e.target.value)}
                                            />
                                            <Form.Control.Feedback type="invalid">
                                                Does not match previous password.
                                            </Form.Control.Feedback>
                                        </FloatingLabel>
                                    </Col>
                                </Row><br/>
                                <Row>
                                    <Col>
                                        <FloatingLabel controlId="phoneNumber" label="Phone Number">
                                            <Form.Control required type="tel"
                                                          value={phoneNumber}
                                                          pattern="^\s*(?:\+?(\d{1,3}))?[-. (]*(\d{3})[-. )]*(\d{3})[-. ]*(\d{4})(?: *x(\d+))?\s*$"
                                                          onChange={(e) => setPhoneNumber(e.target.value)}
                                            />
                                            <Form.Control.Feedback type="invalid">
                                                Please provide a valid phone number.
                                            </Form.Control.Feedback>
                                        </FloatingLabel>
                                    </Col>
                                </Row><br/>
                                <Row>
                                    <Col>
                                        <FloatingLabel controlId="emergencyContactName" label="Emergency Contact Name">
                                            <Form.Control required
                                                          type="text"
                                                          value={emergencyContactName}
                                                          onChange={(e) => setEmergencyContactName(e.target.value)}
                                            />
                                        </FloatingLabel>
                                        <Form.Control.Feedback type="invalid">
                                            Please provide a valid name
                                        </Form.Control.Feedback>
                                    </Col>
                                </Row><br/>
                                <Row>
                                    <Col>
                                        <FloatingLabel controlId="emergencyContactPhone"
                                                       label="Emergency Contact Phone">
                                            <Form.Control required
                                                          type="tel"
                                                          value={emergencyContactNumber}
                                                          pattern="^\s*(?:\+?(\d{1,3}))?[-. (]*(\d{3})[-. )]*(\d{3})[-. ]*(\d{4})(?: *x(\d+))?\s*$"
                                                          onChange={(e) => setEmergencyContactNumber(e.target.value)}
                                            />
                                            <Form.Control.Feedback type="invalid">
                                                Please provide a valid phone number.
                                            </Form.Control.Feedback>
                                        </FloatingLabel>
                                    </Col>
                                </Row><br/>
                                <Row>
                                    <Col>
                                        <FloatingLabel controlId="bio" label="Bio">
                                            <Form.Control type="text"
                                                          value={profileHeader}
                                                          onChange={(e) => setProfileHeader(e.target.value)}/>
                                        </FloatingLabel>
                                    </Col>
                                </Row><br/>
                                <div className="d-grid gap-2">
                                    <Button type={"submit"}>
                                        Sign Up
                                    </Button>
                                </div>
                            </Form>
                        </Card.Body>
                    </Card>
                </Modal.Body>

                <LoadingIndicator show={loading} disableScreen/>

                <ToastContainer className="p-3" position="bottom-center">
                    <Toast onClose={() => setShowToast(false)} show={showToast} delay={10000} autohide>
                        <Toast.Header>
                            <strong className="me-auto">Alert</strong>
                            <small>Just now</small>
                        </Toast.Header>
                        <Toast.Body>{toastMessage}</Toast.Body>
                    </Toast>
                </ToastContainer>
            </Modal>
            {/* endregion */}
        </Container>
    )
}

export default SignUp;