import { User } from './user';

export type AuthResponseType = {
	accessToken: string;
	refreshToken: string;
	user: User;
};
