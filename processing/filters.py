from PIL import ImageEnhance

def brightness_filter(image, factor=1.5):
    print("Aplicando filtro de brillo...")
    enhancer = ImageEnhance.Brightness(image)
    return enhancer.enhance(factor)

def contrast_filter(image, factor=1.5):
    print("Aplicando filtro de contraste...")
    enhancer = ImageEnhance.Contrast(image)
    return enhancer.enhance(factor)
