# PDAN8412 POE Part 1: Author Identification with RNNs

## Scope
Only Part 1 of the PDAN8412 POE (Recurrent Neural Networks, 100 marks).
Scenario: data analyst at a large book press building a fun bot for fans that guesses the author of a passage from its writing style.

## Data
Spooky Author Identification (Kaggle): https://www.kaggle.com/c/spooky-author-identification
File: `Traning Data/train.csv` (19 579 rows; columns id, text, author).
Authors: EAP = Edgar Allan Poe (7 900), MWS = Mary Shelley (6 044), HPL = H.P. Lovecraft (5 635).
test.csv has no labels, so it is NOT used for evaluation. Split train.csv into train, validation and test ourselves.
Known facts: no nulls, no duplicate texts, median of 23 words, max of 861 words (extreme outliers exist).

## Non-negotiable rules
1. Jupyter notebook in `JupyterNotebook/`. Python only.
2. EVERY code cell is followed immediately by a markdown cell that explains, in plain simple English, what the code above does and why.
3. Use Spark (PySpark) for the data analysis (loading, schema, counts, nulls, duplicates, class distribution, length statistics, Spark SQL group bys). Model training uses TensorFlow/Keras, not Spark.
4. Save every chart as a PNG in `figures/` with a clear numbered name (e.g. `figures/03_word_count_by_author.png`) using `plt.savefig(..., dpi=150, bbox_inches="tight")` before `plt.show()`. The report is written from these.
5. Save model comparison results to `outputs/model_comparison.csv` and classification reports to `outputs/`.
6. Set random seeds (numpy, tensorflow, python random) to 42 for reproducibility.
7. Code must be original. Attribute any code adapted from a source or LLM in a comment. Do not copy Kaggle notebooks.
8. Markdown text uses full sentences, and Harvard in-text citations where a source is used.

## Follow the class notebook pattern (lecturer's approach)
Stack: pandas, numpy, re, matplotlib, seaborn, tensorflow.keras (Tokenizer, pad_sequences, Sequential, Embedding, LSTM, GRU, SimpleRNN, Bidirectional, Dropout, Dense), sklearn (train_test_split, LabelEncoder, metrics, compute_class_weight), collections.Counter, nltk (stopwords, word_tokenize, WordNetLemmatizer), wordcloud.
Split: 70/30 stratified train/test, then 20% of train as validation, stratified, random_state=42.
Target: LabelEncoder on author; loss sparse_categorical_crossentropy; softmax output with 3 units.
Tokenizer with num_words and oov_token="<OOV>", fit on training text only.
Choose maxlen from the sequence length distribution (e.g. 95th percentile), not a guess.
Baseline: Embedding(128) then LSTM(64) then Dropout(0.3) then Dense(softmax), adam.
Retrain with EarlyStopping(monitor="val_loss", patience=2, restore_best_weights=True) and adjusted dropout/units, and explicitly document what changed and why.
Evaluate with accuracy, macro precision, recall, F1, classification_report, confusion matrix heatmap, training/validation accuracy and loss curves.
Lecturer request: compare several recurrent models: LSTM, Bidirectional LSTM, GRU (class used RMSprop lr=0.001), and SimpleRNN as a baseline.

## Important adaptation for authorship (explain this in markdown)
Writing style lives in function words and punctuation. For the MODEL input, keep stopwords and meaningful punctuation (commas, semicolons, colons, question and exclamation marks) and do not lemmatise. Stopword removal and lemmatisation are used ONLY for the EDA word frequency, word cloud and n-gram views.

## Notebook structure
1. Setup and imports, seeds, Spark session
2. Load data with Spark: schema, row count, nulls, duplicates, class distribution (Spark SQL)
3. Data quality: empty/very short texts, extreme length outliers, encoding oddities
4. EDA
   a. Class balance bar chart
   b. Word and character count histograms, and boxplots by author
   c. Top words overall and per author (with and without stopwords)
   d. Word cloud per author
   e. Bigrams and trigrams per author
   f. Stylometric features per author: average word length, commas, semicolons, colons, question marks, exclamation marks, quotes per sentence, stopword ratio, vocabulary richness (type token ratio)
   g. Vocabulary size and overlap between authors
   h. Token sequence length distribution to choose maxlen, and OOV coverage for the chosen num_words
5. Feature selection: vocab size (num_words), maxlen, keeping punctuation and stopwords; chi-square on word counts to show the most author-discriminative words (supports the brief's P value hint)
6. Preprocessing for the model: clean text, label encode, split, tokenize, pad
7. Models: baseline LSTM, tuned LSTM (early stopping, dropout), Bidirectional LSTM, GRU, SimpleRNN; optionally class weights
8. Evaluation per model: curves, test accuracy, macro P/R/F1, log loss, confusion matrix, training time, parameter count
9. Model comparison table and chart; choose the best model with justification
10. The fan bot: a `predict_author(text)` function that returns the most likely author with probabilities, demonstrated on a few sample sentences
