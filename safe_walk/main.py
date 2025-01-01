from detection import Detection

if __name__ == '__main__':
    detection = Detection(
        "data/IMG_1573.MP4",
        "weight/yolo11n.pt",
        (150, ),  # (150,) - для первого видео, (300,) - для второго видео
        "Video_detect"
    )  # Создание объекта анализирования
    detection.start_video_object_detection()  # Запуск программы
