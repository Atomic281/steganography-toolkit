import os

def is_image_file(filename):
    return filename.lower().endswith(('.png', '.jpg', '.jpeg'))

def save_uploaded_file(file, folder):
    path = os.path.join(folder, file.filename)
    file.save(path)
    return path
