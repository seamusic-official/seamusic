import MainLayout from '../../components/layouts/MainLayout'
import des from '../../assets/everydesigner.png'
import MessagePreview from '../../components/messages/MessagePreview'

export default function Messages() {
  return (
    <MainLayout>
      <h2 className="mt-2 mb-1 text-white text-3xl capitalize font-extrabold tracking-tighter" id="playlist-title">
      Messages
      </h2>
      <MessagePreview href={"/messages/chat/visagangbeats"} message="Yo bro, lmk me in ig" username="whyspacy?" image_url={des} />
      <MessagePreview href={"/messages/chat/visagangbeats"} message="send me loops please" username="whiteprince" image_url={des} />
      <MessagePreview href={"/messages/chat/visagangbeats"} message="hi" username="prod.flowlove" image_url={des} />
    </MainLayout>
  )
}
