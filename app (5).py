import gradio as gr
import os
import random

# Generate fake audio files (simulated)
def generate_fake_playlist(user_prompt, time_limit):
    num_snippets = time_limit // 5  # Assuming 5 minutes per snippet
    playlist = []
    for idx in range(num_snippets):
        # Simulating a dummy MP3 file path
        fake_audio_file = f"dummy_snippet_{idx+1}.mp3"
        # Create empty file (or use a silent audio clip)
        with open(fake_audio_file, 'wb') as f:
            f.write(b'\0')  # Just write a dummy byte
        playlist.append((f"Snippet {idx+1}", fake_audio_file))
    return playlist

# UI
with gr.Blocks() as demo:
    gr.Markdown("# 🎧 Spotify for Learning\nTurn curiosity into a learning playlist in one click.")

    with gr.Row():
        user_prompt = gr.Textbox(label="What do you want to learn?", placeholder="e.g. AI avatars, Moon landing...")
        time_input = gr.Slider(minimum=5, maximum=60, step=5, value=15, label="How many minutes do you have?")

    generate_button = gr.Button("🎬 Generate Learning Playlist")
    output_playlist = gr.Audio(label="Your Learning Playlist", interactive=False, type="filepath", show_label=False, visible=True)
    playlist_gallery = gr.Gallery(label="Playlist Gallery", scale=1)  # Use scale instead of style.grid

    def generate_and_display(prompt, time):
        playlist = generate_fake_playlist(prompt, time)
        # Create audio components for each snippet in the playlist
        return [gr.Audio(value=audio, label=label) for label, audio in playlist]

    generate_button.click(
        fn=generate_and_display,
        inputs=[user_prompt, time_input],
        outputs=[playlist_gallery]
    )

demo.launch()









    






























 