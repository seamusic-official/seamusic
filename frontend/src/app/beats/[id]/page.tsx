'use client';
import { AlbumDetail } from '@/pages/albums';
import { BeatDetail } from '@/pages/beat-detail';
import { Studio } from '@/pages/dashboard';
import { Messages } from '@/pages/messages';
import { MainLayout } from '@/shared/layouts';

function Page() {
	return <MainLayout><BeatDetail /></MainLayout>;
}

export default Page;
