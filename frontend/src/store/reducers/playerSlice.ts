import { createSlice } from '@reduxjs/toolkit';


const initialState = {
  isActive: false,
  currentSong: {
    id: null,
    picture_url: null,
    author: null,
    name: null,
    type: null,
    album: null,
    date: null,
    duration: {
      min: "00",
      sec: "00"
    },
    seconds: 0,
    src: null,
    sound: null
  },
  isPlaying: false,
  isLiked: false,
  timeElapsed: {
    min: 0,
    sec: 0,
  },
  type: null,
  sound: null,
};


const playerSlice = createSlice({
  name: 'player',
  initialState,
  reducers: {
    setSong(state, action) {
      state.currentSong = action.payload.currentSong;
      state.isActive = action.payload.isActive;
    },
    updateDuration(state, action) {
      state.currentSong.duration = action.payload;
    },
    updateSeconds(state, action) {
      state.currentSong.seconds = action.payload;
    },
    updateTime(state, action) {
      state.timeElapsed = action.payload;
    },
    setSound(state, action) {
      state.sound = action.payload;
    },
    playSong(state) {
      state.isPlaying = true;
    },
    pauseSong(state) {
      state.isPlaying = false;
    },
    setIsLiked(state) {
      state.isLiked = true;
    },
    setDuration(state, action) {
      state.currentSong.duration = action.payload;
    },
}});

export const { setSong, setSound, playSong, pauseSong, updateDuration, updateSeconds, setIsLiked, updateTime, setDuration } = playerSlice.actions;
export default playerSlice.reducer;
