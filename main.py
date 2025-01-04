from flask import Flask, request
import requests
import re
import os

app = Flask(__name__)

# Replace this with your Discord webhook URL
DISCORD_WEBHOOK_URL = "YOUR_DISCORD_WEBHOOK_URL"

@app.route('/', methods=['POST'])
def handle_webhook():
    data = request.json

    # Check if there's content in the message
    if 'content' in data and data['content']:
        # Replace "x.com" with "vxtwitter.com" in the content
        modified_content = re.sub(r'\bhttps?://x\.com\b', 'https://vxtwitter.com', data['content'])

        # If the content was modified, post the updated message
        if modified_content != data['content']:
            payload = {"content": modified_content}
            requests.post(DISCORD_WEBHOOK_URL, json=payload)

    return '', 204

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 10000)))
