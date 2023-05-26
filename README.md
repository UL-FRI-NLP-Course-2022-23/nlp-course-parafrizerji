# Natural language processing course 2022/23: Paraphrasing sentences

Group public acronym/name: `Parafrizerji`

Team members:
 * Uroš Škrjanc, us1883@student.uni-lj.si
 * Jaka Mesarec, jm85537@student.uni-lj.si
 * Grega Rovšček, gr57908@student.uni-lj.si
 
Our repository is divided into the following folders:
- code (our code used in the project)
- report (final report on the project)
- results (all the results obtained by paraphrasing the sentences)
- database (sentences that we used for training and paraphrasing)

Models are available on the following link https://drive.google.com/drive/u/1/folders/1f0zVKhslcP72YnEIVydC55womiWyLMOy and are placed in separate folders. The name of each folder indicates the model, compiler and number of epochs used for training (T5_Clarin_50 means T5 model trained on sentences gained from the Clarin translator trained on 50 epoch).

ccGigafida corpus is available on the follwing link: https://www.clarin.si/repository/xmlui/handle/11356/1035. 

Clarin translator is available at: https://github.com/clarinsi/Slovene_NMT


**CODE** <br>
**Translation.ipynb** <br>
First connects to and creates folders on your Google Drive. After that, you must manually load files of text corpus (ccGigafida or similar) in folder /NLPProject/corpus. The script then reads all sentences from the corpus, stores them on Google Drive and from that database selects a certain number of sentences and sends them to translators (Clarin, Google Translator and Deepl Translator). If you want to use the Clarin translator, you have to install it on your local computer accordingly to the instructions on their website. After translation translated and untranslated sentences are stored separately and do not overlap. Finally, you can export translated sentences to an Excel file and edit them manually.

**T5_Test.ipynb and GPT_Test.ipynb** <br>
Scripts are used to train models. Before training models, sentences for training must be placed in /NLPProject/data folder and must be structured like DeeplTrening.xlsx, GoogleTrening.xlsx or ClarinTrening.xlsx files in the repository. By setting the variable newmodel on True or False, you can either train a new model or retrain the model you got before. Models are then stored in folder /NLPProject/models and names indicates when the model was built.

**T5_Test.ipynb and GPT_Test.ipynb** <br>
Scripts are used for generating paraphrases from selected sentences. The sentences must be placed in the directory /NLPProject/paraphrasing and must be structured like TestSentences.xlsx file on repository. Model must be manually uploaded in the /NLPProject/paraphrasing/model directory. Results are then stored in the Paraphrases.xlsx file in the /NLPProject/paraphrasing directory.
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
**results/model-outputs** <br>
Results we obtained from paraphrasing with different translators and models. The names of the files indicate the model, compiler and number of epochs used for training (T5_Clarin_50 means T5 model trained on sentences gained from Clarin translator trained on 50 epoch).

**results/automatic-evaluation-scores** <br>
Results obtained from automatically evaluating the paraphrases from results/model-outputs and results/t5-choice.

**results/human-evaluation-scores** <br>
Human evaluation of a few outputs from results/model-outputs and results/t5-choice.

**results/t5-choice** <br>
Chosen outputs for T5 models, based on perplexity score.

<br>

**DATABASE** <br>
ClarinTrening.xlsx, DeeplTrening.xlsx and GoogleTrening.xlsx are files for training the models. Each file contains sentences translated with different translator (Clarin, Deepl, Google Translate) 

The file TestSentences.xlsx contains sentences for testing and evaluation of models.

