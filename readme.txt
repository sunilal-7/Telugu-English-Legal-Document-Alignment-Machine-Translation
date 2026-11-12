TELUGU_PROJECT/
││
├── OCR/
│ ├── input/ # Input PDFs for OCR
│ ├── output/ # OCR extracted TXT files
│ └── run_OCR.py # OCR pipeline script
├── EMBEDDING/
│ ├── input/ # Cleaned input TXT files for embedding
│ ├── aligned_telugu_eng_output.csv # Aligned sentence pairs (for embeddings)
│ └── Embedding.ipynb # Embedding experiments & analysis
│
├── EVALUATION/
│ ├── aligned_telugu_eng_output.csv # Aligned data for evaluation
│ └── sarvam_trans.ipynb # Baseline translation + BLEU/chrF eval
│
├── FINETUNNING/
│ ├── aligned_telugu_eng_output.csv # Final aligned data for training
│ ├── con_2_jonl.ipynb # CSV → JSONL conversion
│ ├── eng_tel_jsonl/ # Generated JSONL training files
│ └── finetunning.ipynb # SFT + LoRA fine-tuning notebook



-----------------------------------------------------------------
-----------------------------------------------------------------


project_root/
│
├── run_OCR.py # OCR pipeline for PDFs
├── input/ # Input PDFs for OCR
├── output/ # OCR extracted TXT files
│
├── ALIGNMENT/
│ └── input/ # Cleaned English & Telugu TXT files
│
├── Embedding.ipynb # Embedding experiments / analysis
├── sarvam_trans.ipynb # Translation + Evaluation (BLEU, chrF)
├── finetunning.ipynb # CSV → JSONL + fine-tuning pipeline

