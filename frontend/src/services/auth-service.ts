import { AxiosResponse } from 'axios';
import $api from '@/shared/utils/http';

export class AuthService {
	static async register(
		username: string,
		roles: string[],
		birthday: string,
		password: string,
		email: string
	): Promise<AxiosResponse> {
		return $api.post('auth/register/', {
			password,
			email,
			username,
			roles,
			birthday,
		});
	}
	static async login(email: string, password: string): Promise<AxiosResponse> {
		return $api.post('auth/login/', {
			email,
			password,
		});
	}

	static async get_users(): Promise<AxiosResponse> {
		return $api.get('auth/users/');
	}
	static async update_user(
		id: number,
		username: string
	): Promise<AxiosResponse> {
		return $api.put(`auth/users/${id}`, {
			username: username,
		});
	}
	static async update_user_picture(
		id: number,
		data: any
	): Promise<AxiosResponse> {
		return $api.put(`auth/users/picture/${id}`, data, {
			headers: {
				'Content-Type': 'multipart/form-data',
			},
		});
	}
	static async delete_user(id: number): Promise<AxiosResponse> {
		return $api.get(`auth/users/${id}`);
	}
	static async get_user(id: number): Promise<AxiosResponse> {
		return $api.get(`auth/users/${id}`);
	}

	static async get_artists(): Promise<AxiosResponse> {
		return $api.get('auth/users/artists');
	}
	static async update_artist(): Promise<AxiosResponse> {
		return $api.get('auth/users/producers');
	}
	static async delete_artist(): Promise<AxiosResponse> {
		return $api.get('auth/users/producers');
	}
	static async get_artist(): Promise<AxiosResponse> {
		return $api.get('auth/users/producers');
	}

	static async get_producers(): Promise<AxiosResponse> {
		return $api.get('auth/users/producers');
	}
	static async update_producer(id: number, data: any): Promise<AxiosResponse> {
		return $api.put('auth/users/producers', {
			data,
		});
	}
	static async delete_producer(id: number): Promise<AxiosResponse> {
		return $api.delete(`auth/users/producers/${id}`);
	}
	static async get_producer(id: number): Promise<AxiosResponse> {
		return $api.get(`auth/users/producers/${id}`);
	}
}
