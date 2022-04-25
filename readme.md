### Text Summarizer (Extractive)

> This is a text summarizer that summarizes the text based on the sentence importance.

** Ways to run the program **

```Shell
$ python3 -m venv txt_summ
$ . txt_summ/bin/activate
$ git clone https://github.com/Animesh3193/Summarization.git
$ cd Summarization/
$ python main.py --summarize /home/user/path/to/your/txt/file.txt
```

The program can be run with entry point with main.py file and the text file containing the sentence can be given with argument `--summarize` with the relative or aboslute file path

Similary docker file is provided for the image creation which can be run similary with file mounted at the accessible pvc or mount point.


> The abstractive summarization can be checked in side the folder `Summarization/abstractive`
> ipynb file can be viewed as an Markdown to see the content of approach.