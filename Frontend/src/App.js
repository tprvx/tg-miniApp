import React, { useEffect } from 'react'
import './App.css'
import { useTelegram } from '../src/Hooks/useTelegram'
import Header from '../src/components/Header/header'
import { Route, Routes } from 'react-router-dom'
import ProductList from './components/ProductList/ProductList'
import Form from './components/Form/Form'

function App() {
	const { onToggleButton, tg } = useTelegram()

	useEffect(() => {
		tg.ready()
	}, [])

	return (
		<div className='App'>
			{/* <Header /> */}
			<Routes>
				<Route index element={<Form />} />
				<Route path={'form'} element={<Form />} />
				<Route path={'products'} element={<ProductList />} />
			</Routes>
		</div>
	)
}

export default App
