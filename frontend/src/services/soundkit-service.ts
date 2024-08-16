import { AxiosResponse } from 'axios';
import $api from '@/shared/utils/http';

export class SoundkitService {
	static async all(): Promise<AxiosResponse> {
		return $api.get('soundkits/');
	}

	static async add(data: any): Promise<AxiosResponse> {
		return $api.post('soundkits/', data, {
			headers: {
				'Content-Type': 'multipart/form-data',
			},
		});
	}

	static async update_picture(id: number, data: any): Promise<AxiosResponse> {
		return $api.post(`soundkits/picture/${id}`, data, {
			headers: {
				'Content-Type': 'multipart/form-data',
			},
		});
	}

	static async update(id: number, data: any): Promise<AxiosResponse> {
		return $api.post(`soundkits/release/${id}`, data);
	}

	static async delete(id: number): Promise<AxiosResponse> {
		return $api.delete(`soundkits/${id}`);
	}
	static async get_one(id: number): Promise<AxiosResponse> {
		return $api.get(`soundkits/${id}`);
	}

	static async my(): Promise<AxiosResponse> {
		return $api.get(`soundkits/my`);
	}
}
