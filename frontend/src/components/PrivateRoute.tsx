import React from 'react';
import { Route, redirect } from 'react-router-dom';
import { useAppSelector } from '../hooks/redux';

const PrivateRoute = ({ element: Component, path }) => {
    const isAuthenticated = useAppSelector((state) => state.auth.isAuthenticated)

    return (
        <Route
            element={
                isAuthenticated ? <Component /> : redirect("/auth/login")
            }
            path={path}

        />
    );
};

export default PrivateRoute;