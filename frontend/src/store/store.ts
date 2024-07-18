import { combineReducers } from 'redux';
import authSlice from './reducers/authSlice';
import storage from 'redux-persist/lib/storage';
import playerSlice from './reducers/playerSlice';
import searchSlice from './reducers/searchSlice';
import { configureStore } from '@reduxjs/toolkit';
import { persistReducer, persistStore } from 'redux-persist';


const persistConfig = {
  key: 'root',
  storage,
};

const rootReducer = combineReducers({
  player: playerSlice,
  auth: authSlice,    
  search: searchSlice,    
});

const persistedReducer = persistReducer(persistConfig, rootReducer); // Corrected to use rootReducer

export const store = configureStore({
  reducer: persistedReducer,
});

export const persistor = persistStore(store);

export const setupStore = () => {
  return { store, persistor }; // Return both store and persistor
};

export type RootState = ReturnType<typeof rootReducer>;
export type AppStore = ReturnType<typeof setupStore>;
export type AppDispatch = AppStore['store']['dispatch']; // Updated to 'store' property

// Exporting the slices for usage in components if needed
export { playerSlice, authSlice };
