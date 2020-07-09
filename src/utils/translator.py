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
