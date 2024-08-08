'use client';
import { AlbumDetail } from '@/pages/album';
import { Messages, MessagesDetail } from '@/pages/messages';
import { MainLayout } from '@/shared/layouts';

function Page() {
	return <MainLayout><MessagesDetail /></MainLayout>;
}

export default Page;