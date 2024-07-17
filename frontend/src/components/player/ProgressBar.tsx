import { useAppSelector, useAppDispatch } from '../../hooks/redux'
import {
	play,
	pause,
	updateTime,
	updateDuration,
	setIsLiked,
	setDuration,
} from '../../store/reducers/playerSlice'
import { useEffect, useState } from 'react'
import default_picture from '../../assets/default-track-picture.png'
import useSound from 'use-sound'
import { Link } from 'react-router-dom'
import { memo } from 'react'
import DecorText from '../decor-text/DecorText'

const ProgressBar = memo(() => {
	const { currentSong, timeElapsed, isActive, isLiked } = useAppSelector(
		state => state.player
	)
	const [isPlaying, setIsPlaying] = useState(false)
	const src = currentSong.src
	const [play, { pause, duration, sound }] = useSound(src)
	const dispatch = useAppDispatch()
	const [currTime, setCurrTime] = useState({
		min: '00',
		sec: '00',
	})
	const [time, setTime] = useState({
		min: '00',
		sec: '00',
	})

	const [seconds, setSeconds] = useState() // current position of the audio in seconds

	useEffect(() => {
		const sec = Math.floor(duration / 1000)
		const min = Math.floor(sec / 60)
		const roundedSec = (sec % 60).toFixed(0)

		setTime({
			min,
			sec: roundedSec,
		})
	}, [sound])

	useEffect(() => {
		const interval = setInterval(() => {
			if (sound) {
				setSeconds(sound.seek([])) // setting the seconds state with the current state
				const min = Math.floor(sound.seek([]) / 60)
				const sec = Math.floor(sound.seek([]) % 60)
				setCurrTime({
					sec,
					min,
				})
			}
		}, 1000)
		return () => clearInterval(interval)
	}, [sound])

	useEffect(() => {
		pause() // ставим текущую композицию на паузу
		setIsPlaying(false) // устанавливаем флаг isPlaying в false
	}, [src]) // следим за изменениями переменной src

	const changeButton = () => {
		if (isPlaying) {
			pause() // this will pause the audio
			setIsPlaying(false)
		} else {
			play() // this will play the audio
			setIsPlaying(true)
		}
	}

	return (
		<div
			className={
				isActive
					? 'bg-opacity-5 h-auto'
					: 'border-neutral-800 border-t bg-opacity-5 h-auto'
			}
		>
			<div className='justify-between md:mb-0 lg:flex flex-row items-center'>
				<div className='mx-2 pt-2 lg:pt-0 flex justify-start items-center w-full lg:w-1/3'>
					{currentSong.picture_url ? (
						<img
							src={currentSong.picture_url}
							alt={currentSong.name}
							className='shadow-2xl m-1 rounded-md w-16 h-16 lg:w-24 lg:h-24'
						/>
					) : (
						<img
							src={default_picture}
							alt={currentSong.name}
							className='invert shadow-2xl m-1 rounded-md w-16 h-16 lg:w-24 lg:h-24'
						/>
					)}

					<div className='flex flex-col justify-center m-1 lg:m-4'>
						<h6
							id='song-name'
							className='w-56 text-white font-bold text-xl text-left truncate '
						>
							<Link to={`/beats/${currentSong.id}`}>{currentSong.name}</Link>
						</h6>
						<p id='artist-name' className='text-gray-200 font-semibold text-md'>
							<Link to={`/users/${currentSong.id}`}>@{currentSong.author}</Link>{' '}
							| <DecorText>20 likes</DecorText>
						</p>
						<p id='artist-name' className='text-gray-100 font-semibold text-md'>
							<DecorText>Add to</DecorText>
						</p>
					</div>
					<div className='text-gray-300 flex justify-center items-center'>
						<div
							onClick={() => dispatch(setLike())}
							className='cursor-pointer flex justify-center items-center'
						>
							{isLiked ? (
								<svg
									className='fill-emerald-600 flex justify-center items-center'
									role='img'
									height='24'
									width='24'
									viewBox='0 0 16 16'
									color='#fff'
								>
									<path fill='none' d='M0 0h16v16H0z'></path>
									<path d='M13.797 2.727a4.057 4.057 0 00-5.488-.253.558.558 0 01-.31.112.531.531 0 01-.311-.112 4.054 4.054 0 00-5.487.253c-.77.77-1.194 1.794-1.194 2.883s.424 2.113 1.168 2.855l4.462 5.223a1.791 1.791 0 002.726 0l4.435-5.195a4.052 4.052 0 001.195-2.883 4.057 4.057 0 00-1.196-2.883z'></path>
								</svg>
							) : (
								<svg
									className='fill-current flex justify-center items-center'
									role='img'
									height='36'
									width='36'
									viewBox='0 0 24 24'
								>
									<path d='M13.764 2.727a4.057 4.057 0 00-5.488-.253.558.558 0 01-.31.112.531.531 0 01-.311-.112 4.054 4.054 0 00-5.487.253A4.05 4.05 0 00.974 5.61c0 1.089.424 2.113 1.168 2.855l4.462 5.223a1.791 1.791 0 002.726 0l4.435-5.195A4.052 4.052 0 0014.96 5.61a4.057 4.057 0 00-1.196-2.883zm-.722 5.098L8.58 13.048c-.307.36-.921.36-1.228 0L2.864 7.797a3.072 3.072 0 01-.905-2.187c0-.826.321-1.603.905-2.187a3.091 3.091 0 012.191-.913 3.05 3.05 0 011.957.709c.041.036.408.351.954.351.531 0 .906-.31.94-.34a3.075 3.075 0 014.161.192 3.1 3.1 0 01-.025 4.403z'></path>
								</svg>
							)}
						</div>

						{/* <svg
                    className="ml-4"
                    width="24"
                    height="24"
                    xmlns="http://www.w3.org/2000/svg"
                  >
                    <g fill="currentColor" fill-rule="evenodd">
                      <path
                        d="M1 3v9h14V3H1zm0-1h14a1 1 0 0 1 1 1v10a1 1 0 0 1-1 1H1a1 1 0 0 1-1-1V3a1 1 0 0 1 1-1z"
                        fill-rule="nonzero"
                      ></path>
                      <path d="M10 8h4v3h-4z"></path>
                    </g>
                  </svg> */}
					</div>
				</div>

				<div className='lg:w-2/5 w-full flex flex-col justify-center items-center border-0'>
					<div className='text-gray-300 lg:mb-3 flex justify-between lg:pb-0 pb-1 w-3/5 lg:w-2/5 items-center'>
						<svg
							className='fill-current'
							role='img'
							height='16'
							width='16'
							viewBox='0 0 16 16'
						>
							<path d='M4.5 6.8l.7-.8C4.1 4.7 2.5 4 .9 4v1c1.3 0 2.6.6 3.5 1.6l.1.2zm7.5 4.7c-1.2 0-2.3-.5-3.2-1.3l-.6.8c1 1 2.4 1.5 3.8 1.5V14l3.5-2-3.5-2v1.5zm0-6V7l3.5-2L12 3v1.5c-1.6 0-3.2.7-4.2 2l-3.4 3.9c-.9 1-2.2 1.6-3.5 1.6v1c1.6 0 3.2-.7 4.2-2l3.4-3.9c.9-1 2.2-1.6 3.5-1.6z'></path>
						</svg>

						<svg
							className='fill-current'
							role='img'
							height='24'
							width='24'
							viewBox='0 0 16 16'
						>
							<path d='M13 2.5L5 7.119V3H3v10h2V8.881l8 4.619z'></path>
						</svg>
						{isPlaying ? (
							<button
								onClick={changeButton}
								id='play-btn'
								className='bg-white rounded-full w-8 h-8 flex justify-center items-center'
							>
								<svg
									role='img'
									height='16'
									width='16'
									viewBox='0 0 16 16'
									className='Svg-ulyrgf-0 hJgLcF'
								>
									<path fill='none' d='M0 0h16v16H0z'></path>
									<path d='M3 2h3v12H3zM10 2h3v12h-3z'></path>
								</svg>
							</button>
						) : (
							<button
								onClick={changeButton}
								id='play-btn'
								className='bg-white rounded-full w-8 h-8 flex justify-center items-center'
							>
								<svg
									xmlns='http://www.w3.org/2000/svg'
									width='16'
									height='16'
									viewBox='0 0 16 16'
									fill='none'
								>
									<path d='M4 2L12 8L4 14V2Z' fill='black' />
								</svg>
							</button>
						)}
						<svg
							className='fill-current'
							role='img'
							height='24'
							width='24'
							viewBox='0 0 16 16'
						>
							<path d='M11 3v4.119L3 2.5v11l8-4.619V13h2V3z'></path>
						</svg>
						<svg
							className='fill-current'
							role='img'
							height='16'
							width='16'
							viewBox='0 0 16 16'
						>
							<path d='M5.5 5H10v1.5l3.5-2-3.5-2V4H5.5C3 4 1 6 1 8.5c0 .6.1 1.2.4 1.8l.9-.5C2.1 9.4 2 9 2 8.5 2 6.6 3.6 5 5.5 5zm9.1 1.7l-.9.5c.2.4.3.8.3 1.3 0 1.9-1.6 3.5-3.5 3.5H6v-1.5l-3.5 2 3.5 2V13h4.5C13 13 15 11 15 8.5c0-.6-.1-1.2-.4-1.8z'></path>
						</svg>
					</div>

					<div className='pl-2 pr-2 lg:pl-0 lg:pr-0 flex flex-row justify-between items-center w-full'>
						<div
							id='time-elapsed'
							className='text-white text-lg fond-semibold text-center'
						>
							{currTime.min}:{currTime.sec}
						</div>
						<div className='flex w-full h-full rounded-full mx-4'>
							<input
								type='range'
								min='0'
								max={duration ? duration / 1000 : 1000}
								default='0'
								value={seconds}
								className='timeline'
								style={{ flexGrow: 1 }} // Установка максимальной ширины для input
								onChange={e => {
									sound.seek([e.target.value])
								}}
							/>
						</div>
						<div
							id='duration'
							className='text-white text-lg fond-semibold text-center'
						>
							{time.min}:{time.sec}
						</div>
					</div>
				</div>

				<div className='invisible lg:visible flex flex-row justify-end items-center w-1/3 mr-4'>
					<div className='flex justify-center w-2/5 items-center text-gray-300'>
						<svg
							className='fill-current m-4'
							height='20'
							width='20'
							viewBox='0 0 48 48'
							xmlns='http://www.w3.org/2000/svg'
						>
							<path d='M0 0h48v48H0z' fill='none' />
							<path d='M30 12H6v4h24v-4zm0 8H6v4h24v-4zM6 32h16v-4H6v4zm28-20v16.37c-.63-.23-1.29-.37-2-.37-3.31 0-6 2.69-6 6s2.69 6 6 6 6-2.69 6-6V16h6v-4H34z' />
						</svg>
						<svg
							className='fill-current mr-2'
							role='img'
							height='16'
							width='16'
							viewBox='0 0 16 16'
						>
							<path d='M12.945 1.379l-.652.763c1.577 1.462 2.57 3.544 2.57 5.858s-.994 4.396-2.57 5.858l.651.763a8.966 8.966 0 00.001-13.242zm-2.272 2.66l-.651.763a4.484 4.484 0 01-.001 6.397l.651.763c1.04-1 1.691-2.404 1.691-3.961s-.65-2.962-1.69-3.962zM0 5v6h2.804L8 14V2L2.804 5H0zm7-1.268v8.536L3.072 10H1V6h2.072L7 3.732z'></path>
						</svg>
					</div>
				</div>
			</div>
		</div>
	)
})

export default ProgressBar
