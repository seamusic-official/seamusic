'use client';

import { Hello } from '@/pages/hello';
import { HelloLayout, RouterLayoutWithStaticPlayer } from '@/shared/layouts';

const Page = () => {
	return <HelloLayout><Hello/></HelloLayout>;
};

export default Page;
