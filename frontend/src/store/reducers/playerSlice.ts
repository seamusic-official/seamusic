import { createSlice } from '@reduxjs/toolkit';

const initialState = {
  isActive: false,
  currentSong: {
    id: null,
    picture: null,
    author: null,
    name: null,
    type: null,
    album: null,
    date: null,
    duration: null,
    src: null
  },
  isLiked: false,
  isPlaying: false,
  timeElapsed: 0,
  type: null
};

const playerSlice = createSlice({
  name: 'player',
  initialState,
  reducers: {
    setSong(state, action) {
      state.isActive = action.payload.isActive; // Update isActive separately
      state.currentSong = action.payload.currentSong; // Update currentSong separately
    },
    setLike(state) {
      state.isLiked = !state.isLiked;
    },
    play(state) {
      state.isPlaying = true;
    },
    pause(state) {
      state.isPlaying = false;
    },
    updateTime(state, action) {
      state.timeElapsed = action.payload;
    },
    updateDuration(state, action) {
      state.currentSong.duration = action.payload;
    },

  },
});

export const { setSong, setLike, play, pause, updateTime, updateDuration } = playerSlice.actions;
export default playerSlice.reducer;
