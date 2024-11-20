from .template import ImageProcessor
from .filters import brightness_filter, contrast_filter

class BrightnessProcessor(ImageProcessor):
    def transform(self, image):
        return brightness_filter(image, factor=1.2)

class ContrastProcessor(ImageProcessor):
    def transform(self, image):
        return contrast_filter(image, factor=1.5)

def process_image(input_path, output_path, mode="brightness"):
    if mode == "brightness":
        processor = BrightnessProcessor()
    elif mode == "contrast":
        processor = ContrastProcessor()
    else:
        raise ValueError(f"Modo desconocido: {mode}")
    
    processor.process(input_path, output_path)
