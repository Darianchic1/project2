"""
Файл для хранения вспомогательных функций
"""
import cv2

def draw_object_bounding_box(image_to_process, bbox, color=(0, 255, 0)):
    """
    Отрисовка квадрата по координатам
    :param image_to_process: изображение
    :param bbox: bbox квадрата от yolo
    :param color: цвет в формате (b, g, r)
    :return: изображение с отрисованной границей
    """
    x1, y1, x2, y2 = bbox
    width = 2
    final_image = cv2.rectangle(image_to_process, (x1, y1), (x2, y2), color, width)
    return final_image


def draw_line(frame, y_coord, color=(0, 0, 255)):
    """
    Отрисовка линии забора/границы
    :param frame: изображение
    :param y_coord: координата забора/границы по y
    :param color: цвет в формате (b, g, r)
    :return: изображение с отрисованной границей
    """
    height, width, _ = frame.shape
    start_point = (0, y_coord)  # Начальная точка (x1, y1)
    end_point = (width, y_coord)  # Конечная точка (x2, y2)
    thickness = 2
    frame_with_line = cv2.line(frame, start_point, end_point, color, thickness)
    return frame_with_line

