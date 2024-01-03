import PictureLink from './components/PictureLink'
import MainLayout from './components/layouts/MainLayout'


function App() {
  return (
    <MainLayout>
        <h1 className="text-white capitalize font-semibold text-2xl mt-2">
            Your playlists
        </h1>
      <PictureLink link="albums/1" image="/assets/react.svg" title="alan walker"/>

      <h1 className="text-white capitalize font-semibold text-2xl mt-2">
            Your favorite songs
        </h1>
      <PictureLink link="albums/1" image="/assets/react.svg" title="alan walker"/>

      <h1 className="text-white capitalize font-semibold text-2xl mt-2">
            Your favorite artists
        </h1>
      <PictureLink link="albums/1" image="/assets/react.svg" title="alan walker"/>
    </MainLayout>
  )
}

export default App
