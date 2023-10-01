import React, { useEffect } from 'react'
import './App.css'
import { useTelegram } from '../src/Hooks/useTelegram'
import Header from '../src/components/Header/header'

function App() {
	const { onToggleButton, tg } = useTelegram()

	useEffect(() => {
		tg.ready()
	}, [])

	return (
		<div className='App'>
			<Header></Header>
			<button onClick={onToggleButton}>toggle</button>
		</div>
	)
}

export default App
