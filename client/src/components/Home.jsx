import React from 'react'
import { Link } from 'react-router-dom'


const Home = () => {
  return (
    <div className='flex flex-col lg:grid lg:grid-cols-2 lg:gap-4 items-center w-full h-screen'>
      <div className='h-full w-full  custom_home_bg flex items-center justify-center overflow-hidden lg:rounded-lg '></div>
      <div className='flex w-full  shadow-md h-full  lg:rounded-lg flex-col gap-1 items-center lg:justify-center'>
        <div className='flex  flex-col mt-11 lg:mt-0 items-center justify-center '>
        <h1 className='text-center text-2xl md:text-3xl font-bold'>You & I</h1>
        <h1 className='text-center text-3xl md:text-4xl font-bold'>Makes One Big</h1>
        <h1 className='text-center text-2xl md:text-3xl font-bold'>Gallery</h1>
        </div>
        <Link to="/gallery"><button className='bg-purple-800 text-white font-bold w-[110px] mt-8 p-1 md:p-2 md:text-lg rounded-full'>Gallery</button></Link>
      </div>
        
    </div>
  )
}

export default Home