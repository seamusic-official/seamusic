import { Route, Routes } from 'react-router-dom'
import Hello from './pages/hello/Hello'
import Search from './pages/search/Search'
import Notifications from './pages/notifications/Notifications'
import Liked from './pages/playlists/Liked'
import Login from './pages/auth/Login'
import Register from './pages/auth/Register'
import Profile from './pages/profile/Profile'
import EditProfile from './pages/profile/EditProfile'
import KitDetail from './pages/kits/KitDetail'
import BeatPack from './pages/beatpacks/Beatpack'
import AddBeatpack from './pages/beatpacks/AddBeatpack'
import BeatDetail from './pages/beat-detail/BeatDetail'
import Studio from './pages/dashboard/Studio'
import Messages from './pages/messages/Messages'
import MessagesDetail from './pages/messages/MessagesDetail'
import AlbumDetail from './pages/albums/AlbumDetail'
import RouterLayoutWithStaticPlayer from './components/layouts/RouterLayoutWithStaticPlayer'
import { useAppSelector } from './hooks/redux'
import Home from './pages/home/Home'

function App() {
	const { isAuthenticated } = useAppSelector(state => state.auth)
	console.log(isAuthenticated)
	return (
		<>
			<Routes>
				<Route path='/' element={<Hello />} />

				<Route path='/auth'>
					<Route path='login' element={<Login />} />
					<Route path='register' element={<Register />} />
				</Route>

				<Route
					element={<RouterLayoutWithStaticPlayer auth={isAuthenticated} />}
				>
					<Route path='/home' element={<Home />} />
					<Route path='/search' element={<Search />} />
					<Route path='/notifications' element={<Notifications />} />
					<Route path='/liked' element={<Liked />} />
					<Route path='/profile'>
						<Route index element={<Profile />} />
						<Route path=':id' element={<Profile />} />
						<Route path='update' element={<EditProfile />} />
					</Route>

					<Route path='/artist'>
						<Route index element={<Profile />} />
						<Route path=':id' element={<Profile />} />
						<Route path='update' element={<EditProfile />} />
					</Route>

					<Route path='/producer'>
						<Route index element={<Profile />} />
						<Route path=':id' element={<Profile />} />
						<Route path='update' element={<EditProfile />} />
					</Route>

					<Route path='/soundkits'>
						<Route path=':id' element={<KitDetail />} />
						<Route path='add/' element={<BeatPack />} />
						<Route path='update' element={<BeatPack />} />
					</Route>

					<Route path='/beatpacks'>
						<Route path=':id' element={<BeatPack />} />
						<Route path='add/' element={<AddBeatpack />} />
						<Route path='update/' element={<BeatPack />} />
					</Route>

					<Route path='/beats'>
						<Route path=':id' element={<BeatDetail />} />
						<Route path='add/' element={<BeatDetail />} />
						<Route path='update/:id' element={<BeatDetail />} />
					</Route>

					<Route path='/dashboard'>
						<Route index element={<Studio />} />
					</Route>

					<Route path='/messages'>
						<Route index element={<Messages />} />
						<Route path='chat/:slug' element={<MessagesDetail />} />
					</Route>

					<Route path='/albums'>
						<Route path=':id' element={<AlbumDetail />} />
					</Route>
				</Route>
			</Routes>
		</>
	)
}

export default App
