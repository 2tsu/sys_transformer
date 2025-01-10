import gradio as gr
import os
from PIL import Image

# Placeholder for image paths associated with choices
CONFIGS = {
    "Transformer": {
        "batch=64 layer=7": ["./graphs/b_64_l_7/train_loss.png", "./graphs/b_64_l_7/5d_pred.png", "./graphs/b_64_l_7/30d_pred.png"],#"./graphs/b_64_l_7/valid_loss.png", 
        "batch=64 layer=1": ["./graphs/b_64_l_1/train_loss.png", "./graphs/b_64_l_1/valid_loss.png", "./graphs/b_64_l_1/5d_pred.png", "./graphs/b_64_l_1/30d_pred.png"],
        "batch=32 layer=2": ["./graphs/b_32_l_2/train_loss.png", "./graphs/b_32_l_2/valid_loss.png", "./graphs/b_32_l_2/5d_pred.png", "./graphs/b_32_l_2/30d_pred.png"],
        "batch=16 layer=5": ["./graphs/b_16_l_5/train_loss.png", "./graphs/b_16_l_5/valid_loss.png", "./graphs/b_16_l_5/5d_pred.png", "./graphs/b_16_l_5/30d_pred.png"],
        "batch=16 layer=2": ["./graphs/b_16_l_2/train_loss.png", "./graphs/b_16_l_2/valid_loss.png", "./graphs/b_16_l_2/5d_pred.png", "./graphs/b_16_l_2/30d_pred.png"],
        "batch=16 layer=1":["./graphs/b_16_l_1/train_loss.png", "./graphs/b_16_l_1/valid_loss.png", "./graphs/b_16_l_1/5d_pred.png", "./graphs/b_16_l_1/30d_pred.png"],
        "batch=8 layer=1":["./graphs/b_8_l_1/train_loss.png", "./graphs/b_8_l_1/valid_loss.png", "./graphs/b_8_l_1/5d_pred.png", "./graphs/b_8_l_1/30d_pred.png"],

    },
    "LSTM": {
        "hidden size=400": ["./graphs/lstm_h_400/train_loss.png", "./graphs/lstm_h_400/valid_loss.png", "./graphs/lstm_h_400/5d_pred.png", "./graphs/lstm_h_400/30d_pred.png"],
        "hidden size=800": ["./graphs/lstm_h_800/train_loss.png", "./graphs/lstm_h_800/valid_loss.png", "./graphs/lstm_h_800/5d_pred.png", "./graphs/lstm_h_800/30d_pred.png"],
        "hidden size=100": ["./graphs/lstm_h_100/train_loss.png", "./graphs/lstm_h_100/valid_loss.png", "./graphs/lstm_h_100/5d_pred.png", "./graphs/lstm_h_100/30d_pred.png"],
    }
}
#graphs\b_64_l_7\train_loss.png
import os

for model_configs in CONFIGS.values():
    for config, paths in model_configs.items():
        for path in paths:
            if not os.path.exists(path):
                print(f"Path does not exist: {path}")
                

# CONFIGS の定義はそのまま
def predict(choice):
    for model_configs in CONFIGS.values():
        if choice in model_configs:
            image_paths = model_configs[choice]
            if all(os.path.exists(path) for path in image_paths):
                return [Image.open(path) for path in image_paths]
            break
    return []

def update_hyperparams(model_name):
    if model_name in CONFIGS:
        return gr.update(choices=list(CONFIGS[model_name].keys()))
    return gr.update(choices=[])

with gr.Blocks() as demo:
    gr.Markdown("# Machine Learning Model Configuration Viewer")
    model_selector = gr.Dropdown(
        list(CONFIGS.keys()), 
        label="Select Model"
    )
    hyperparam_selector = gr.Dropdown(
        [], 
        label="Select Configuration", 
        interactive=True
    )
    
    model_selector.change(
        update_hyperparams, 
        inputs=model_selector, 
        outputs=hyperparam_selector
    )
    
    output_plots = gr.Gallery(label="Configuration Results")
    
    predict_button = gr.Button("Show Configuration")
    
    predict_button.click(
        predict, 
        inputs=[hyperparam_selector], 
        outputs=output_plots
    )

demo.launch()