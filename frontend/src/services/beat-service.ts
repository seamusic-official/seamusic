import { AxiosResponse } from 'axios';
import $api from '@/shared/utils/http';

export class BeatService {
	static async all(): Promise<AxiosResponse> {
		return $api.get('beats/');
	}

	static async add(data: any): Promise<AxiosResponse> {
		return $api.post('beats/', data, {
			headers: {
				'Content-Type': 'multipart/form-data',
			},
		});
	}

	static async update_picture(id: number, data: any): Promise<AxiosResponse> {
		return $api.post(`beats/picture/${id}`, data, {
			headers: {
				'Content-Type': 'multipart/form-data',
			},
		});
	}

	static async update(id: number, data: any): Promise<AxiosResponse> {
		return $api.post(`beats/release/${id}`, data);
	}

	static async delete(id: number): Promise<AxiosResponse> {
		return $api.delete(`beats/${id}`);
	}
	static async get_one(id: number): Promise<AxiosResponse> {
		return $api.get(`beats/${id}`);
	}

	static async my(): Promise<AxiosResponse> {
		return $api.get(`beats/my`);
	}
}
