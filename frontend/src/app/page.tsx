'use client';

import Image from 'next/image';
import Link from 'next/link';
import { useAppSelector } from '@/shared/hooks/redux';
import { Hello } from '@/pages/hello';
import { Login, Register } from '@/pages/auth';
import { RouterLayoutWithStaticPlayer } from '@/shared/layouts';
import { Search } from '@/pages/search';

export default function Home() {
	const { isAuthenticated } = useAppSelector((state) => state.auth);
	// console.log(isAuthenticated);
	return (
		<>
			<Hello />
		</>
	);
}
