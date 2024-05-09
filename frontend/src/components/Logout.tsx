import React from 'react';
import { useNavigate } from 'react-router-dom';
import { useAppDispatch } from '../hooks/redux';
import { clearAuthData } from '../store/reducers/authSlice';

export default function Logout() {
  const dispatch = useAppDispatch();
  const navigate = useNavigate();

  const handleLogout = () => {
    localStorage.removeItem('accessToken');
    document.cookie = "refreshToken=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;";
    dispatch(clearAuthData());
    navigate('/auth/login');
  };

  return (
    <a className="block px-4 py-2 text-gray-300 text-sm font-extrabold hover:text-white" onClick={handleLogout}>
      Logout
    </a>
  );
}
