import { AxiosResponse } from "axios";
import $api from "../http";

export default class BeatService {
    static async all(): Promise<AxiosResponse> {
        return $api.get("beats/all/");
    }
    
    static async add(data: any): Promise<AxiosResponse> {
        return $api.post("beats/add/", data, {
            headers: {
                'Content-Type': 'multipart/form-data'
            }
        });
    }
    
    static async update_picture(id: number, data): Promise<AxiosResponse> {
        return $api.post(`beats/picture/${id}`, data, {
            headers: {
                'Content-Type': 'multipart/form-data'
            }
        });
    }

    static async update(id: number, data): Promise<AxiosResponse> {
        return $api.post(`beats/release/${id}`, data, {
            headers: {
                'Content-Type': 'multipart/form-data'
            }
        });
    }
    static async delete(id: number): Promise<AxiosResponse> {
        return $api.delete(`beats/delete/${id}`);
    }

    static async my(): Promise<AxiosResponse> {
        return $api.get(`beats/my`);
    }
}
