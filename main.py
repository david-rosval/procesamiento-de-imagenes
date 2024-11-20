import os
from processing.manager import process_image

def main():
    input_path = "images/oso.jpg"  # Cambia el nombre según tu imagen
    output_dir = "results"
    os.makedirs(output_dir, exist_ok=True)

    # Procesar con diferentes modos
    process_image(input_path, f"{output_dir}/brightness.jpg", mode="brightness")
    process_image(input_path, f"{output_dir}/contrast.jpg", mode="contrast")

if __name__ == "__main__":
    main()
