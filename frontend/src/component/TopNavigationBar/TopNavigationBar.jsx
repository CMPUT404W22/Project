import React, {useState} from "react";

import {Button, Container, Nav, Navbar, NavDropdown, NavItem} from "react-bootstrap";

import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faSignOutAlt, faUserCircle } from '@fortawesome/free-solid-svg-icons'

import Identity from "../../model/Identity";
import {AuthProvider} from "../../auth/AuthProvider";

/**
 * Top Navigation Bar
 * @param prop
 * @returns {JSX.Element}
 * @constructor
 */
function TopNavigationBar(prop) {
    // region listen for identity change
    let UserIdentity = Identity.GetIdentity();
    const [auth, setAuth] = useState(UserIdentity.IsAuthenticated()); // determine if authorized, from context or however you're doing it

    // listen for change in auth state
    window.addEventListener("storage", () => {
        UserIdentity = Identity.GetIdentity(); // Get new updated identity
        if (auth !== UserIdentity.IsAuthenticated()) {
            setAuth(UserIdentity.IsAuthenticated());
        }
    });
    // endregion

    /**
     * Sign out
     */
    function signOut() {
        AuthProvider.signOut();
    }

    return (
        <Navbar bg="light" expand="lg" fixed="top">
            <Container fluid>
                <Navbar.Brand href="/home">
                    Social Network
                </Navbar.Brand>
                <Navbar.Toggle aria-controls="navbarScroll"/>
                <Navbar.Collapse id="navbarScroll">
                    <Nav
                        className="me-auto my-2 my-lg-0"
                        style={{maxHeight: '100px'}}
                        navbarScroll
                    >
                        {auth ?
                            <>
                                <NavItem>
                                    <Nav.Link href="/home">Home</Nav.Link>
                                </NavItem>
                                <NavItem>
                                    <Nav.Link href="/inbox">Inbox</Nav.Link>
                                </NavItem>
                            </>
                            :
                            ""
                        }
                        <NavItem>
                            <Nav.Link href="/about">About</Nav.Link>
                        </NavItem>
                    </Nav>
                    {auth ?
                        <Nav className="d-flex">
                            <NavDropdown title="My Account" id="basic-nav-dropdown" align="end">
                                <NavDropdown.Item href="/user-profile">
                                    <FontAwesomeIcon icon={faUserCircle} style={{paddingRight:10}}/>
                                    My Profile
                                </NavDropdown.Item>
                                <NavDropdown.Divider />
                                <NavDropdown.Item onClick={signOut}>
                                    <FontAwesomeIcon icon={faSignOutAlt} style={{paddingRight:10}}/>
                                    Sign Out
                                </NavDropdown.Item>
                            </NavDropdown>
                        </Nav>
                        :
                        <Nav className="d-flex">
                            <Button onClick={() => window.location.assign("/sign-in")}>
                                Sign in
                            </Button>
                        </Nav>
                    }
                </Navbar.Collapse>
            </Container>
        </Navbar>
    );
}

export default TopNavigationBar;