### Text Summarizer (Extractive)

> This is a text summarizer that summarizes the text based on the sentence importance.

** Ways to run the program **

```Shell
$ python3 main.py --summarize /home/user/path/to/your/txt/file.txt
```

The program can be run with entry point with main.py file and the text file containing the sentence can be given with argument `--summarize` with the relative or aboslute file path

Similary docker file is provided for the image creation which can be run similary with file mounted at the accessible pvc or mount point.