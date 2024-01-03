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
import AlbumList from './pages/albums/AlbumList.tsx';
import Profile from './pages/profile/Profile.tsx';
import Studio from './pages/dashboard/Studio.tsx';
import Messages from './pages/messages/Messages.tsx';


ReactDOM.createRoot(document.getElementById('root')!).render(
  <React.StrictMode>
      <BrowserRouter>
        <Routes>
          <Route path="/" element={<App />} />
          <Route path="/profile" element={<Profile />} />
          <Route path="/messages" element={<Messages />} />

          <Route path="/dashboard">
            <Route index element={<Studio/>} />
          </Route>

          <Route path="/tracks">
          
          </Route>

          <Route path="/albums">
            <Route index element={<AlbumList/>} />
            <Route path=":id" element={<AlbumDetail />} />
          </Route>

      </Routes>
    </BrowserRouter>
</React.StrictMode>,
)
