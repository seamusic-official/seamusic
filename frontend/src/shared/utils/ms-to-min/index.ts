export default function msToMin(ms: number) {
	const minutes = Math.floor(ms / 60000); // Получаем количество минут
	const seconds = Math.floor((ms % 60000) / 1000); // Получаем количество секунд

	const formattedMinutes = String(minutes).padStart(2, '0'); // Добавляем ведущий ноль, если число минут меньше 10
	const formattedSeconds = String(seconds).padStart(2, '0'); // Добавляем ведущий ноль, если число секунд меньше 10

	return `${formattedMinutes}:${formattedSeconds}`; // Возвращаем время в формате "мм:сс"
}
