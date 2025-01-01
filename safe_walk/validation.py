"""
Файл для валидорования аргументов
"""
from exceptions import BadPath, BadWindowName, BadFenceCoord
import os


def valid_detection_init(path_to_video: str, path_to_model: str, fence_coord: tuple, window_name: str):
    """
    Валидация аргументов метода __init__
    """
    if not isinstance(path_to_video, str):
        raise BadPath(f"type({path_to_video}) is not str", 400)
    if not isinstance(path_to_model, str):
        raise BadPath(f"type({path_to_model}) is not str", 400)
    if not isinstance(window_name, str):
        raise BadWindowName(f"type({window_name}) is not str", 400)
    if not isinstance(fence_coord, tuple):
        raise BadFenceCoord(f"type({fence_coord}) is not tuple", 400)
    if len(fence_coord) != 1:
        raise BadFenceCoord(f"Shape {fence_coord}) != (1, )", 400)
    if not path_to_video.lower().endswith(".mp4"):
        raise BadPath(f"{path_to_video} is not video file (*.mp4)", 400)
    if not path_to_model.lower().endswith(".pt"):
        raise BadPath(f"{path_to_model} is not model file (*.pt)", 400)
    if not (os.path.exists(path_to_video) and os.path.isfile(path_to_video)):
        raise BadPath(f"Not find {path_to_video}", 400)
    if not (os.path.exists(path_to_model) and os.path.isfile(path_to_model)):
        raise BadPath(f"Not find {path_to_model}", 400)


def valid_set_new_fence_coord(fence_coord: tuple):
    """
    Валидация аргументов метода set_new_fence_coord
    """
    if not isinstance(fence_coord, tuple):
        raise BadFenceCoord(f"type({fence_coord}) is not tuple", 400)
    if len(fence_coord) != 1:
        raise BadFenceCoord(f"Shape {fence_coord}) != (1, )", 400)
