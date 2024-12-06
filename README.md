# Multimodal RAG Project

Проект для автоматизации поиска и индексации документов с использованием мультимодального RAG-подхода.
Включены следующие компоненты:
- Извлечение текстовой информации из различных типов данных (текстовые файлы, PDF, DOCX, изображения, мультимедиа).
- Использование модели `colpali` для получения эмбеддингов.
- Векторная индексация документов с помощью FAISS (или другой векторной БД).
- Поиск релевантных документов и генерация ответа с помощью модели `Qwen/Qwen2.5-72B-Instruct`.

## Структура

- `data/` – Исходные данные
- `models/qwen` – Веса и токенизатор модели QWEN
- `models/colpali` – Веса модели colpali (эмбеддинги)
- `src/pipelines` – Пайплайны обработки различных типов данных
- `src/models` – Обёртки над моделями QWEN и colpali
- `src/index` – Логика индексации (включая векторный индекс)
- `src/search` – Логика поиска по индексам
- `src/utils` – Утилиты для извлечения текста
- `main.py` – Точка входа
- `scripts/download_qwen.py` – Скрипт для загрузки модели Qwen


## Основные шаги:

1. **Подготовка данных**:  
   Разместите ваши данные в каталог `data/`:
   - `data/text/` – текстовые документы (.txt, .pdf, .docx)
   - `data/images/` – изображения и сканированные документы
   - `data/multimedia/` – мультимедийные файлы (например .pptx)
   - `data/metadata/` – файлы с метаданными (например, .json)

2. 

3. 


## Установка моделей

### Загрузка модели Qwen/Qwen2.5-72B-Instruct

1. Установите [Hugging Face CLI](https://huggingface.co/docs/hub/security-tokens) и войдите в систему:

    ```bash
    pip install huggingface_hub
    huggingface-cli login
    ```

2. Запустите скрипт для загрузки модели:

    ```bash
    python scripts/download_qwen.py
    ```

### Загрузка модели Colpali

(Предполагается, что модель colpali аналогично загружается. Если colpali – это другая модель, замените соответствующие части.)

```bash
# Пример загрузки с использованием Sentence Transformers
mkdir -p models/colpali
from sentence_transformers import SentenceTransformer

model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')  # Замените на colpali модель
model.save('models/colpali')
