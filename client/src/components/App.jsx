import React from 'react'
import Home from './Home'
import {BrowserRouter as Router, Routes, Route} from 'react-router-dom'
import Gallery from './Gallery'
import Navbar from './Navbar'
import Memories from './Memories'
import Dates from './Dates'
import College from './College'


const App = () => {
  return (
    <Router>
      <div className='flex  flex-col min-h-screen text-purple-800 '>
        <div className='fixed w-full  bg-white'>
       
        <Navbar />
        </div>
        
      <div className='flex flex-grow mt-[40px] lg:mt-[80px] overflow-y-auto'>
      <Routes >
        <Route path='/' element={<Home />} />
        <Route path='/gallery' element={<Gallery />} />
        <Route path='/memories' element={<Memories />} />
        <Route path='/dates' element={<Dates/>} />
        <Route path='/college' element={<College />} />
      </Routes>
      </div>
      </div>
    </Router>
  )
}
export default App