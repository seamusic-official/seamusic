import { useDispatch, useSelector, useStore } from 'react-redux';
import { RootState, AppDispatch, AppStore } from '@/store/store';

export const useAppDispatch = useDispatch.withTypes<AppDispatch>(),
	useAppSelector = useSelector.withTypes<RootState>(),
	useAppStore = useStore.withTypes<AppStore>();
