import React, { useRef } from 'react'
import Sidebar from './Sidebar'
import NavBar from './NavBar'
import Footer from './Footer'

type MyComponentProps = React.PropsWithChildren

const MainLayout = ({ children }: MyComponentProps) => {
	const dropdownRef = useRef(null)

	return (
		<div className='w-screen max-w-screen-xl overflow-y-auto '>
			<main className='tracking-tighter'>
				<Sidebar />
				<div className='text-center lg:text-left w-full md:w-4/5 md:absolute md:right-0 relative place-items-center '>
					<div className='p-4'>
						<NavBar reference={dropdownRef} />
						{children}
						<Footer />
					</div>
				</div>
			</main>
		</div>
	)
}

export default MainLayout
