import Link from 'next/link';
import { DecorText } from '@/shared/ui/decor-text';

export function Fasttube() {
	return (
		<div className="flex justify-center items-center h-screen ">
			<div className="my-6 lg:mb-24">
				<h1 className="font-extrabold lg:text-5xl text-4xl tracking-tighter leading-6 text-center">
					For{' '}
					<DecorText font="extrabold">producers</DecorText>. <br />{' '}
					Self-expression for <DecorText font="extrabold">everyone</DecorText>
				</h1>
					<Link href="/auth/register">
				<p className="lg:text-xl text-lg my-3 tracking-tighter text-center leading-6">
								С помощью <DecorText font="font-semibold">этого телеграм бота</DecorText> вы можете создать видео для YouTube & YTShorts/TikTok/Instagram <br /> скинув изображения и mp3 аудио. И при желании, вы можете подключить ваш YT канал и выклыдвать туда видео напрямую и тг бота.
				</p>
					</Link>
			</div>
		</div>
	);
}
