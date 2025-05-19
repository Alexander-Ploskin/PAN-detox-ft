# Detoxification 2025

## Данные

В сореве модель тестируется на 

- en — English

- ru — Russian

- uk — Ukrainian

- de — German 

- es — Spanish

- am — Amhairc

- zh — Chineese

- ar — Arabic

- hi — Hindi

- it — Italian

- fr — Franch

- he — Hebrew

- hin — Hinglish

- tt — Tatar

- ja — Japanese

| Ссылка                                                                                                                                                                                                                                 | Описание                                                                                                                                                                  | Язык                                                        | Количество примеров                                                    | Как можем использовать                                                                                                                              |
|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------- | ---------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| [textdetox/multilingual_paradetox · Datasets at Hugging Face](https://huggingface.co/datasets/textdetox/multilingual_paradetox)                                                                                                        | Основной датасет задачи, соджержит пары токсичное предлождение и его детокс версия                                                                                        | en, ru, uk, de, es, am, zh, ar, hi                          | По 400 на каждый язык                                                  |                                                                                                                                                     |
| [textdetox/multilingual_toxicity_dataset · Datasets at Hugging Face](https://huggingface.co/datasets/textdetox/multilingual_toxicity_dataset)                                                                                          | Датасет для классфикации токсичности предложений (всезде 50% токстичных и 50% нетоксичных)                                                                                | en, ru, uk, de, es, am, zh, ar, hi, it, fr, he, hin, tt, ja | По 5k на каждый язык кроме he и hin, в них 2k и 4.3k  соотв            |                                                                                                                                                     |
| [GitHub - leondz/hatespeechdata: Catalog of abusive language data (PLoS 2020)](https://github.com/leondz/hatespeechdata)                                                                                                               | Сборная солянка из ссылок на датасеты и ключевые слова, для каждого языка по-разному                                                                                      | en, ru, uk, zh, de, it, es, ar                              | Очень много датасетов, есть даже hinglish, но все они на классификацию | Можем поставить эксперимент: взять дипсик, дать во фью-шот примеры из para-detox'а, посмотреть, если он выбивает хороший скор, то размечаем датасет |
| [SvetlanaKayfajian/ss-toxicator · Datasets at Hugging Face](https://huggingface.co/datasets/SvetlanaKayfajian/ss-toxicator/viewer/default/train?p=340)                                                                                 | Неразмеченные по языкам пары toxic-neutral, не факт, что хорошие (это генерация [SOURCE](https://huggingface.co/SvetlanaKayfajian/my_mt5_small_test-finetuned-textdetox)) | ru, uk, zh, hi, es, de, ar, am, en (мб еще каке-то есть)    | 35k, разбивку надо делать самим                                        | Если хороший датасет, то можно для обучения использовать, но скорее всего нет 2025 языков                                                           |
| [multilingual-transformer-detoxification/mt0_detox_full_data.csv at main · s-nlp/multilingual-transformer-detoxification · GitHub](https://github.com/s-nlp/multilingual-transformer-detoxification/blob/main/mt0_detox_full_data.csv) | Решение прошлого года на каком-то датасете, топ-бейзлайн сейчас                                                                                                           | en, ru, uk, de, es, am, zh, ar, hi                          | 55k                                                                    | можем тренировать свои модели на популярных изыках или переиспользовать                                                                             |
| [yasalma/tatar-exams · Datasets at Hugging Face](https://huggingface.co/datasets/yasalma/tatar-exams)                                                                                                                                  | Типа MMLU на татарском, подходит для выбора базовой модели                                                                                                                | tt                                                          | похер                                                                  | можем выбирать модель для генерации данных/детокса, но нам нужна fluent, а не умная модель                                                          |
| [s-nlp/paradetox · Datasets at Hugging Face](https://huggingface.co/datasets/s-nlp/paradetox/viewer/default/train?p=197)                                                                                                               | Большой парадетокс                                                                                                                                                        | en                                                          | 20k                                                                    | хороший датасет для трейна, описана схема, по которому его строили, можем переиспользовать для языков, для которых нет данных                       |
| [s-nlp/ru_paradetox · Datasets at Hugging Face](https://huggingface.co/datasets/s-nlp/ru_paradetox)                                                                                                                                    | Большой парадетокс                                                                                                                                                        | ru                                                          | 11k                                                                    | то же, что и en                                                                                                                                     |
| [textdetox/uk_paradetox · Datasets at Hugging Face](https://huggingface.co/datasets/textdetox/uk_paradetox)                                                                                                                            | Большой парадетокс                                                                                                                                                        | uk                                                          | 4k                                                                     | то же, что и en                                                                                                                                     |
| [textdetox/es_paradetox · Datasets at Hugging Face](https://huggingface.co/datasets/textdetox/es_paradetox)                                                                                                                            | Не очень большой парадетокс                                                                                                                                               | es                                                          | 500                                                                    | то же, что и en                                                                                                                                     |
| [textdetox/multilingual_toxic_lexicon · Datasets at Hugging Face](https://huggingface.co/datasets/textdetox/multilingual_toxic_lexicon)                                                                                                | Словарь токсичных слов                                                                                                                                                    | en, ru, uk, de, es, am, zh, ar, hi, it, fr, he, hin, tt, ja | 200-141k                                                               | 1. поиск токсичных комментов в интернете.<br/>2. Токсификация нейтриальных предложений                                                              |
| [textdetox/multilingual_paradetox_test · Datasets at Hugging Face](https://huggingface.co/datasets/textdetox/multilingual_paradetox_test)                                                                                              | Тест                                                                                                                                                                      | en, ru, uk, de, es, am, zh, ar, hi, it, fr, he, hin, tt, ja | 100-600                                                                | Валидировать модель на части метрик, где не нужен таргет (STA, SIM, мб Fluency)                                                                     |
| https://github.com/deepanshu1995/HateSpeech-Hindi-English-Code-Mixed-Social-Media-Text                                                                                                                                                 | Нейтральные и токсичные сообщения на Hindi-English                                                                                                                        | hin                                                         | 4k                                                                     | Генерация синты, но только айди твитов, за доступом надо писать на почту deepanshuvijay01995@gmail.com                                              |

## Данные по языкам

|                | train |     |     | validate |
| -------------- | ----- | --- | --- | -------- |
| en — English   |       |     |     |          |
| ru — Russian   |       |     |     |          |
| uk — Ukrainian |       |     |     |          |
| de — German    |       |     |     |          |
| es — Spanish   |       |     |     |          |
| am — Amhairc   |       |     |     |          |
| zh — Chineese  |       |     |     |          |
| ar — Arabic    |       |     |     |          |
| hi — Hindi     |       |     |     |          |
| it — Italian   |       |     |     |          |
| fr — French    |       |     |     |          |
| he — Hebrew    |       |     |     |          |
| hin — Hinglish |       |     |     |          |
| tt — Tatar     |       |     |     |          |
| ja — Japanese  |       |     |     |          |



## Модели

| Ссылка                                                                                                              | Описание | Размер | Языки | Как можем использовать |
| ------------------------------------------------------------------------------------------------------------------- | -------- | ------ | ----- | ---------------------- |
| [s-nlp/mt0-xl-detox-orpo · Hugging Face](https://huggingface.co/s-nlp/mt0-xl-detox-orpo)                            |          |        |       |                        |
| [textdetox/mt5-xl-detox-baseline · Hugging Face](https://huggingface.co/textdetox/mt5-xl-detox-baseline)            |          |        |       |                        |
| [textdetox/mbart-detox-baseline · Hugging Face](https://huggingface.co/textdetox/mbart-detox-baseline)              |          |        |       |                        |
| [s-nlp/ruT5-base-detox · Hugging Face](https://huggingface.co/s-nlp/ruT5-base-detox)                                |          |        |       |                        |
| [MT5 release - a google Collection](https://huggingface.co/collections/google/mt5-release-65005f1a520f8d7b4d039509) |          |        |       |                        |
| [bigscience/mt0-xl · Hugging Face](https://huggingface.co/bigscience/mt0-xl)                                        |          |        |       |                        |
| [facebook/mbart-large-50 · Hugging Face](https://huggingface.co/facebook/mbart-large-50)                            |          |        |       |                        |
| [ai-forever/mGPT-1.3B-tatar · Hugging Face](https://huggingface.co/ai-forever/mGPT-1.3B-tatar)                      |          |        |       |                        |
| [google/gemma-scope · Hugging Face](https://huggingface.co/google/gemma-scope)                                      |          |        |       |                        |
| [Tweeties/tweety-7b-tatar-v24a · Hugging Face](https://huggingface.co/Tweeties/tweety-7b-tatar-v24a)                |          |        |       |                        |
|                                                                                                                     |          |        |       |                        |
|                                                                                                                     |          |        |       |                        |

## Бейзлайны из соревнования

![Unsupervised Baselines](https://pan.webis.de/clef25/pan25-figures/detox_baselines.png)

### Duplicate

### Delete

### Backtranslation

### mt0-xl-orpo

[GitHub - s-nlp/multilingual-transformer-detoxification: A code for PAN-2024 Multilingual Text Detoxification](https://github.com/s-nlp/multilingual-transformer-detoxification/tree/main)

## Метрика

**На протяжении всего конкурса будет доступен набор автоматических метрик оценки.** Мы предоставляем многоязычный автоматизированный конвейер оценки, основанный на трёх ключевых параметрах:

- **Точность переноса стиля (Style Transfer Accuracy, STA)**: Для сгенерированного парафраза определяется уровень **нетоксичности**. Для этого используется специально дообученная модель **xlm-roberta-large** для бинарной классификации токсичности ([классификатор](https://huggingface.co/textdetox/xlmr-large-toxicity-classifier-v2)).  
  *🔹 Пояснение: Чем выше значение STA (ближе к 1), тем менее токсичным считается текст.*

- **Сохранение содержания (Content preservation, SIM)**: Оценивается смысловая близость двух текстов. Рассчитывается как косинусная близость между эмбеддингами модели [LaBSe](https://huggingface.co/sentence-transformers/LaBSE).  
  🔹 Пояснение: Если SIM = 1, содержание исходного и преобразованного текста идентично; если 0 — полностью разное.*

- **Грамотность (Fluency, FL)**: Для оценки естественности текста и его соответствия человеческим эталонам детоксификации используется модель **[xCOMET](https://huggingface.co/myyycroft/XCOMET-lite)**. Наши эксперименты показали, что COMET-модели (из машинного перевода) идеально коррелируют с экспертной оценкой грамотности в детоксифицированных текстах.  
  
  🔹 *Пояснение: FL = 1 означает, что текст звучит так же естественно, как написанный человеком.*

Каждая метрика принимает значения в диапазоне **[0; 1]**. Для формирования единого критерия в таблице лидеров (**Joint metric, J**) мы усредняем комбинацию **STA × SIM × FL** для каждого примера.

### **[Обновление метрик в 2025 году]**

По сравнению с 2024 годом, формула расчёта **J** значительно усовершенствована. Теперь каждая метрика (**STA, SIM, FL**) учитывает **человеческие эталоны**:

- **STA**: Проверяется не только вероятность нетоксичности выходного текста, но и то, насколько его оценка **ниже**, чем у эталонных человеческих детоксификаций.  
  *🔹 Пояснение: Это важно, потому что даже ручная детоксификация иногда неидеальна.*

- **SIM**: Вычисляется **взвешенная сумма** сходства выходного текста с исходным предложением **и** с человеческой детоксификацией.

- **FL**: Метрика **xCOMET** (вдохновлённая оценкой машинного перевода) измеряет близость выходного текста к эталону, написанному человеком.

### Финальная формула:

![Final Formula](https://latex.codecogs.com/png.latex?J%20%3D%20xCOMMET_%7B%5Ctext%7Bfluency%7D%7D%28%5Ctext%7Binput%7D%2C%20%5Ctext%7Boutput%7D_%5Ctext%7Bref%7D%2C%20%5Ctext%7Boutput%7D_%7B%5Ctext%7Bgenerated%7D%7D%29%20%5Ctimes%20%280.4%20%5Ctimes%20%5Ctext%7BSimilarity%7D%28%5Ctext%7Binput%7D%2C%20%5Ctext%7Boutput%7D_%7B%5Ctext%7Bgenerated%7D%7D%29%20%2B%200.6%20%5Ctimes%20%5Ctext%7BSimilarity%7D%28%5Ctext%7Boutput%7D_%5Ctext%7Bref%7D%2C%20%5Ctext%7Boutput%7D_%7B%5Ctext%7Bgenerated%7D%7D%29%29%20%5Ctimes%20%5Ctext%7BSTA%7D)

### STA:

![STA Formula](https://latex.codecogs.com/png.latex?%5Ctext%7BSTA%7D%20%3D%20%5Cdfrac%7B%5Ctext%7Bsta%5C_scores%7D%20%2B%20%5Cdfrac%7B%5Csum%20%5Ctext%7Bcompared%5C_scores%7D%20%7D%20%7B%5Ctext%7Blen%28compared%5C_scores%29%7D%7D%7D%7B%5Ctext%7Bref%5C_sta%5C_scores%7D%7D)

### Где:

1. ![sta_scores](https://latex.codecogs.com/png.latex?%5Ctext%7Bsta%5C_scores%7D%20%3D%20%5Ctext%7Bclassifer%5C_prob%5C_neutral%7D%28%5Ctext%7Boutput%7D_%7B%5Ctext%7Bgenerated%7D%7D%29)
2. ![compared_scores](https://latex.codecogs.com/png.latex?%5Ctext%7Bcompared%5C_scores%7D%20%3D%20%5Ctext%7Bsta%5C_scores%7D%20%5Cleq%20%5Ctext%7Bref%5C_sta%5C_scores%7D)
3. ![ref_sta_scores](https://latex.codecogs.com/png.latex?%5Ctext%7Bref%5C_sta%5C_scores%7D%20%3D%20%5Ctext%7Bclassifer%5C_prob%5C_neutral%7D%28%5Ctext%7Boutput%7D_%7B%5Ctext%7Bref%7D%7D%29)

[Код для скоринга тут](https://github.com/pan-webis-de/pan-code/tree/master/clef25/text-detoxification)

### Пейперы

| Paper Title                                                                 | Key Idea                                                      | Languages                                                    | Main Contribution                                                                                 | Paper Link |
|-----------------------------------------------------------------------------|---------------------------------------------------------------|--------------------------------------------------------------|---------------------------------------------------------------------------------------------------|------------|
| Overview of the Multilingual Text Detoxification Task at PAN 2024           | Introduces shared task for multilingual detoxification         | 9 languages (EN, ES, DE, ZH, AR, HI, UK, RU, AM)             | Provides datasets, baselines, and evaluation results across 9 languages.                          | [PDF](https://ceur-ws.org/Vol-3740/paper-223.pdf) |
| Multilingual Text Detoxification Using Google Cloud Translation and...       | Combines translation (NLLB) + BART/ruT5 detox models           | EN, RU, others via translation                               | Achieves competitive results via translation-based cross-lingual detoxification.                  | [PDF](https://ceur-ws.org/Vol-3740/paper-263.pdf) |
| LLMs to Replace Crowdsourcing For Parallel Data Creation                    | Activation-patched LLMs (Llama-3) for pseudo-parallel data     | English (methodology generalizable)                          | Generates detox data comparable to human-annotated corpora.                                       | [PDF](https://aclanthology.org/2024.findings-emnlp.839/) |
| SmurfCat at PAN 2024 TextDetox: Alignment of Multilingual Transformers...   | mT0-XL + ORPO alignment + data augmentation                    | 9 languages                                                  | State-of-the-art for Ukrainian; 2nd in human evaluation.                                          | [arXiv](https://arxiv.org/abs/2407.05449) |
| Text Detoxification with Cross-Lingual Style Transfer                       | Combines mT5/mBART with translation pipelines                  | EN, RU, ES, DE, ZH                                           | Evaluates cross-lingual detox via backtranslation and adapter-based methods.                      | [PDF](https://ceur-ws.org/Vol-3740/paper-280.pdf) |
| Team SomethingAwful (LaMa-3 & mT0-XL)                                       | Few-shot prompting with "uncensored" LLaMa-3 and mT0-XL        | 8 languages + mT0-XL for Amharic                             | Achieved 2nd place in human evaluation (Joint score: 0.774).                                      | [PDF](https://ceur-ws.org/Vol-3740/paper-223.pdf) |
| Team ZhongyuLuo (Translation & BART-detox)                                  | Translation + BART/ruT5 detox + postprocessing                 | EN, RU, ZH                                                   | Hybrid approach combining translation and monolingual detox models.                               | [PDF](https://ceur-ws.org/Vol-3740/paper-263.pdf) |
| Team MBZUAI-UnbabelDetox (GPT-3.5)                                          | Two-step GPT-3.5 prompting for synthetic data generation       | 9 languages                                                  | Generated synthetic detox data for few-shot prompting.                                            | [PDF](https://ceur-ws.org/Vol-3740/paper-223.pdf) |
| Team dkenco (Cotype-7b)                                                     | Few-shot Cotype-7b prompting                                   | EN, RU                                                       | Tested region-specific LLMs for detoxification.                                                   | [PDF](https://ceur-ws.org/Vol-3740/paper-223.pdf) |





## Возможные подходы

TODO

## Результаты

### Baseline Duplicate

Конфиг : —

Run W&B : —

Краткое описание : Вход подается на выход

Результаты:

| Language           | STA   | SIM   | CHRF  | J     | XCOMET |
| ------------------ | ----- | ----- | ----- | ----- | ------ |
| am                 | 0.730 | 0.810 | 0.486 | 0.461 | 0.760  |
| ar                 | 0.680 | 0.926 | 0.776 | 0.564 | 0.890  |
| de                 | 0.630 | 0.946 | 0.812 | 0.572 | 0.959  |
| en                 | 0.533 | 0.892 | 0.670 | 0.353 | 0.739  |
| es                 | 0.700 | 0.887 | 0.655 | 0.566 | 0.902  |
| fr                 | 0.522 | 0.947 | 0.827 | 0.458 | 0.926  |
| he                 | 0.570 | 0.827 | 0.544 | 0.405 | 0.841  |
| hi                 | 0.539 | 0.889 | 0.695 | 0.417 | 0.865  |
| hin                | 0.596 | 0.885 | 0.682 | 0.418 | 0.778  |
| it                 | 0.745 | 0.963 | 0.810 | 0.656 | 0.912  |
| ja                 | 0.524 | 0.946 | 0.763 | 0.438 | 0.884  |
| ru                 | 0.525 | 0.895 | 0.699 | 0.424 | 0.899  |
| tt                 | 0.734 | 0.929 | 0.784 | 0.587 | 0.855  |
| uk                 | 0.516 | 0.940 | 0.778 | 0.442 | 0.910  |
| zh                 | 0.630 | 0.874 | 0.536 | 0.477 | 0.857  |
| Average_p J        | -     | -     | -     | 0.475 | -      |
| Average_np J       | -     | -     | -     | 0.493 | -      |
| Average all XCOMET | -     | -     | -     | 0.865 | -      |

### Baseline Delete

Конфиг : —

Run W&B : —

Краткое описание : С помощью словаря вырезаются все токсиные слова

Результаты:

| Language           | STA   | SIM   | CHRF  | J     | XCOMET |
| ------------------ | ----- | ----- | ----- | ----- | ------ |
| am                 | 0.750 | 0.808 | 0.487 | 0.461 | 0.739  |
| ar                 | 0.788 | 0.916 | 0.778 | 0.611 | 0.842  |
| de                 | 0.657 | 0.941 | 0.803 | 0.586 | 0.949  |
| en                 | 0.826 | 0.882 | 0.689 | 0.473 | 0.663  |
| es                 | 0.795 | 0.878 | 0.662 | 0.603 | 0.854  |
| fr                 | 0.647 | 0.948 | 0.832 | 0.524 | 0.863  |
| he                 | 0.659 | 0.823 | 0.548 | 0.445 | 0.777  |
| hi                 | 0.630 | 0.886 | 0.706 | 0.480 | 0.848  |
| hin                | 0.622 | 0.878 | 0.676 | 0.421 | 0.753  |
| it                 | 0.854 | 0.948 | 0.796 | 0.676 | 0.834  |
| ja                 | 0.524 | 0.946 | 0.763 | 0.438 | 0.884  |
| ru                 | 0.663 | 0.889 | 0.709 | 0.514 | 0.869  |
| tt                 | 0.775 | 0.926 | 0.790 | 0.611 | 0.843  |
| uk                 | 0.707 | 0.932 | 0.792 | 0.581 | 0.884  |
| zh                 | 0.831 | 0.818 | 0.525 | 0.516 | 0.748  |
| Average_p J        | -     | -     | -     | 0.536 | -      |
| Average_np J       | -     | -     | -     | 0.519 | -      |
| Average all XCOMET | -     | -     | -     | 0.823 | -      |

### Файнтюн mT5 на Paradetox

Конфиг : TODO

Run W&B : [Weights & Biases](https://wandb.ai/kozlovskij-vu/huggingface?nw=nwuserkozlovskijvu)

Краткое описание : Файнтюн втупую на парном датасете

Результаты:

| Language           | STA   | SIM   | CHRF  | J     | XCOMET |
| ------------------ | ----- | ----- | ----- | ----- | ------ |
| am                 | 0.842 | 0.623 | 0.292 | 0.309 | 0.562  |
| ar                 | 0.781 | 0.667 | 0.588 | 0.328 | 0.605  |
| de                 | 0.813 | 0.837 | 0.618 | 0.587 | 0.853  |
| en                 | 0.881 | 0.844 | 0.688 | 0.598 | 0.791  |
| es                 | 0.805 | 0.824 | 0.611 | 0.557 | 0.819  |
| fr                 | 0.630 | 0.814 | 0.637 | 0.408 | 0.763  |
| he                 | 0.724 | 0.674 | 0.380 | 0.326 | 0.631  |
| hi                 | 0.719 | 0.822 | 0.649 | 0.487 | 0.786  |
| hin                | 0.636 | 0.749 | 0.528 | 0.315 | 0.628  |
| it                 | 0.788 | 0.819 | 0.590 | 0.509 | 0.758  |
| ja                 | 0.542 | 0.887 | 0.628 | 0.385 | 0.786  |
| ru                 | 0.851 | 0.833 | 0.648 | 0.597 | 0.824  |
| tt                 | 0.692 | 0.783 | 0.604 | 0.419 | 0.741  |
| uk                 | 0.841 | 0.851 | 0.679 | 0.601 | 0.820  |
| zh                 | 0.733 | 0.780 | 0.434 | 0.448 | 0.772  |
| Average_p          | -     | -     | -     | 0.501 | -      |
| Average_np J       | -     | -     | -     | 0.394 | -      |
| Average all XCOMET | -     | -     | -     | 0.743 | -      |

Анализ: 
