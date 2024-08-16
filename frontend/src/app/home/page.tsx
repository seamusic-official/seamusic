'use client';
import { AlbumDetail } from '@/pages/albums';
import { Studio } from '@/pages/dashboard';
import { Home } from '@/pages/home/ui/home';
import { Messages } from '@/pages/messages';
import { MainLayout, RouterLayoutWithStaticPlayer } from '@/shared/layouts';

const Page = () => {
	return (
		<MainLayout>
			<Home />
			<RouterLayoutWithStaticPlayer auth={true} />
		</MainLayout>
		);
}

export default Page;
