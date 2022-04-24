import argparse
import heapq

from summarize.clean import clean_text_inside_file
from summarize.model import create_sentence_score


my_parser = argparse.ArgumentParser(description='Text file that needs to be summarized')

my_parser.add_argument('--summarize',
                       metavar='text_file',
                       type=str,
                       help='the path of text file that needs to be summarized')


if __name__ == "__main__":
    args = my_parser.parse_args()
    input_file = args.summarize

    print("File to be read ==>", args.summarize)
    
    sentences_list = clean_text_inside_file(input_file)
    
    sentence_score = create_sentence_score(sentence_list=sentences_list)
    
    important_sentences = heapq.nlargest(4,sentence_score,key=sentence_score.get)                    

    summarized_text = ". ".join(important_sentences)
    
    print("Summary : ", summarized_text)
    
    