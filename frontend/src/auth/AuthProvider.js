import Identity from "../model/Identity";
import {Ajax} from "../utility/Ajax";

/**
 * Authentication Provider
 * @type {{signIn(string, string, Function): void, signOut(Function): void, Identity: Identity}}
 */
const AuthProvider = {
    Identity: Identity.GetIdentity(),
    /**
     * Sign in using given username and password, the run callback
     * @param email {string}
     * @param password {string}
     * @param failure {function}
     * @param always {function}
     */
    signIn(username, password, failure = () => {}, always = () => {}) {
        Ajax.post(
            "api/auth/login/",
            JSON.stringify({username: username, password: password}),
            (resp)=> {
                // create identity
                AuthProvider.Identity = new Identity(
                    username, password
                );

                // save identity to localStorage
                AuthProvider.Identity.StoreIdentity();

                // Go to user home
                window.location.assign("/user-home")
            },
            failure,
            always
        );
    },
    /**
     * Sign out then run callback
     * @param callback {function}
     */
    signOut(callback = () => window.location.assign("/")) {
        // clear identity
        AuthProvider.Identity = new Identity();
        Identity.ClearIdentity();

        // clear refresh timer
        clearTimeout();

        // run callback
        callback()
    },
    /**
     * Refresh token
     * @param debug {boolean} print token if debug
     * @returns {Promise<void>}
     */
    async refreshToken(debug=false) {
        try {
            if (AuthProvider.Identity.refreshToken === "" || AuthProvider.Identity.refreshToken == null) {
                throw Error("Attempt to refresh access token without a refresh token")
            }

            await Ajax.postNoRefresh(
                "api/auth/token/refresh/",
                JSON.stringify({refresh:AuthProvider.Identity.refreshToken}),
                (resp)=>{
                    if (debug) {
                        console.log(resp);
                    }

                    localStorage.setItem("token", resp['access']);
                    localStorage.setItem("refreshToken", resp['refresh']);
                },
                (resp)=>{
                    console.log("You are signed out");
                    AuthProvider.signOut();
                },
                ()=>{}
            );
        }
        catch(e) {
            throw(e)
        }
    },
    /**
     * Update user password
     * @param oldPassword {string}
     * @param newPassword {string}
     * @param success {function} success callback
     * @param failure {function} success callback
     */
    updatePassword(oldPassword, newPassword, success = ()=>{}, failure = ()=>{}) {
        Ajax.post(
            "api/auth/password/update/",
            JSON.stringify({
                "old_password": oldPassword,
                "new_password": newPassword
            }),
            success,
            failure
        )
    }
};

export { AuthProvider };
