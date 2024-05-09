import { AxiosResponse } from "axios";
import $api from "../http";

export default class AuthService {
    static async register(username: string, role: string, birthday: string, password: string, email: string): Promise<AxiosResponse> {
        return $api.post("auth/register/", {
            password,
            email,
            username,
            role,
            birthday,
        });
    }
    static async login(email: string, password: string): Promise<AxiosResponse> {
        return $api.post("auth/login/", {
            email,
            password,
        });
    }
    static async artists(): Promise<AxiosResponse> {
        return $api.get("auth/users/artists");
    }
}
