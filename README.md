# Install Anaconda Navigator
Download and install the Anaconda

https://www.anaconda.com/products/distribution

# Create a Virtual Environment for RASA
```
pip3 install -U pip # upgrade the pip
conda create --name rasa-chatbot python=3.9
conda update -n base -c defaults conda
conda activate rasa-chatbot
pip install rasa

conda install python-crfsuite
conda install grpcio
conda install websocket-client

pip install spacy
python3 -m spacy download en_core_web_md
rasa init

# Perform initial training
# Speak to chatbot
```
