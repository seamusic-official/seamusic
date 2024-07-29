import React from 'react';
import { DefaultLinkType } from './type';
import Link from 'next/link';

export function DefaultLink({ children, link }: DefaultLinkType) {
	return (
		<Link href={link}>
			<span className="hover:text-emerald-600">{children}</span>
		</Link>
	);
}
