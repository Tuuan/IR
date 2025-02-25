import phonlp
import py_vncorenlp

segmenter = py_vncorenlp.VnCoreNLP(annotators=["wseg"], save_dir='vncorenlp')
model = phonlp.load(save_dir='phonlp')

def ner(text):
    sentences = segmenter.word_segment(text)
    result = {}
    sentences = segmenter.word_segment(text)
    for sentence in sentences:
        _, word, pos, ner, _, _ = model.annotate(sentence)
        for w, p, n in zip(word, pos, ner):
            if n != "O":
                if n in result:
                    result[n].append(w)
                else:
                    result[n] = [w]
                continue
            if p in result:
                result[p].append(w)
            else:
                result[p] = [w]
                
    return result