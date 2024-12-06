import argparse
import os
from src.pipelines.text_pipeline import TextPipeline
from src.pipelines.image_pipeline import ImagePipeline
from src.pipelines.multimedia_pipeline import MultimediaPipeline
from src.pipelines.metadata_pipeline import MetadataPipeline
from src.index.indexer import Indexer
from src.search.searcher import Searcher
from src.models.qwen_wrapper import QWENModel

def process_all(data_path: str = 'data', index_path: str = 'models/index.pkl'):
    # Обработка текстовых документов
    tp = TextPipeline(f"{data_path}/text")
    text_docs = tp.process_documents()

    # Обработка изображений
    ip = ImagePipeline(f"{data_path}/images")
    img_docs = ip.process_images()

    # Обработка мультимедиа
    mp = MultimediaPipeline(f"{data_path}/multimedia")
    mm_docs = mp.process_multimedia()

    # Обработка метаданных
    mdp = MetadataPipeline(f"{data_path}/metadata")
    md_docs = mdp.process_metadata()

    all_docs = text_docs + img_docs + mm_docs + md_docs

    indexer = Indexer()
    indexer.build_index(all_docs)

    # Сохраняем индекс
    indexer.save_index(index_path)
    return indexer

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--process_all", action="store_true", help="Предварительно обработать все данные и построить индекс")
    parser.add_argument("--query", type=str, help="Запрос к системе")
    parser.add_argument("--index_path", type=str, default="models/index.pkl", help="Путь к файлу индекса")
    args = parser.parse_args()

    if args.process_all:
        process_all(index_path=args.index_path)
        print("Индекс создан и сохранён.")
    elif args.query:
        indexer = Indexer()
        if os.path.exists(args.index_path):
            indexer.load_index(args.index_path)
        else:
            # Если индекса нет, создаём заново
            indexer = process_all(index_path=args.index_path)

        searcher = Searcher(indexer.get_vector_index())
        results = searcher.search(args.query, top_k=3)

        # Формируем контекст из найденных документов
        context = ""
        for r in results:
            context += r.get('content', '') + "\n"

        qwen = QWENModel(model_path="models/qwen")
        answer = qwen.generate_answer(context=context, query=args.query)
        print("Ответ:", answer)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
