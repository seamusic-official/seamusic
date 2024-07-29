import React from 'react';
import { useRouter } from 'next/navigation';
import { useAppDispatch } from '@/shared/hooks/redux';
import { clearAuthData } from '@/store/reducers/authSlice';

export function Logout() {
	const dispatch = useAppDispatch();
	const navigate = useRouter();

	const handleLogout = () => {
		localStorage.removeItem('accessToken');
		document.cookie =
			'refreshToken=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;';
		dispatch(clearAuthData());
		navigate.push('/auth/login');
	};

	return (
		<a
			className="text-gray-200 text-sm font-bold hover:text-white capitalize"
			onClick={handleLogout}>
			Logout
		</a>
	);
}
