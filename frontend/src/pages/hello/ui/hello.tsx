import React from 'react';
import Link from 'next/link';
import { DecorText } from '@/shared/ui/decor-text';

export function Hello() {
	return (
		<div className="flex justify-center items-center h-screen ">
			<div className="mb-36">
				<h1 className="font-extrabold text-5xl tracking-tighter text-center">
					For <DecorText font="extrabold">artists</DecorText>. For{' '}
					<DecorText font="extrabold">producers</DecorText>. <br />{' '}
					Self-expression for <DecorText font="extrabold">everyone</DecorText>
				</h1>
					<Link href="/auth/register">
				<p className="text-2xl my-2 text-center">
						<span className="flex items-center justify-center">
							<div>
								Let's get to <DecorText font="font-semibold">work</DecorText>
							</div>
							<svg
								xmlns="http://www.w3.org/2000/svg"
								fill="none"
								viewBox="0 0 24 24"
								strokeWidth={1.5}
								stroke="currentColor"
								className="size-6 m-2 mt-3">
								<path
									strokeLinecap="round"
									strokeLinejoin="round"
									d="M17.25 8.25 21 12m0 0-3.75 3.75M21 12H3"
								/>
							</svg>
						</span>
				</p>
					</Link>
			</div>
		</div>
	);
}
