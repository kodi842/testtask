from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

# === НАСТРОЙКИ ===
DEEPAI_API_KEY = os.getenv("DEEPAI_API_KEY")
HF_API_URL = 'https://stabilityai-stable-diffusion.hf.space/run/predict'

@app.route('/generate', methods=['POST'])
def generate_image():
    data = request.json
    prompt = data.get('prompt')
    model = data.get('model')

    if not prompt or not model:
        return jsonify({'error': 'No prompt or model provided'}), 400

    try:
        if model == 'deepai':
            response = requests.post(
                "https://api.deepai.org/api/text2img",
                data={'text': prompt},
                headers={'api-key': DEEPAI_API_KEY},
                timeout=20
            )
            image_url = response.json().get('output_url')

        elif model == 'sd':
            response = requests.post(
                HF_API_URL,
                json={"data": [prompt, 30]},
                timeout=60
            )
            image_url = response.json().get("data", [""])[0]

        else:
            return jsonify({'error': 'Unknown model'}), 400

        return jsonify({'image_url': image_url})

    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
