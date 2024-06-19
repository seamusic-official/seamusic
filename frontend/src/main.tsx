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
import BeatPack from './pages/beatpacks/Beatpack.tsx';
import Artist from './pages/profile/Artist.tsx';
import EditProfile from './pages/profile/EditProfile.tsx';
import Notifications from './pages/notifications/Notifications.tsx';
import Hello from './pages/hello/Hello.tsx';
import BeatDetail from './pages/beat-detail/BeatDetail.tsx';
import AddBeatpack from './pages/beatpacks/AddBeatpack.tsx';



ReactDOM.createRoot(document.getElementById('root')!).render(
  <React.StrictMode>
    <Provider store={store}>
      <PersistGate loading={null} persistor={persistor}>
        <BrowserRouter>
          <Routes>
            <Route path="/" element={<Hello />} />
            <Route path="/home" element={<App />} />
            <Route path="/search" element={<Search />} />
            <Route path="/notifications" element={<Notifications />} />
            <Route path="/liked" element={<Liked />} />

            <Route path="/auth">
              <Route path="login" element={<Login/>} />
              <Route path="register" element={<Register />} />
            </Route>

            <Route path="/profile">
              <Route index element={<Profile />} />
              <Route path=":id" element={<Profile />} />
              <Route path="update" element={<EditProfile />} />
            </Route>

            <Route path="/artist">
              <Route index element={<Profile />} />
              <Route path=":id" element={<Profile />} />
              <Route path="update" element={<EditProfile />} />
            </Route>

            <Route path="/producer">
              <Route index element={<Profile />} />
              <Route path=":id" element={<Profile />} />
              <Route path="update" element={<EditProfile />} />
            </Route>
            
            <Route path="/kits">
              <Route path=":id" element={<KitDetail />} />
              <Route path="add/" element={<BeatPack />} />
              <Route path="update" element={<BeatPack />} />
            </Route>

            <Route path="/beatpacks">
              <Route path=":id" element={<BeatPack />} />
              <Route path="add/" element={<AddBeatpack />} />
              <Route path="update/" element={<BeatPack />} />
            </Route>

            <Route path="/beats">
              <Route path=":id" element={<BeatDetail />} />
              <Route path="add/" element={<BeatDetail />} />
              <Route path="update/:id" element={<BeatDetail />} />
            </Route>
            
            <Route path="/dashboard">
              <Route index element={<Studio/>} />
            </Route>

            <Route path="/messages">
              <Route index element={<Messages/>} />
              <Route path="chat/:slug" element={<MessagesDetail/>} />
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
