# Opis programov
**Translation.ipynb** 
First connects to and creates folders on your Google Drive. After that you must manually load files of text corpus (ccGigafida or similar) in folder /NLPProject/corpus. Script then read all sentences from corpus, stores them on Google Drive and from that database selects certain number of sentences and sends them to translators (Clarin, Google Translator and Deepl Translator). If you want to use Clarin translator, you have to install it on local computer accordingly to the instructions on their web-site. After translation translated and untranslated sentences are stored separately and do not overlap. Finally you can export translated sentences to Excel file and edit them manually.

**T5_Test.ipynb and GPT_Test.ipynb**
Scripts are used to train models. Before training models sentences for training must be placed in /NLPProject/data folder and must be structured like DeeplTrening.xlsx, GoogleTrening.xlsx or ClarinTrening.xlsx files on repository. By setting variable newmodel on True or False you can either train new model or retrain model you got before. Models are the stored in folder /NLPProject/models and names indicates when model was built.

**T5_Test.ipynb and GPT_Test.ipynb**
Scripts are used for geerating paraphrases from selected sentences. Sentences must be placed in directory /NLPProject/paraphrasing and must be structured like TestSentences.xlsx file on repository. Model must be manually uploaded in /NLPProject/paraphrasing/model directory. Results are then stored in Paraphrases.xlsx file in /NLPProject/paraphrasing directory.


