import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App.tsx'
import './index.css'
import {
  BrowserRouter,
  Routes,
  Route,
} from 'react-router-dom';
import AlbumDetail from './pages/albums/AlbumDetail.tsx';
import Profile from './pages/profile/Profile.tsx';
import Studio from './pages/dashboard/Studio.tsx';
import Messages from './pages/messages/Messages.tsx';
import Search from './pages/search/Search.tsx';
import Producer from './pages/profile/Producer.tsx';
import KitDetail from './pages/kits/KitDetail.tsx';
import Login from './pages/auth/Login.tsx';
import Register from './pages/auth/Register.tsx';
import { Provider } from 'react-redux';
import { persistor, store } from './store/store.ts';
import { PersistGate } from 'redux-persist/integration/react';
import Liked from './pages/playlists/Liked.tsx';
import MessagesDetail from './pages/messages/MessagesDetail.tsx';
import PrivateRoute from './components/PrivateRoute.tsx';
import BeatPack from './pages/beatpacks/BeatPack.tsx';



ReactDOM.createRoot(document.getElementById('root')!).render(
  <React.StrictMode>
    <Provider store={store}>
      <PersistGate loading={null} persistor={persistor}>
        <BrowserRouter>
          <Routes>
            <Route path="/" element={<App />} />
            <Route path="/profile" element={<Profile />} />
            <Route path="/profile/:slug" element={<Profile />} />
            <Route path="/producer" element={<Producer />} />
            <Route path="/messages" element={<Messages />} />
            <Route path="/search" element={<Search />} />
            
            <Route path="/kit/:id" element={<KitDetail />} />
            <Route path="/beatpack">
              <Route path=":id" element={<BeatPack />} />
            </Route>

            <Route path="/dashboard">
              <Route index element={<Studio/>} />
            </Route>

            <Route path="/tracks">

            </Route>

            <Route path="/messages">
              <Route index element={<Messages/>} />
              <Route path="chat/:slug" element={<MessagesDetail/>} />
            </Route>

            <Route path="/auth">
              <Route path="login" element={<Login/>} />
              <Route path="register" element={<Register />} />
            </Route>
            
            <Route path="/liked">
              <Route index element={<Liked />} />
            </Route>

            <Route path="/albums">
              <Route path=":id" element={<AlbumDetail />} />
            </Route>

          </Routes>
        </BrowserRouter>
      </PersistGate>
    </Provider>
  </React.StrictMode>
)
