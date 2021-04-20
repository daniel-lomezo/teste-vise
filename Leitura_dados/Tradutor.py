# -*- coding: utf-8 -*-
from google_trans_new import google_translator


class Google_Trad(object):
    def Traduzindo_texto(self, b):
        tradutor = google_translator()
        tradutor_texto = tradutor.translate(b, lang_tgt='pt')
        qt = len(tradutor_texto)
        if qt == 2:
            for i in tradutor_texto:
                return i[1]
        return tradutor_texto

