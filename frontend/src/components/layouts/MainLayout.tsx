import React from 'react'
import ProgressBar from '../ProgressBar'
import Sidebar from '../Sidebar'
import NavBar from '../NavBar';


type MyComponentProps = React.PropsWithChildren;

const MainLayout = ({children}: MyComponentProps) => {
  return (
    <div>
        <div>
            <Sidebar/>
            <ProgressBar/>


            <div className="text-center lg:text-left  ">
                <div className="p-6 w-full md:w-4/5 md:absolute md:right-0 ">
                  <NavBar/>
                    {children}
                </div>
            </div>
        </div>
    </div>
  )
}

export default MainLayout
