from transformers import AutoModelForCausalLM, AutoTokenizer
import os

def download_qwen(model_name: str, save_directory: str):
    if not os.path.exists(save_directory):
        os.makedirs(save_directory)
    
    print(f"Загрузка токенизатора модели {model_name}...")
    tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)
    tokenizer.save_pretrained(save_directory)
    
    print(f"Загрузка модели {model_name} с использованием disk_offload...")
    model = AutoModelForCausalLM.from_pretrained(
        model_name,
        torch_dtype="auto",
        device_map="auto",
        trust_remote_code=True,
        offload_folder="offload",
        offload_state_dict=True  # Включает offload состояния модели
    )
    model.save_pretrained(save_directory)
    print(f"Модель успешно сохранена в {save_directory}")

if __name__ == "__main__":
    MODEL_NAME = "Qwen/Qwen2-7B-Instruct"  # Убедитесь, что это правильное имя модели на Hugging Face
    SAVE_DIR = "models/qwen"
    download_qwen(MODEL_NAME, SAVE_DIR)
