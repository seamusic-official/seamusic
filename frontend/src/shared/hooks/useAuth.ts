import axios from 'axios';
import React, { useEffect, useState } from 'react';
import { useAppDispatch } from './redux';
import { setAuthData } from '../../store/reducers/authSlice';

export default function useAuth(code: string) {
	const dispatch = useAppDispatch();
	useEffect(() => {
		const fetchData = async () => {
			try {
				const response = await axios.post(
					`http://localhost:8000/auth/callback?code=${code}`
				);
				const { access_token, refresh_token, user_data } = response.data;
				console.log({ access_token, refresh_token, user_data });

				// Диспатчим action setAuthData для сохранения данных в store
				dispatch(
					setAuthData({
						accessToken: access_token,
						refreshToken: refresh_token,
						expiresInToken: null, // Например, вы не получаете expiresIn в этом запросе
						user: user_data,
					})
				);
			} catch (error) {
				console.error('Error fetching data:', error);
			}
		};

		if (code) {
			fetchData();
		}
	}, [code, dispatch]); // Убедитесь, что dispatch добавлен в зависимости useEffect
}
