import React from 'react';
import { DefaultButtonType } from './type';

export function DefaultButton({
	title,
	onClick,
	className,
}: DefaultButtonType) {
	return (
		<div className={className}>
			<button
				className="p-2.5 border border-zinc-800/30 hover:border-emerald-800 transition cursor-pointer font-bold rounded-lg from-zinc-200 backdrop-blur-2xl bg-zinc-800/30 from-inherit"
				onClick={onClick}>
				{title}
			</button>
		</div>
	);
}
