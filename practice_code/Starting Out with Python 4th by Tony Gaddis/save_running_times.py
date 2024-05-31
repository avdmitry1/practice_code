# Программа сохраняет последовательность, стостоящую из
# длительностей видео клипов в файл video_times.txt
def main():
    # Получить количество видеоклипов в проекте
    num_videos = int(input('Сколько видеоклипов в проекте? '))
    # Открыть файл для записи видеоклипов
    video_file = open('video_times.txt', 'w')
    # Получить длительность видеоклипа и записать их в файл
    print('Введите длительность каждого видео клипа')
    for i in range(1, num_videos + 1):
        run_time = float(input(f'Видеоклип № {i}: '))
        video_file.write(f'{run_time}\n')
    # Закрыть файл
    video_file.close()


if __name__ == '__main__':
    main()
