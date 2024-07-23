import { MainLayout } from '@/shared/layouts';
import des from '@/shared/assets/everydesigner.png';
import { MessagePreview } from '@/shared/ui/messages';

export function Messages() {
	const imgUrl = des.toString();
	return (
		<MainLayout>
			<h2
				className="mt-2 mb-1 text-white text-3xl capitalize font-extrabold tracking-tighter"
				id="playlist-title">
				Messages
			</h2>
			<MessagePreview
				href={'/messages/chat/visagangbeats'}
				message="Yo bro, lmk me in ig"
				username="whyspacy?"
				image_url={imgUrl}
			/>
			<MessagePreview
				href={'/messages/chat/visagangbeats'}
				message="send me loops please"
				username="whiteprince"
				image_url={imgUrl}
			/>
			<MessagePreview
				href={'/messages/chat/visagangbeats'}
				message="hi"
				username="prod.flowlove"
				image_url={imgUrl}
			/>
		</MainLayout>
	);
}
