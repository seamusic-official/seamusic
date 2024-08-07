'use client';
import { AlbumDetail } from '@/pages/album';
import { Studio } from '@/pages/dashboard';
import { Messages } from '@/pages/messages';
import { Search } from '@/pages/search';
import { MainLayout } from '@/shared/layouts';

function Page() {
	return <MainLayout><Search /></MainLayout>;
}

export default Page;
