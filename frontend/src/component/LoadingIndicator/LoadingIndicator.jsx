import React, {useEffect, useState} from "react";
import {Spinner} from "react-bootstrap";

/**
 * Loading Indicator
 * use disableScreen property to disable whole screen
 * use show property to control show
 * @param prop
 * @returns {JSX.Element|string}
 * @constructor
 */
function LoadingIndicator(prop) {
    const [show, setShow] = useState(prop.show)
    const [disableScreen, setDisableScreen] = useState(prop.disableScreen)
    
    useEffect(() => {
        setShow(prop.show)
        setDisableScreen(prop.disableScreen)
    }, [prop])

    const fullScreenStyle = {
        position: "absolute",
        height: "100vh",
        width: "100vw",
        opacity: 0.8,
        top: 0,
        left: 0,
        zIndex: 999,
        background: "white"
    }

    const centerSpinnerStyle = {
        position: "absolute",
        top: "50%",
        left: "47%",
        marginRight: "-50%",
    }

    return (
        show ?
            <div style={disableScreen ? fullScreenStyle : {}}>
                <Spinner animation="border" style={centerSpinnerStyle}/>
            </div>
            :
            ""
    );
}

export default LoadingIndicator;