![](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)
# Retrieval Augmented Generation (RAG) with Ollama and ChromaDB

A Python project that uses ChromaDB and Ollama to generate answers based on documents. 
Only uses open source products, and it meant to run locally on your computer. 

## Description

A client was looking for a RAG solution as part of their products. I did this project
as a test case to see how difficult that would be. I had found some articles, but those
were typically notebooks, and not meant to run continuously.

This project has two Python scripts:
* load_data.py loads the document that you want to ask questions about into a ChromaDB, and persists it.
* rag_server.py connects to the ChromaDB and answers questions based on the information in the document.

The code is adapted from [this article on Medium](https://medium.com/@rubentak/talk-to-your-files-in-a-local-rag-application-using-mistral-7b-langchain-and-chroma-db-no-2b4ba77358e0).


## Getting Started

### Dependencies

* Ollama
* Python 3.9

### Installing

* These instructions are for a Mac, I assume it would be similar on any other OS
* Install Ollama on your computer: https://ollama.com/download/mac
* Create a virtual environment based on Python 3.9
* Download a sample document. I used [Alice in Wonderland](https://archive.org/stream/alicesadventures19033gut/19033.txt)
* Run `python -m pip install -r requirements.txt`

Ensure that 
```
loader = DirectoryLoader('./../../data/')
```
in load_data.py points to the directory that contains your document(s).


### Executing program

* Ensure Ollama is running
* Run `python load_data.py`. This may take a couple of minutes
* Run `python rag_server.py`

## Enhancements

This program only uses one document as its knowledge base, 
but it is not difficult to extend this to multiple directories, and also
multiple formats. For more info, see [langchain document loaders](https://python.langchain.com/docs/modules/data_connection/document_loaders/).

## Help

Feel free to reach out with comments or issues. 

## Authors

Jan Gerritsen

## Version History

* 0.1
    * Initial Release

## License

This project is licensed under the MIT License - see the license.txt file for details

## Acknowledgments

* [Talk to your files](https://medium.com/@rubentak/talk-to-your-files-in-a-local-rag-application-using-mistral-7b-langchain-and-chroma-db-no-2b4ba77358e0)

