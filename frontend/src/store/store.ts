import { configureStore } from '@reduxjs/toolkit';
import playerSlice from './reducers/playerSlice';
import authSlice from './reducers/authSlice';
import searchSlice from './reducers/searchSlice';

export const makeStore = () => {
	return configureStore({
		reducer: { player: playerSlice, auth: authSlice, search: searchSlice },
	});
};

// Infer the type of makeStore
export type AppStore = ReturnType<typeof makeStore>;
// Infer the `RootState` and `AppDispatch` types from the store itself
export type RootState = ReturnType<AppStore['getState']>;
export type AppDispatch = AppStore['dispatch'];
