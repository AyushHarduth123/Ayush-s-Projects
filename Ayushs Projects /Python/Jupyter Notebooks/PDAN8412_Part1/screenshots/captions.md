# Notebook screenshots and captions

Each image shows one code cell of PDAN8412_Part1_Full_Analysis.ipynb together with its output.

**01_imports_and_versions.png**: Loads every library used in the notebook and prints the Python, NumPy, pandas and TensorFlow versions, together with the devices available for training.

**02_seed_and_paths.png**: Fixes the random seed at 42 for Python, NumPy and TensorFlow so the results can be repeated, and sets up the data, figures and outputs folders.

**03_chart_style_and_authors.png**: Sets one chart style for the whole notebook and gives each author a fixed colour from a colour blind friendly palette so that every chart is read the same way.

**04_load_dataset_head.png**: Reads train.csv into a table, prints its shape and column names, and shows the first five rows.

**05_info_and_describe.png**: Prints the technical summary of the table, showing the type of each column, how many values are filled in, and the number of unique values in each column.

**06_sample_sentences.png**: Displays eight randomly chosen sentences so that the real text can be read before any modelling.

**07_class_counts.png**: Counts the sentences belonging to each author and converts the counts into percentages.

**08_missing_and_duplicates.png**: Checks for missing values, duplicate rows, duplicate ids, duplicate sentences, near duplicates that differ only in case or spacing, and sentences labelled with more than one author.

**09_very_short_texts.png**: Adds word and character counts to the table and lists the sentences with fewer than four words together with their authors.

**10_length_outliers.png**: Prints the percentiles of the sentence lengths, works out the boxplot cut off for an outlier, counts the sentences beyond it and shows the five longest sentences.

**11_characters_and_punctuation.png**: Lists every character outside plain English letters with its Unicode name, counts them per author, inventories the punctuation and checks for marks that never appear.

**12_data_quality_summary.png**: Collects every quality check into one table of findings and decisions and saves it as a CSV file.

**13_class_balance_chart.png**: Draws the bar chart of the number of sentences per author with the counts and percentages written above each bar.

**14_length_histograms.png**: Draws histograms of the words and the characters per sentence, with a separate outline for each author.

**15_length_boxplots.png**: Draws boxplots of sentence length by author on a logarithmic scale and prints the mean, median, spread, minimum and maximum for each author.

**16_eda_text_views.png**: Builds the three cleaned views of each sentence used by the exploration, namely the plain words, the words without stopwords and the lemmatised words.

**17_top_words_overall.png**: Counts how often every word appears and charts the twenty most common words, once with stopwords kept and once with them removed.

**18_top_words_by_author.png**: Charts the twelve most common words for each author, with stopwords kept on the top row and removed on the bottom row.

**19_word_clouds.png**: Draws one word cloud per author from the lemmatised words with stopwords removed.

**20_bigrams_and_trigrams.png**: Finds and charts the ten most common word pairs and word triples for each author.

**21_style_feature_table.png**: Measures ten writing style features for every sentence and prints their averages per author, including the punctuation marks per hundred words.

**22_style_charts_and_tests.png**: Charts each style feature by author with confidence intervals and runs a Kruskal Wallis test on each feature to check whether the differences are real.

**23_vocabulary_overlap.png**: Compares the vocabularies of the three authors, including an equally sized sample from each author, the words unique to each author and the overlap between them.

**24_cleaning_for_model.png**: Applies the light cleaning used for the model input and prints three sentences before and after cleaning.

**25_label_encoding.png**: Turns the three author labels into the numbers that the network needs and prints the mapping.

**26_train_validation_test_split.png**: Splits the sentences into training, validation and test sets and prints the size and author mix of each set.

**27_sequence_length_and_maxlen.png**: Summarises the token lengths of the training sentences, chooses the common input length from the 95th percentile and reports how much text would be cut.

**28_vocabulary_coverage.png**: Counts how often every training token appears, charts how much of the text is covered as the word list grows and chooses the size of the word list.

**29_chi_square_words.png**: Runs the chi square test on the training words and shows the words most strongly linked to each author.

**30_chi_square_punctuation.png**: Runs the same chi square test on the punctuation marks and shows the average number of each mark per sentence for each author.

**31_feature_decisions.png**: Collects every feature and setting decision into one table with the evidence behind it and saves it as a CSV file.

**32_tokenize_and_pad.png**: Fits the tokenizer on the training text only, converts all three sets into sequences of numbers, pads them to the chosen length and reports the share of unknown tokens in the test set.

**33_model_helper_functions.png**: Defines the reusable functions that build and train every model in exactly the same way, so that the comparison between models is fair.

**34_padding_experiment.png**: Trains a small LSTM and a SimpleRNN twice each to test whether padding at the start or at the end of a sentence works better.

**35_baseline_lstm.png**: Builds and trains the baseline LSTM from the class notebook for a fixed twelve epochs and prints its layer summary.

**36_lstm_tuning_grid.png**: Trains four LSTMs with early stopping across two layer sizes and two dropout rates and picks the combination with the lowest validation loss.

**37_bidirectional_lstm.png**: Trains the Bidirectional LSTM with the chosen units and dropout.

**38_gru_models.png**: Trains the GRU twice, once with Adam and once with the RMSprop optimiser used in the class notebook.

**39_simplernn.png**: Trains the SimpleRNN with the same settings as the tuned LSTM as a baseline without gates.

**40_class_weights.png**: Calculates balanced class weights and trains the tuned LSTM again with them to test whether the class imbalance is holding the model back.

**41_accuracy_curves.png**: Draws the training and validation accuracy curves for every model with the best epoch marked.

**42_loss_curves.png**: Draws the training and validation loss curves for every model.

**43_confusion_matrices_all.png**: Draws a confusion matrix for every model on the test set, in percentages of each actual author.

**44_per_author_scores.png**: Calculates precision, recall and F1 for each author for every model and saves a full classification report for each one.

**45_model_comparison_table.png**: Builds the comparison table of every model with its parameters, epochs, training time, validation results and test results, and names the best model.

**46_model_comparison_chart.png**: Charts the test accuracy with its margin of error and the macro F1 of every model, next to the training time of each one.

**47_best_model_report.png**: Prints the full classification report for the chosen model and draws its confusion matrix in counts and in percentages.

**48_error_analysis.png**: Examines the errors of the chosen model by sentence length and by prediction confidence, and lists the most confident mistakes.

**49_fan_bot.png**: Defines the predict_author function that powers the fan bot and runs it on example passages, showing the guess and the probability for each author.
