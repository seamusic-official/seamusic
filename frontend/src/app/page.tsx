'use client';

import Image from 'next/image';
import Link from 'next/link';
import { useAppSelector } from '@/shared/hooks/redux';
import { Hello } from '@/pages/hello';
import { Login, Register } from '@/pages/auth';
import { RouterLayoutWithStaticPlayer } from '@/shared/layouts';
import { Search } from '@/pages/search';
import {
	AddButtonPlus,
	DefaultButton,
	SubmitButton,
} from '@/shared/ui/buttons';

const Page = () => {
	const isAuthenticated = useAppSelector((state) => state.auth);
	console.log(isAuthenticated.isAuthenticated);
	const onClick = () => console.log('click');
	return (
		<>
			неддщ
			<DefaultButton title="123" />
			<DefaultButton title="123" />
			<DefaultButton title="123" />
			<DefaultButton title="123" />
			<AddButtonPlus link="/a" onClick={onClick} />
			<SubmitButton />
			{/* <Hello /> */}
		</>
	);
};

export default Page;
