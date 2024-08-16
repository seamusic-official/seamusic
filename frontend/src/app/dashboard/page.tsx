'use client';
import { AlbumDetail } from '@/pages/albums';
import { Studio } from '@/pages/dashboard';
import { Messages } from '@/pages/messages';
import { MainLayout } from '@/shared/layouts';

function Page() {
	return <MainLayout><Studio /></MainLayout>;
}

export default Page;
