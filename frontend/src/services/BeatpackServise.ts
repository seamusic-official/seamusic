import { AxiosResponse } from "axios";
import $api from "../http";

export default class BeatpackService {
    static async all(): Promise<AxiosResponse> {
        return $api.get("beats/beatpacks/all");
    }
    
    static async add(data: any): Promise<AxiosResponse> {
        return $api.post("beats/beatpacks/add/", data, {
            headers: {
                'Content-Type': 'multipart/form-data'
            }
        });
    }
    static async get_one(id): Promise<AxiosResponse> {
        return $api.get(`beats/beatpacks/${id}`);
    }
    static async update(id: number, data: any): Promise<AxiosResponse> {
        return $api.put(`beats/beatpacks/update/${id}`, data);
    }
}
