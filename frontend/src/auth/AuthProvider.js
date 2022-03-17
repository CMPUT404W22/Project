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
     * @param username
     * @param password {string}
     * @param failure {function}
     * @param always {function}
     */
    signIn(username, password) {
        Ajax.postNoAuth(
            "service/authors/login/",
            {username: username, password: password}
        ).then(function (response) {
            let url = response.data.id
            let lastSegment = url.split("/").pop()
            console.log("user: ", lastSegment)
            AuthProvider.Identity = new Identity(username, password, "user");
            AuthProvider.Identity.StoreIdentity();

            window.location.assign("/home");
        }).catch(function (error) {
            alert("Login Failed")
        }).then(function () {

        });
    },
    /**
     * Sign out then run callback
     * @param callback {function}
     */
    signOut(callback = () => window.location.assign("/")) {
        // clear identity
        AuthProvider.Identity = new Identity();
        Identity.ClearIdentity();

        // run callback
        callback()
    }
};

export {AuthProvider};
