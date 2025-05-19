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
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------- | ---------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- |
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
| [textdetox/multilingual_toxic_lexicon · Datasets at Hugging Face](https://huggingface.co/datasets/textdetox/multilingual_toxic_lexicon)                                                                                                | Словарь токсичных слов                                                                                                                                                    | en, ru, uk, de, es, am, zh, ar, hi, it, fr, he, hin, tt, ja | 200-141k                                                               | 1. поиск токсичных комментов в интернете.<br>2. Токсификация нейтриальных предложений                                                               |
| [textdetox/multilingual_paradetox_test · Datasets at Hugging Face](https://huggingface.co/datasets/textdetox/multilingual_paradetox_test)                                                                                              | Тест                                                                                                                                                                      | en, ru, uk, de, es, am, zh, ar, hi, it, fr, he, hin, tt, ja | 100-600                                                                | Валидировать модель на части метрик, где не нужен таргет (STA, SIM, мб Fluency)                                                                     |
| [GitHub - deepanshu1995/HateSpeech-Hindi-English-Code-Mixed-Social-Media-Text](https://github.com/deepanshu1995/HateSpeech-Hindi-English-Code-Mixed-Social-Media-Text)                                                                 | Нейтральные и токсичные сообщения на Hindi-English                                                                                                                        | hin                                                         | 4k                                                                     | Генерация синты, но только айди твитов, за доступом надо писать на почту [deepanshuvijay01995@gmail.com](mailto:deepanshuvijay01995@gmail.com)      |

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