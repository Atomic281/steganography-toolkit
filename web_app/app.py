import os
import sys
from flask import Flask, render_template, request, send_file

# Fix the import path for image_stego
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from image_stego import encode_image, decode_image

# ✅ Initialize Flask app
app = Flask(__name__)

# Create a secure absolute path for uploads
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
UPLOAD_FOLDER = os.path.join(BASE_DIR, 'uploads')
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/encode', methods=['POST'])
def encode():
    try:
        image = request.files['image']
        message = request.form['message']

        if not image:
            return "No image uploaded", 400

        image_path = os.path.join(UPLOAD_FOLDER, image.filename)
        save_path = os.path.join(UPLOAD_FOLDER, 'stego.png')

        image.save(image_path)

        # Encode message into the image
        encode_image(image_path, message, save_path)

        if not os.path.exists(save_path):
            return "Failed to create stego image", 500

        return send_file(save_path, as_attachment=True)

    except Exception as e:
        return f"Error during encoding: {str(e)}", 500

@app.route('/decode', methods=['POST'])
def decode():
    try:
        image = request.files['image']
        if not image:
            return "No image uploaded", 400

        image_path = os.path.join(UPLOAD_FOLDER, image.filename)
        image.save(image_path)

        message = decode_image(image_path)
        return f"Decoded Message: {message}"

    except Exception as e:
        return f"Error during decoding: {str(e)}", 500

if __name__ == '__main__':
    app.run(debug=True)
