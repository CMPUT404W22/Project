import React, {useState} from "react";

import {Button, Card, Container, Form, InputGroup, Modal, Toast, ToastContainer} from "react-bootstrap";

import {Link} from "react-router-dom";

import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faKey, faUser } from '@fortawesome/free-solid-svg-icons'

import {AuthProvider} from "../auth/AuthProvider";


/**
 * Sign in page
 * @param prop
 * @returns {JSX.Element}
 * @constructor
 */
function SignIn(prop) {
    // region sign in page
    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");
    const [failed, setFailed] = useState(false);

    /**
     * Sign in
     */
    function signIn() {
        AuthProvider.signIn(username, password);
    }
    // endregion

    // region forgot password modal
    const [showForgotPasswordModal, setShowForgotPasswordModal] = useState(false);
    const [forgotPasswordEmail, setForgotPasswordEmail] = useState("");
    const [passwordResetToken, setPasswordResetToken] = useState("");
    const [tokenSent, setTokenSent] = useState(false);
    const [newPassword, setNewPassword] = useState("");
    const [newPasswordRepeat, setNewPasswordRepeat] = useState("");

    /**
     * Request a password reset token to be sent to the user through email
     */
    function requestPasswordResetToken() {
        // TODO use email to request a password reset token
        // TODO

        // TODO test code
        setTokenSent(true)
    }

    /**
     * Request a password reset
     */
    function requestPasswordReset() {

    }
    // endregion

    return (
        <Container style={{maxWidth: 800}}>
            {/* region toast */}
            <ToastContainer position={"bottom-center"} style={{paddingBottom:20}}>
                <Toast onClose={() => setFailed(false)} show={failed} delay={10000} autohide>
                    <Toast.Body><i>Sign in failed. Please check your username and password. <Link to="" onClick={()=>setShowForgotPasswordModal(true)}>Forgot your password?</Link></i></Toast.Body>
                </Toast>
            </ToastContainer>
            {/* endregion */}

            {/* region sign in page */}
            <Card>
                <Card.Body>
                    <Card.Title>Sign in to your account</Card.Title>
                    <Form>
                        <Form.Group className="mb-3" controlId="formBasicUsername">
                            <Form.Label>Username</Form.Label>
                            <InputGroup>
                                <InputGroup.Text>
                                    <FontAwesomeIcon icon={faUser}/>
                                </InputGroup.Text>
                                <Form.Control type="username" placeholder="Username"
                                              onChange={(e) => setUsername(e.target.value)} required/>
                            </InputGroup>
                        </Form.Group>
                        <Form.Group className="mb-3" controlId="formBasicPassword">
                            <Form.Label>Password</Form.Label>
                            <InputGroup>
                                <InputGroup.Text>
                                    <FontAwesomeIcon icon={faKey}/>
                                </InputGroup.Text>
                                <Form.Control type="password" placeholder="Password"
                                              onChange={(e) => setPassword(e.target.value)} required/>
                            </InputGroup>
                        </Form.Group>
                        <Form.Group className="mb-3">
                            <Form.Text className="text-muted">
                                <Link to="" onClick={()=>setShowForgotPasswordModal(true)}>Forgot Password?</Link>
                            </Form.Text>
                        </Form.Group>
                        <Form.Group className="mb-3">
                            <Form.Text className="text-muted">
                                <Link to="/sign-up">Don't have an account? Sign up here -></Link>
                            </Form.Text>
                        </Form.Group>
                        <Button variant="primary" onClick={() => signIn()}>
                            Sign in
                        </Button>
                    </Form>
                </Card.Body>
            </Card>
            {/* endregion */}

            {/* region forgot password modal */}
            <Modal show={showForgotPasswordModal} fullscreen={true} onHide={() => setShowForgotPasswordModal(false)}>
                <Modal.Header closeButton>
                    <Modal.Title>Reset Password</Modal.Title>
                </Modal.Header>
                <Modal.Body>
                    <Card>
                        <Card.Body>
                            <Form>
                                <Form.Group className="mb-3" controlId="formBasicEmail">
                                    <Form.Label>Email Address</Form.Label>
                                    <InputGroup>
                                        <InputGroup.Text>
                                            <FontAwesomeIcon icon={faUser}/>
                                        </InputGroup.Text>
                                        <Form.Control type="username" placeholder="Enter username"
                                                      onChange={(e) => setForgotPasswordEmail(e.target.value)}/>
                                    </InputGroup>
                                </Form.Group>
                                <Button variant="primary" onClick={()=>requestPasswordResetToken(forgotPasswordEmail)}>
                                    Request Password Reset Token
                                </Button>
                            </Form>
                        </Card.Body>
                    </Card>
                    <br/>
                    <Card>
                        <Card.Body>
                            <Form>
                                <fieldset disabled={!tokenSent}>
                                    <Form.Group className="mb-3">
                                        <Form.Label>Password Reset Token</Form.Label>
                                        <InputGroup>
                                            <InputGroup.Text>
                                                <FontAwesomeIcon icon={faKey}/>
                                            </InputGroup.Text>
                                            <Form.Control type="password" placeholder="Token"
                                                          onChange={(e) => setPasswordResetToken(e.target.value)}/>
                                        </InputGroup>
                                    </Form.Group>
                                    <Form.Group className="mb-3">
                                        <Form.Label>New Password</Form.Label>
                                        <InputGroup>
                                            <InputGroup.Text>
                                                <FontAwesomeIcon icon={faKey}/>
                                            </InputGroup.Text>
                                            <Form.Control type="password" placeholder="New Password"
                                                          onChange={(e) => setNewPassword(e.target.value)}/>
                                        </InputGroup>
                                    </Form.Group>
                                    <Form.Group className="mb-3">
                                        <Form.Label>Confirm New Password</Form.Label>
                                        <InputGroup>
                                            <InputGroup.Text>
                                                <FontAwesomeIcon icon={faKey}/>
                                            </InputGroup.Text>
                                            <Form.Control type="password" placeholder="New Password"
                                                          onChange={(e) => setNewPasswordRepeat(e.target.value)}/>
                                        </InputGroup>
                                    </Form.Group>
                                    <Button variant="primary" onClick={() => requestPasswordReset(forgotPasswordEmail, newPassword, newPasswordRepeat, passwordResetToken)}>
                                        Submit
                                    </Button>
                                </fieldset>
                            </Form>
                        </Card.Body>
                    </Card>
                </Modal.Body>
            </Modal>
            {/* endregion */}
        </Container>
    );
}

export default SignIn;