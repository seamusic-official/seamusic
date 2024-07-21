import React from 'react';
import Link from 'next/link';
import { AddButtonPlusType } from './type';

export function AddButtonPlus({ link, onClick }: AddButtonPlusType) {
	return (
		<Link
			href={link}
			onClick={onClick}
			className="flex items-center justify-center ml-2 mr-2 p-2 w-5 h-5 bg-emerald-700 hover:bg-emerald-600 transition rounded-full">
			+
		</Link>
	);
}
