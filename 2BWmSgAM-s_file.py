from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def index():
    # HTML template with Spotify player and blur effect
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Music Player</title>
        <style>
            /* Add your custom CSS styles here */
            body {
                margin: 0;
                padding: 0;
                background: url('your-background-image.jpg') no-repeat center center fixed;
                background-size: cover;
                filter: blur(5px); /* Adjust the blur amount as needed */
            }
            #spotify-player {
                border-radius: 12px;
                width: 600px;
                height: 152px;
                position: absolute;
                top: 50%;
                left: 50%;
                transform: translate(-50%, -50%);
            }
        </style>
    </head>
    <body>
        <iframe id="spotify-player" src="https://open.spotify.com/embed/album/5KbSHcs8iGcDVflTiRx4FA?utm_source=generator" frameborder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy"></iframe>
    </body>
    </html>
    """
    return render_template_string(html_content)

if __name__ == '__main__':
    app.run(debug=True)
