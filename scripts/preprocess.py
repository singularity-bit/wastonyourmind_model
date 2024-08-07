import typer
import srsly
from pathlib import Path
from spacy.util import get_words_and_spaces
from spacy.tokens import Doc, DocBin
import spacy

def main(
    input_path: Path = typer.Argument(..., exists=True, dir_okay=False),
    output_path: Path = typer.Argument(..., dir_okay=False),
):
    print(f"Starting preprocessing!")
    nlp = spacy.blank("en")
    doc_bin = DocBin(attrs=["ENT_IOB", "ENT_TYPE"])
    for eg in srsly.read_jsonl(input_path):
        # if eg["answer"] != "accept":
        #     continue
        spacyTokens=nlp(eg["text"])
        tokens = [token.text for token in spacyTokens]
        words, spaces = get_words_and_spaces(tokens, eg["text"])

        doc = Doc(nlp.vocab, words=words, spaces=spaces)
        ents=[
            doc.char_span(s["start"], s["end"], label=s["label"])
            for s in eg.get("spans", []) if doc.char_span(s["start"], s["end"], label=s["label"])
        ]
        doc.ents=ents

        doc_bin.add(doc)
    doc_bin.to_disk(output_path)
    print(f"Processed {len(doc_bin)} documents: {output_path.name}")

if __name__ == "__main__":
    typer.run(main)
