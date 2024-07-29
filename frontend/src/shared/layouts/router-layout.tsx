import { ProgressBar } from '@/entities/progress-bar';
import { MainMenu } from '@/entities/menu';

type RouterLayoutWithStaticPlayerProps = {
	auth: boolean;
};

export function RouterLayoutWithStaticPlayer({
	auth,
}: RouterLayoutWithStaticPlayerProps) {
	return auth ? (
		<>
			{/* <Outlet /> */}
			<div className="fixed dark:border-neutral-800 transition border-t bg-zinc-800/30 dark:from-inherit backdrop-blur-md left-0 bottom-0 right-0 h-auto">
				<ProgressBar />
				<MainMenu />
			</div>
		</>
	) : (
		//<Navigate to={'/auth/login'} /> // раскоментить когда будет функционал с логином (isAuthenticated не меняется даже если ставить вручную в стейте)
		<>
			{/* <Outlet /> */}
			<div className="fixed dark:border-neutral-800 transition border-t bg-zinc-800/30 dark:from-inherit backdrop-blur-md left-0 bottom-0 right-0 h-auto">
				<ProgressBar />
				<MainMenu />
			</div>
		</>
	);
}
