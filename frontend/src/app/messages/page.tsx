'use client';
import { AlbumDetail } from '@/pages/album';
import { Messages } from '@/pages/messages';
import { MainLayout, RouterLayoutWithStaticPlayer } from '@/shared/layouts';

const Page = () => {
	return (
		<MainLayout>
				<Messages />
				<RouterLayoutWithStaticPlayer auth={true} />
		</MainLayout>
		)
}

export default Page;
