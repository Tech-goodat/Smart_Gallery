import React, { useState } from 'react'
import { Link } from 'react-router-dom'
// import { FaHandHoldingHeart } from "react-icons/fa";




const Navbar = () => {
const [search,setSearch]=useState([])
const handleChange=(e)=>{
  e.preventDefault()
  setSearch(e.target.value)
}
  return (
    <div className='flex  w-full items-center justify-between h-[40px] md:h-[70px] shadow-md md:shadow-md'>
        <div className='flex items-center justify-center ml-5'>
        {/* <FaHandHoldingHeart /> */}
           <Link to="/"> <h1 className='font-bold md:text-lg text-purple-800'>Ngesh<span className='text-lg md:text-xl'>Feli</span></h1></Link>
        </div>
        <div className='hidden md:flex items-center justify-center md:gap-1 lg:gap-5 text-purple-900'>
          <Link className='hover:bg-purple-800 md:p-1 lg:p-1.5  rounded-full  hover:text-white' to="/">Home</Link>
          <Link className='hover:bg-purple-800 md:p-1 lg:p-1.5  rounded-full  hover:text-white' to="/gallery">Gallery</Link>
          <Link className='hover:bg-purple-800 md:p-1 lg:p-1.5  rounded-full  hover:text-white' to="/memories">Memories</Link>
          <Link className='hover:bg-purple-800 md:p-1 lg:p-1.5  rounded-full  hover:text-white' to="/dates">Dates</Link>
          <Link className='hover:bg-purple-800 md:p-1 lg:p-1.5  rounded-full  hover:text-white' to="/college">College</Link>
        </div>


        <div className='flex  items-center justify-center'>
            <form>
              <input 
              type='text'
              value={search}
              onChange={handleChange}
              placeholder='Search...' 
              className='border hidden w-[200px] lg:flex text-sm border-purple-800 rounded-full outline-none px-6 py-1'/>
            </form>
        </div>
        <div className='mr-6 md:mr-[110px] lg:mr-10 text-sm  md:font-bold'>
          Kiprotich
        </div>

    </div>
  )
}

export default Navbar