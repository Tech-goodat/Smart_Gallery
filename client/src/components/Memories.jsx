import React, { useEffect, useState } from 'react'



const Memories = () => {
  const [memories, setMemories]=useState([])
  useEffect (()=>{
    fetch ("http://127.0.0.1:5555/memories")
    .then(response=>response.json())
    .then(data=>{
      console.log(data);
      setMemories(data)
    })
    .catch(error=>{
      console.error("error fetching", error)
    })
  },[])
  return (
    <div>{memories.map(memory=>(
      <div key={memory.id}>
      <h1>{memory.id}</h1>
      <h1>{memory.name}</h1>
      </div>
    ))}</div>
  )
}

export default Memories