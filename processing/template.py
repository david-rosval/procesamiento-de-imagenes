from abc import ABC, abstractmethod
from PIL import Image

class ImageProcessor(ABC):
    def process(self, input_path, output_path):
        # 1. Cargar la imagen
        image = self.load_image(input_path)
        # 2. Aplicar transformación (definida en subclases)
        transformed_image = self.transform(image)
        # 3. Guardar la imagen
        self.save_image(transformed_image, output_path)

    def load_image(self, path):
        print(f"Cargando imagen desde {path}")
        return Image.open(path)

    @abstractmethod
    def transform(self, image):
        pass

    def save_image(self, image, path):
        print(f"Guardando imagen en {path}")
        image.save(path)
