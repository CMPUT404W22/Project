import React, {useState} from "react";

import {Button, Card, Col, Container, FloatingLabel, Form, Modal, Row, Toast, ToastContainer} from "react-bootstrap";

import {Helmet} from "react-helmet";

import Identity from "../model/Identity";
import Global from "../utility/Global";
import {AuthProvider} from "../auth/AuthProvider";
import {Ajax} from "../utility/Ajax";

let identity = Identity.GetIdentity();

function UserProfile(prop) {
    // region shared
    const [showToast, setShowToast] = useState(false);
    const [toastMessage, setToastMessage] = useState("");
    //endregion

    // region profile
    const [firstName, setFirstName] = useState(identity.firstName);
    const [lastName, setLastName] = useState(identity.lastName);
    const [emailAddress, setEmailAddress] = useState(identity.emailAddress);
    const [phoneNumber, setPhoneNumber] = useState(identity.phoneNumber);
    const [emergencyContactName, setEmergencyContactName] = useState(identity.emergencyContactName);
    const [emergencyContactNumber, setEmergencyContactNumber] = useState(identity.emergencyContactNumber);
    const [profileHeader, setProfileHeader] = useState(identity.profileHeader);
    const [pronoun, setPronoun] = useState(identity.pronoun);
    const [edit, setEdit] = useState(false);
    const [changePasswordModal, setChangePasswordModal] = useState(false);

    function saveProfile () {
        Ajax.post(
            "user/profile/",
            JSON.stringify({
                "first_name": firstName,
                "last_name": lastName,
                "pronoun": pronoun,
                "header": profileHeader,
                "email": emailAddress,
                "phone": phoneNumber,
                "emergency_contact_name": emergencyContactName,
                "emergency_contact_number": emergencyContactNumber,
            }),
            (resp) => {
                Identity.UpdateProfile(
                    resp["first_name"],
                    resp["last_name"],
                    resp["pronoun"],
                    resp["header"],
                    resp["email"],
                    resp["phone"],
                    resp["emergency_contact_name"],
                    resp["emergency_contact_number"],
                );
                setShowToast(true);
                setToastMessage("Profile Updated.");
                setEdit(false);
            },
            () => {
                setShowToast(true);
                setToastMessage("Failed to update profile, please try again.");
            }
        );
    }

    function resetProfile () {
        identity = Identity.GetIdentity();

        setFirstName(identity.firstName);
        setLastName(identity.lastName);
        setEmailAddress(identity.emailAddress);
        setPhoneNumber(identity.phoneNumber);
        setEmergencyContactName(identity.emergencyContactName);
        setEmergencyContactNumber(identity.emergencyContactNumber);
        setProfileHeader(identity.profileHeader);
        setPronoun(identity.pronoun);
        setEdit(false);
    }
    // endregion

    // region change password
    const [oldPassword, setOldPassword] = useState("");
    const [newPassword1, setNewPassword1] = useState("");
    const [newPassword2, setNewPassword2] = useState("");

    function changePassword () {
        // TODO
    }
    // endregion

    return (
        <Container>
            {/* region helmet */}
            <Helmet>
                <title>{Global.TITLE} | Profile</title>
            </Helmet>
            {/* endregion */}

            {/* region profile */}
            <Card>
                <Card.Body>
                    <Form>
                        <fieldset disabled={!edit}>
                            <div>
                                <Row>
                                    <Col>
                                        <FloatingLabel controlId="firstName" label="First Name">
                                            <Form.Control type="text" value={firstName} onChange={(e)=>setFirstName(e.target.value)}/>
                                        </FloatingLabel>
                                    </Col>
                                    <Col>
                                        <FloatingLabel controlId="lastName" label="Last Name">
                                            <Form.Control type="text" value={lastName} onChange={(e)=>setLastName(e.target.value)}/>
                                        </FloatingLabel>
                                    </Col>
                                </Row><br/>
                                <Row>
                                    <Col>
                                        <FloatingLabel controlId="pronoun" label="Pronoun">
                                            <Form.Control type="text" value={pronoun} onChange={(e)=>setPronoun(e.target.value)}/>
                                        </FloatingLabel>
                                    </Col>
                                </Row><br/>
                                <Row>
                                    <Col>
                                        <FloatingLabel controlId="emailAddress" label="Email Address">
                                            <Form.Control type="email" value={emailAddress} onChange={(e)=>setEmailAddress(e.target.value)}/>
                                        </FloatingLabel>
                                    </Col>
                                </Row><br/>
                                <Row>
                                    <Col>
                                        <FloatingLabel controlId="phoneNumber" label="Phone Number">
                                            <Form.Control type="phone" value={phoneNumber} onChange={(e)=>setPhoneNumber(e.target.value)}/>
                                        </FloatingLabel>
                                    </Col>
                                </Row><br/>
                                <Row>
                                    <Col>
                                        <FloatingLabel controlId="emergencyContactName" label="Emergency Contact Name">
                                            <Form.Control type="text" value={emergencyContactName} onChange={(e)=>setEmergencyContactName(e.target.value)}/>
                                        </FloatingLabel>
                                    </Col>
                                </Row><br/>
                                <Row>
                                    <Col>
                                        <FloatingLabel controlId="emergencyContactPhone" label="Emergency Contact Phone">
                                            <Form.Control type="phone" value={emergencyContactNumber} onChange={(e)=>setEmergencyContactNumber(e.target.value)}/>
                                        </FloatingLabel>
                                    </Col>
                                </Row><br/>
                                <Row>
                                    <Col>
                                        <FloatingLabel controlId="bio" label="Bio">
                                            <Form.Control type="text" value={profileHeader} onChange={(e)=>setProfileHeader(e.target.value)}/>
                                        </FloatingLabel>
                                    </Col>
                                </Row><br/>
                            </div>
                        </fieldset>
                        {!edit ?
                            <Row>
                                <Col className="d-grid gap-2">
                                    <Button variant="primary" style={{right:0}} onClick={()=>setChangePasswordModal(true)}>
                                        Change Password
                                    </Button>
                                </Col>
                                <Col className="d-grid gap-2">
                                    <Button variant="primary" onClick={()=>setEdit(true)}>
                                        Edit
                                    </Button>
                                </Col>
                            </Row>
                            :
                            <Row>
                                <Col className="d-grid gap-2">
                                    <Button variant="primary" onClick={saveProfile}>
                                        Save
                                    </Button>
                                </Col>
                                <Col className="d-grid gap-2">
                                    <Button variant="primary" onClick={resetProfile}>
                                        Cancel
                                    </Button>
                                </Col>
                            </Row>
                        }
                    </Form>
                </Card.Body>
            </Card>
            {/* endregion */}

            {/* region change password */}
            <Modal show={changePasswordModal} fullscreen={true} onHide={() => setChangePasswordModal(false)}>
                <Modal.Header closeButton>
                    <Modal.Title>Reset Password</Modal.Title>
                </Modal.Header>
                <Modal.Body>
                    <Card style={{textAlign:"end"}}>
                        <Card.Body>
                            <Row>
                                <Col>
                                    <FloatingLabel controlId="oldPassword" label="Old Password">
                                        <Form.Control type="password" onChange={(e)=>setOldPassword(e.target.value)}/>
                                    </FloatingLabel>
                                </Col>
                            </Row><br/>
                            <Row>
                                <Col>
                                    <FloatingLabel controlId="newPassword1" label="New Password">
                                        <Form.Control type="password" onChange={(e)=>setNewPassword1(e.target.value)}/>
                                    </FloatingLabel>
                                </Col>
                            </Row><br/>
                            <Row>
                                <Col>
                                    <FloatingLabel controlId="newPassword2" label="Confirm New Password">
                                        <Form.Control type="password" onChange={(e)=>setNewPassword2(e.target.value)}/>
                                    </FloatingLabel>
                                </Col>
                            </Row><br/>
                            <Button onClick={changePassword}>
                                Change Password
                            </Button>
                        </Card.Body>
                    </Card>
                </Modal.Body>
            </Modal>
            {/* endregion */}

            {/* region shared */}
            <ToastContainer className="p-3" position="bottom-center">
                <Toast onClose={() => setShowToast(false)} show={showToast} delay={10000} autohide>
                    <Toast.Header>
                        <strong className="me-auto">Alert</strong>
                        <small>Just now</small>
                    </Toast.Header>
                    <Toast.Body>{toastMessage}</Toast.Body>
                </Toast>
            </ToastContainer>
            {/* endregion */}
        </Container>
    )
}

export default UserProfile;