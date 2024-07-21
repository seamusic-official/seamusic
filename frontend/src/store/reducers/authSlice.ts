import { createSlice } from '@reduxjs/toolkit';

type IUser = {
	isAuthenticated: boolean;
	accessToken: string;
	refreshToken: string;
	expiresInToken: number | null;
	user: {
		id: number | null;
		username: string;
		email: string;
		picture_url: string;
		birthday: string[] | null;
		registered_at: number | null;
		role: object | null;
	}; // Объект с информацией о количестве фолловеров
};

const initialState = <IUser>{
	isAuthenticated: true,
	accessToken: '',
	refreshToken: '',
	expiresInToken: null,
	user: {
		id: null,
		username: '',
		email: '',
		picture_url: '',
		birthday: null,
		registered_at: null,
		role: null,
	},
};

const authSlice = createSlice({
	name: 'auth',
	initialState,
	reducers: {
		setAuthData: (state, action) => {
			state.isAuthenticated = true;
			state.accessToken = action.payload.accessToken;
			state.refreshToken = action.payload.refreshToken;
			state.expiresInToken = action.payload.expiresInToken;
			state.user = { ...action.payload.user };
		},
		updateAuthData: (state, action) => {
			state.user = { ...action.payload };
		},
		clearAuthData: (state) => {
			state.isAuthenticated = false;
			state.accessToken = '';
			state.refreshToken = '';
			state.expiresInToken = null;
			state.user = {
				id: null,
				username: '',
				email: '',
				picture_url: '',
				birthday: null, // Массив объектов с URL изображений
				registered_at: null,
				role: null, // Объект с информацией о количестве фолловеров
			};
		},
	},
});

export const { setAuthData, clearAuthData, updateAuthData } = authSlice.actions;

export default authSlice.reducer;
