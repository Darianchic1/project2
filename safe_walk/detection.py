"""
Основной файл с классом
"""
import cv2
from ultralytics import YOLO

from managers import draw_object_bounding_box, draw_line
from validation import valid_detection_init, valid_set_new_fence_coord

class Detection:
    def __init__(self, path_to_video, path_to_model, fence_coord, window_name="Video") -> None:
        """
        Инициализация объекта
        :param path_to_video: str - путь до видео
        :param path_to_model: str - путь до модели
        :param fence_coord: tuple - координаты забора/ограничения
        :param window_name: str - имя окна
        """
        valid_detection_init(path_to_video, path_to_model, fence_coord, window_name)
        self.model = YOLO(path_to_model)
        self.path_to_video = path_to_video
        self.window_name = window_name
        self.fence_coord = fence_coord
        self.is_msg = True

    def set_new_fence_coord(self, new_fence_coord):
        """
        Задание новых координат забора
        """
        valid_set_new_fence_coord(new_fence_coord)
        self.fence_coord = new_fence_coord

    def _apply_yolo_object_detection(self, image, verbose: bool):
        """
        Определение животного на кадре
        """
        results = self.model.predict(image, verbose=verbose)
        classes = results[0].boxes.cls.cpu().numpy().astype(int)
        image = draw_line(image, self.fence_coord[0])
        if len(classes) == 1 and classes[0] != 0:  # Исключаем человека
            boxes = results[0].boxes.xyxy.cpu().numpy().astype(int)
            if boxes[0, 1] >= self.fence_coord[0]:  # Если объект вышел за пределы забора
                image = draw_object_bounding_box(image, boxes[0])
            else:
                image = draw_object_bounding_box(image, boxes[0], color=(0, 0, 255))
                if self.is_msg:
                    print("ВЫШЛИ")  # Вывод сообщения, что объект вышел за пределы забора
                    self.is_msg = False
        return image

    def start_video_object_detection(self, verbose: bool = False) -> None:
        """
        Захват и анализ видео в режиме реального времени
        """
        video_camera_capture = cv2.VideoCapture(self.path_to_video)

        while video_camera_capture.isOpened():  # Запускаем обработку видео потока
            ret, frame = video_camera_capture.read()
            if not ret:
                break

            frame = self._apply_yolo_object_detection(frame, verbose)
            cv2.imshow(self.window_name, frame)  # Вывод на экран изображения
            cv2.waitKey(1)

        video_camera_capture.release()
        cv2.destroyAllWindows()
