import React, { useState } from "react";
import { Button, Col, Container, Form, Offcanvas, Row } from "react-bootstrap";

import hotkeys from 'hotkeys-js';
import Identity from "../../model/Identity";
import Global from "../../utility/Global";
import {AuthProvider} from "../../auth/AuthProvider";
import {Ajax} from "../../utility/Ajax";

function fakeSignIn() {
    AuthProvider.signIn("123", "123");
    let i = new Identity("token", 1,
        "fakeUser", "fake",
        "user", "fakeUser.foo.com",
        "1231231234");
    i.StoreIdentity();
    console.log("signed in")
}

function signOut() {
    AuthProvider.signOut();
    console.log("signed out")
}

function changeRole(role) {
    localStorage.setItem("role", role.toString());
    console.log(`role changed to ${role}`);
}

function printIdentity() {
    console.log(Identity.GetIdentity());
}

function testBackendAuth(){
    Ajax.get(
        "api/auth/test/",
        (resp) => console.log(resp),
        (resp) => console.log(resp),
        () => {}
    );
}

function refreshToken() {
    AuthProvider.refreshToken(true);
}

function DevMenu(prop) {
    const [show, setShow] = useState(false);

    const handleClose = () => setShow(false);
    const handleShow = () => setShow(true);

    const [role, setRole] = useState(0);

    hotkeys('shift+alt+1', function (event, handler) {
        // Prevent the default refresh event under WINDOWS system
        event.preventDefault()
        handleShow();
        console.log("Dev Menu Activated")
    });

    return (
        <div>
            {Global.DEBUG ?
                <Offcanvas show={show} onHide={handleClose}>
                    <Offcanvas.Header closeButton>
                        <Offcanvas.Title>Dev Menu</Offcanvas.Title>
                    </Offcanvas.Header>
                    <Offcanvas.Body>
                        <Container>
                            {/* region dev sign in */}
                            <Row>
                                <Button onClick={fakeSignIn}>
                                    Fake Sign in
                                </Button>
                            </Row>
                            <br />
                            <Row>
                                <Button onClick={signOut}>
                                    Sign out
                                </Button>
                            </Row>
                            <br />
                            {/* endregion */}
                            {/* region dev user role change */}
                            <Row>
                                <Col className="col-md-7">
                                    <Form.Select aria-label="Default select example"
                                        onChange={(e) => setRole(parseInt(e.target.value))}>
                                        <option value="0">Participant</option>
                                        <option value="1">Volunteer</option>
                                        <option value="2">Staff</option>
                                        <option value="3">Admin</option>
                                    </Form.Select>
                                </Col>
                                <Col className="col-md-5">
                                    <Button onClick={() => changeRole(role)}>
                                        Change role
                                    </Button>
                                </Col>
                            </Row>
                            <br />
                            {/* endregion */}
                            {/* region identity */}
                            <Row>
                                <Button onClick={printIdentity}>
                                    Print Identity
                                </Button>
                            </Row>
                            <br />
                            {/* endregion */}
                            {/* region testBackendAuth */}
                            <Row>
                                <Button onClick={testBackendAuth}>
                                    Test Auth State
                                </Button>
                            </Row>
                            <br />
                            {/* endregion */}
                            {/* region testBackendAuth */}
                            <Row>
                                <Button onClick={refreshToken}>
                                    RefreshToken
                                </Button>
                            </Row>
                            <br />
                            {/* endregion */}
                            {/* region identity */}
                            <Row>
                                <Button onClick={printIdentity}>
                                    Print Identity
                                </Button>
                            </Row>
                            <br/>
                            {/* endregion */}
                            {/* region testBackendAuth */}
                            <Row>
                                <Button onClick={testBackendAuth}>
                                    Test Auth State
                                </Button>
                            </Row>
                            <br/>
                            {/* endregion */}
                            {/* region testBackendAuth */}
                            <Row>
                                <Button onClick={refreshToken}>
                                    RefreshToken
                                </Button>
                            </Row>
                            <br/>
                            {/* endregion */}
                        </Container>
                    </Offcanvas.Body>
                </Offcanvas>
                : ""}
        </div>

    );
}

export default DevMenu;