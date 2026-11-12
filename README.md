# Telugu-English Legal Document Alignment & Machine Translation

## Overview

This project focuses on developing a Telugu-English document alignment and machine translation pipeline for legal documents.

The pipeline includes OCR-based text extraction, multilingual sentence embeddings, semantic sentence alignment, translation evaluation, and model fine-tuning.

## Project Workflow

1. **OCR:** Extract text from Telugu and English legal PDF documents.
2. **Sentence Alignment:** Generate multilingual embeddings and identify semantically corresponding sentences.
3. **Translation Evaluation:** Perform baseline translation and evaluate using BLEU and chrF metrics.
4. **Fine-Tuning:** Convert aligned data into JSONL format and fine-tune a translation model using Supervised Fine-Tuning (SFT) and LoRA.

## Technologies Used

- Python
- Jupyter Notebook
- OCR
- Multilingual Sentence Embeddings
- Sarvam Translation
- BLEU and chrF
- JSONL
- LoRA / PEFT

## Project Structure

```text
TELUGU_PROJECT/
├── OCR/
│   ├── input/
│   ├── output/
│   └── run_OCR.py
├── EMBEDDING/
│   ├── input/
│   ├── aligned_telugu_eng_output.csv
│   └── Embedding.ipynb
├── EVALUATION/
│   ├── aligned_telugu_eng_output.csv
│   └── sarvam_trans.ipynb
├── FINETUNNING/
│   ├── aligned_telugu_eng_output.csv
│   ├── con_2_jonl.ipynb
│   ├── eng_tel_jsonl/
│   └── finetunning.ipynb
└── README.md
```

## Evaluation Metrics

- **BLEU:** Measures translation quality using n-gram precision.
- **chrF:** Evaluates translation quality using character-level n-grams.

## Expected Outcome

- Extracted legal documents.
- Aligned Telugu-English sentence pairs.
- Baseline translation evaluation.
- Fine-tuned machine translation model.

## Project Status

Under Development.
