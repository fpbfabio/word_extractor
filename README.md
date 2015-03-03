# word_extractor
> Prints all unique words from a collection set up in Apache Solr

## How to use

Execute the bash file program.sh

```.sh
./program.sh <core url> <target field>
```
#### About the command line parameters:
1. core url = the url of the Solr's core which the words wil be printed, for instance, if you set up Solr in localhost port 8983, and the core name is "newsgroups", the url would be http://localhost:8983/solr/newsgroups/
2. target field = the name of the field defined in schema.xml which its words will be printed

## Important

Make sure to give the file the necessary permissions, e.g.

```
chmod +rx program.sh
```
