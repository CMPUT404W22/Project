import $ from "jquery";
import {AuthProvider} from "../auth/AuthProvider";

const BackendAddress = "http://127.0.0.1:8000/";

class Ajax {
    /**
     * Ajax post request
     * @param endpoint {string}
     * @param data {string}
     * @param success {function}
     * @param failure {function}
     * @param always {function}
     */
    static post (endpoint, data, success = ()=>{}, failure = ()=>{}, always = ()=>{}) {
        AuthProvider.refreshToken().then(() => {
            $.ajax({
                url: BackendAddress + endpoint,
                type: 'POST',
                contentType: "application/json",
                dataType: "json",
                data: data,
                headers: {"Authorization": `Bearer ${localStorage.getItem('token')}`},
                success: success,
                error: failure,
                always: always
            });
        });
    }

    /**
     * Ajax get request
     * @param endpoint {string}
     * @param success {function}
     * @param failure {function}
     * @param always {function} 
     * */
    static get(endpoint, success = () => { }, failure = () => { }, always = () => { }) {
        AuthProvider.refreshToken().then(() => {
            $.ajax({
                url: BackendAddress + endpoint,
                type: 'GET',
                headers: { "Authorization": `Bearer ${localStorage.getItem('token')}` },
                success: success,
                error: failure,
                always: always
            });
        });
    }

    /**
     * Ajax post request with no token refresj
     * @param endpoint {string}
     * @param data {string}
     * @param success {function}
     * @param failure {function}
     * @param always {function}
     * @returns {Promise<*>}
     */
    static postNoRefresh (endpoint, data, success = ()=>{}, failure = ()=>{}, always = ()=>{}) {
        return $.ajax({
            url: BackendAddress + endpoint,
            type: 'POST',
            contentType: "application/json",
            dataType: "json",
            data: data,
            headers: {"Authorization": `Bearer ${localStorage.getItem('token')}`},
            success: success,
            error: failure,
            always: always
        });
    }

    /**
  * Ajax put request
  * @param endpoint {string}
  * @param data {string}
  * @param success {function}
  * @param failure {function}
  * @param always {function}
  */
    static put (endpoint, data, success = () => { }, failure = () => { }, always = () => { }) {
        AuthProvider.refreshToken().then(() => {
            $.ajax({
                url: BackendAddress + endpoint,
                type: 'PUT',
                contentType: "application/json",
                dataType: "json",
                data: data,
                headers: { "Authorization": `Bearer ${localStorage.getItem('token')}` },
                success: success,
                error: failure,
                always: always
            });
        })
    }
}

export {Ajax}
