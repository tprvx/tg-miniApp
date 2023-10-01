import React from 'react'
import { useTelegram } from '../../Hooks/useTelegram'
import './header.css'

const Header = () => {
	const { user, onClose } = useTelegram()

	return (
		<div className={'header'}>
			<span className={'username'}>{user?.username}</span>
		</div>
	)
}

export default Header
