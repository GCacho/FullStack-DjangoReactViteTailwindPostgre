import { useEffect } from 'react'

function App() {
  useEffect(()=> {
    console.log(import.meta.env.VITE_API_URL)
  }, [])

  return (
    <>
      <h1>Hola Mundoooo</h1>
    </>
  )
}

export default App
