# Natural language processing course 2022/23: Paraphrasing sentences

Group public acronym/name: `Parafrizerji`

Team members:
 * Uroš Škrjanc, us1883@student.uni-lj.si
 * Jaka Mesarec, jm85537@student.uni-lj.si
 * Grega Rovšček, gr57908@student.uni-lj.si
 
Our repository is divided into the following folders:
- Code (our code used in project)
- Reports (final report on project)
- Results (all the results obtained by paraphrasing the sentences)
- Database (sentences that we used for training and paraphrasing)

Models are available on link https://drive.google.com/drive/u/1/folders/1f0zVKhslcP72YnEIVydC55womiWyLMOy and are placed in separate folders. Name of each folder indicates the model, compiler and number of epochs used for training (T5_Clarin_50 means T5 model trained on sentences gained from Clarin translator trained on 50 epoch).

ccGigafida corpus is available on link https://www.clarin.si/repository/xmlui/handle/11356/1035. 

Clarin translator is available at link https://github.com/clarinsi/Slovene_NMT


**CODE** <br>
**Translation.ipynb** <br>
First connects to and creates folders on your Google Drive. After that you must manually load files of text corpus (ccGigafida or similar) in folder /NLPProject/corpus. Script then read all sentences from corpus, stores them on Google Drive and from that database selects certain number of sentences and sends them to translators (Clarin, Google Translator and Deepl Translator). If you want to use Clarin translator, you have to install it on local computer accordingly to the instructions on their web-site. After translation translated and untranslated sentences are stored separately and do not overlap. Finally you can export translated sentences to Excel file and edit them manually.

**T5_Test.ipynb and GPT_Test.ipynb** <br>
Scripts are used to train models. Before training models sentences for training must be placed in /NLPProject/data folder and must be structured like DeeplTrening.xlsx, GoogleTrening.xlsx or ClarinTrening.xlsx files on repository. By setting variable newmodel on True or False you can either train new model or retrain model you got before. Models are the stored in folder /NLPProject/models and names indicates when model was built.

**T5_Test.ipynb and GPT_Test.ipynb** <br>
Scripts are used for geerating paraphrases from selected sentences. Sentences must be placed in directory /NLPProject/paraphrasing and must be structured like TestSentences.xlsx file on repository. Model must be manually uploaded in /NLPProject/paraphrasing/model directory. Results are then stored in Paraphrases.xlsx file in /NLPProject/paraphrasing directory.
<br><br>
Dependencies:
- deepl
- googletrans==4.0.0rc1
- datasets
- transformers 
- SentencePiece 
- evaluate
- rouge_score
- tensorflow_text
- torchtext
- accelerate
- xformers

<br>

**RESULST** <br>
Results we obtained from paraphrasing with different translators and models. Names of the files indicatesmodel, compiler and number of epochs used for training (T5_Clarin_50 means T5 model trained on sentences gained from Clarin translator trained on 50 epoch).

<br>

**DATABASE** <br>
ClarinTrening.xlsx, DeeplTrening.xlsx and GoogleTrening.xlsx are files for training models. Each file contains sentences translated with different translator (Clarin, Deepl, Google Translate) 

TestSentences.xlsx contains sentences for testing and evaluation of models.

