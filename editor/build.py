from generator.image.build import build_image_generator
from generator.video.build import build_video_generator
from generator.tts.build import build_tts_generator
from generator.text.build import build_text_generator
from generator.music.build import build_bgm_generator
from editor.chat_editor import Text2VideoEditor
from comm.mylog import logger

from generator.text.models.news_generator import top_news

def build_editor(cfg):
    text_gen_type = cfg.video_editor.text_gen.type
    logger.info('editor text_gen_type: {}'.format(text_gen_type))
    if text_gen_type == 'newsapi':
        top_headlines = top_news(cfg.video_editor.text_gen.category)
        text_generator = build_text_generator(cfg, top_headlines)
        vision_generator = build_image_generator(cfg, top_headlines)
        audio_generator = build_tts_generator(cfg)
        bgm_generator = build_bgm_generator(cfg)
    
        editor = Text2VideoEditor(cfg,text_generator, vision_generator, audio_generator,bgm_generator)
        return editor

    visual_gen_type = cfg.video_editor.visual_gen.type
    logger.info('visual_gen_type: {}'.format(visual_gen_type))
    # image_by_diffusion  video_by_retrieval image_by_retrieval_then_diffusion video_by_diffusion
    if visual_gen_type in ["image_by_retrieval","image_by_diffusion","image_by_retrieval_then_diffusion"]:
        vision_generator = build_image_generator(cfg)
    else:
        vision_generator = build_video_generator(cfg)
    
    text_generator = build_text_generator(cfg)
    audio_generator = build_tts_generator(cfg)
    bgm_generator = build_bgm_generator(cfg)
    
    editor = Text2VideoEditor(cfg,text_generator, vision_generator, audio_generator,bgm_generator)
    return editor