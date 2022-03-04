import $ from "jquery";
import {AuthProvider} from "../auth/AuthProvider";
import axios from "axios";

const BackendAddress = "http://127.0.0.1:8000/";

class Ajax {
    /**
     * Get
     * @param path {string}
     * @returns {Promise<AxiosResponse<any>>}
     */
    static async get(path){
        return axios.get(BackendAddress + path, {
            auth: {
                username: localStorage.getItem("username"),
                password: localStorage.getItem("password")
            }
        });
    }

    /**
     * Post
     * @param path {string}
     * @param data {object}
     * @returns {Promise<AxiosResponse<any>>}
     */
    static async post(path, data){
        return axios.post(BackendAddress + path, data, {
            auth: {
                username: localStorage.getItem("username"),
                password: localStorage.getItem("password")
            }
        });
    }

    /**
     * Post No Auth
     * @param path {string}
     * @param data {object}
     * @returns {Promise<AxiosResponse<any>>}
     */
    static async postNoAuth(path, data){
        return axios.post(BackendAddress + path, data);
    }

    /**
     * Put
     * @param path {string}
     * @param data {object}
     * @returns {Promise<AxiosResponse<any>>}
     */
    static async put(path, data){
        return axios.put(BackendAddress + path, data, {
            auth: {
                username: localStorage.getItem("username"),
                password: localStorage.getItem("password")
            }
        });
    }

    /**
     * Delete
     * @param path {string}
     * @returns {Promise<AxiosResponse<any>>}
     */
    static async delete(path){
        return axios.put(BackendAddress + path, {
            auth: {
                username: localStorage.getItem("username"),
                password: localStorage.getItem("password")
            }
        });
    }
}

export {Ajax}
