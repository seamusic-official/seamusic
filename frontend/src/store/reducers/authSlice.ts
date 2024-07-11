import { createSlice } from '@reduxjs/toolkit';

const initialState = {
  isAuthenticated: false,
  accessToken: null as string | null,
  refreshToken: null as string | null,
  expiresInToken: null as number | null,
  user: {
    id: null as number | null,
    username: null as string | null,
    email: null as string | null,
    picture_url: null as string | null,
    birthday: null,
    registered_at: null,
    role: null, // Объект с информацией о количестве фолловеров
  } 
};

const authSlice = createSlice({
  name: 'auth',
  initialState,
  reducers: {
    setAuthData: (state, action) => {
      state.isAuthenticated = true,
      state.accessToken = action.payload.accessToken;
      state.refreshToken = action.payload.refreshToken;
      state.expiresInToken = action.payload.expiresInToken;
      state.user = { ...action.payload.user };
    },
    updateAuthData: (state, action) => {
      state.user = { ...action.payload };
    },
    clearAuthData: (state) => {
      state.isAuthenticated = false,
      state.accessToken = null;
      state.refreshToken = null;
      state.expiresInToken = null;
      state.user = {
        id: null,
        username: null,
        email: null,
        picture_url: null,
        birthday: null, // Массив объектов с URL изображений
        registered_at: null,
        role: null, // Объект с информацией о количестве фолловеров
      } 
    },
  },
});

export const { setAuthData, clearAuthData, updateAuthData } = authSlice.actions;

export default authSlice.reducer;
