from googletrans import Translator


translator = Translator()


def get_translated_text(trans_from, trans_to, origin_text):
    translated_obj = translator.translate(
        text=origin_text,
        origin=trans_from,
        dest=trans_to,
    )
    return translated_obj.text


def get_detected_language_obj(sentence):
    return translator.detect(sentence)


def create_translated_file(file_to_translate):
    with open('translated.txt', 'w') as translated_file:
        with open(file_to_translate, 'r') as original_file:
            for line in original_file:
                translated_line = translator.translate(line).text
                translated_file.write(translated_line + '\n')
