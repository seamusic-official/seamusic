import { Navigate, Outlet } from 'react-router-dom'
import ProgressBar from '../player/ProgressBar'
import Menu from './Menu'

interface RouterLayoutWithStaticPlayerProps {
	auth: boolean
}

const RouterLayoutWithStaticPlayer = ({
	auth,
}: RouterLayoutWithStaticPlayerProps) => {
	return auth ? (
		<>
			<Outlet />
			<div className='fixed dark:border-neutral-800 transition border-t bg-zinc-800/30 dark:from-inherit backdrop-blur-md left-0 bottom-0 right-0 h-auto'>
				<ProgressBar />
				<Menu />
			</div>
		</>
	) : (
		//<Navigate to={'/auth/login'} /> // раскоментить когда будет функционал с логином (isAuthenticated не меняется даже если ставить вручную в стейте)
		<>
			<Outlet />
			<div className='fixed dark:border-neutral-800 transition border-t bg-zinc-800/30 dark:from-inherit backdrop-blur-md left-0 bottom-0 right-0 h-auto'>
				<ProgressBar />
				<Menu />
			</div>
		</>
	)
}

export default RouterLayoutWithStaticPlayer
