import { AxiosResponse } from "axios";
import $api from "../http";

export default class KitService {
    static async all(): Promise<AxiosResponse> {
        return $api.get("kits/");
    }
    
    static async add(data: any): Promise<AxiosResponse> {
        return $api.post("kits/", data, {
            headers: {
                'Content-Type': 'multipart/form-data'
            }
        });
    }ц
    
    static async update_picture(id: number, data): Promise<AxiosResponse> {
        return $api.post(`kits/picture/${id}`, data, {
            headers: {
                'Content-Type': 'multipart/form-data'
            }
        });
    }

    static async update(id: number, data): Promise<AxiosResponse> {
        return $api.post(`kits/release/${id}`, data);
    }

    static async delete(id: number): Promise<AxiosResponse> {
        return $api.delete(`kits/${id}`);
    }
    static async get_one(id: number): Promise<AxiosResponse> {
        return $api.get(`kits/${id}`);
    }

    static async my(): Promise<AxiosResponse> {
        return $api.get(`kits/my`);
    }
}
