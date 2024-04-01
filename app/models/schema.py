from enum import Enum
from typing import Any, Optional

from pydantic import BaseModel
import warnings

# 忽略 Pydantic 的特定警告
warnings.filterwarnings("ignore", category=UserWarning, message="Field name.*shadows an attribute in parent.*")


class VideoConcatMode(str, Enum):
    random = "random"
    sequential = "sequential"


class VideoAspect(str, Enum):
    landscape = "16:9"
    portrait = "9:16"
    square = "1:1"

    def to_resolution(self):
        if self == VideoAspect.landscape.value:
            return 1920, 1080
        elif self == VideoAspect.portrait.value:
            return 1080, 1920
        elif self == VideoAspect.square.value:
            return 1080, 1080
        return 1080, 1920


class MaterialInfo:
    provider: str = "pexels"
    url: str = ""
    duration: int = 0


# VoiceNames = [
#     # zh-CN
#     "female-zh-CN-XiaoxiaoNeural",
#     "female-zh-CN-XiaoyiNeural",
#     "female-zh-CN-liaoning-XiaobeiNeural",
#     "female-zh-CN-shaanxi-XiaoniNeural",
#
#     "male-zh-CN-YunjianNeural",
#     "male-zh-CN-YunxiNeural",
#     "male-zh-CN-YunxiaNeural",
#     "male-zh-CN-YunyangNeural",
#
#     # "female-zh-HK-HiuGaaiNeural",
#     # "female-zh-HK-HiuMaanNeural",
#     # "male-zh-HK-WanLungNeural",
#     #
#     # "female-zh-TW-HsiaoChenNeural",
#     # "female-zh-TW-HsiaoYuNeural",
#     # "male-zh-TW-YunJheNeural",
#
#     # en-US
#
#     "female-en-US-AnaNeural",
#     "female-en-US-AriaNeural",
#     "female-en-US-AvaNeural",
#     "female-en-US-EmmaNeural",
#     "female-en-US-JennyNeural",
#     "female-en-US-MichelleNeural",
#
#     "male-en-US-AndrewNeural",
#     "male-en-US-BrianNeural",
#     "male-en-US-ChristopherNeural",
#     "male-en-US-EricNeural",
#     "male-en-US-GuyNeural",
#     "male-en-US-RogerNeural",
#     "male-en-US-SteffanNeural",
# ]


class VideoParams:
    """
    {
      "video_subject": "",
      "video_aspect": "横屏 16:9（西瓜视频）",
      "voice_name": "女生-晓晓",
      "bgm_name": "random",
      "font_name": "STHeitiMedium 黑体-中",
      "text_color": "#FFFFFF",
      "font_size": 60,
      "stroke_color": "#000000",
      "stroke_width": 1.5
    }
    """
    video_subject: str
    video_script: str = ""  # 用于生成视频的脚本
    video_terms: Optional[str | list] = None  # 用于生成视频的关键词
    video_aspect: Optional[VideoAspect] = VideoAspect.portrait.value
    video_concat_mode: Optional[VideoConcatMode] = VideoConcatMode.random.value
    video_clip_duration: Optional[int] = 5
    video_count: Optional[int] = 1

    video_language: Optional[str] = ""  # auto detect

    voice_name: Optional[str] = ""
    bgm_type: Optional[str] = "random"
    bgm_file: Optional[str] = ""
    bgm_volume: Optional[float] = 0.2

    subtitle_enabled: Optional[bool] = True
    subtitle_position: Optional[str] = "bottom"  # top, bottom, center
    font_name: Optional[str] = "STHeitiMedium.ttc"
    text_fore_color: Optional[str] = "#FFFFFF"
    text_background_color: Optional[str] = "transparent"

    font_size: int = 60
    stroke_color: Optional[str] = "#000000"
    stroke_width: float = 1.5
    n_threads: Optional[int] = 2
    paragraph_number: Optional[int] = 1


class BaseResponse(BaseModel):
    status: int = 200
    message: Optional[str] = 'success'
    data: Any = None


class TaskVideoRequest(VideoParams, BaseModel):
    pass


class TaskQueryRequest(BaseModel):
    pass


######################################################################################################
######################################################################################################
######################################################################################################
######################################################################################################
class TaskResponse(BaseResponse):
    class TaskResponseData(BaseModel):
        task_id: str
        task_type: str = ""

    data: TaskResponseData


class TaskQueryResponse(BaseResponse):
    pass
