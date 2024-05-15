# Vector Enabled Entity Resolution (VEER)

### Table of Contents
  - [Project Overview](#project-overview)
  - [Getting Started](#getting-started)
  - [Usage](#usage)


## Project Overview

Utilize precomputed vector distances derived from entity attributes to discern similarity, enabling people to effortlessly identify matches and compute match scores for potential or automatic merges. The resulting match scores for existing records serve as a pivotal indicator, guiding actions towards efficient merging strategies. This approach holds the promise of bypassing rigid static rules that dictate exact types of matching, fostering a more adaptable and dynamic resolution process.


## Getting Started

### Setting Up A Virtual Environment

1.⁠ ⁠Install pip if it is not already present on your machine: https://pip.pypa.io/en/stable/installation/
2.⁠ ⁠Create a virtual environment by running:
    
   ``` 
   pip install virtualenv
   virtualenv --python path/to/desired/python/executable/in/your/machine .venv
   ```⁠

3.⁠ ⁠Activate the environment on Mac/Linux (Bash):
    ```
    source .venv/bin/activate
    ```

    Activate the environment on Windows (PowerShell):
    
    ```
     .\.venv\Scripts\activate
    ```
⁠    
     ⁠
    Note: If you run into Windows permissions issues, it is probably because your Power Shell is restriced. Run your IDE/shell as an administrator and set your execution policy.
    https://www.mssqltips.com/sqlservertip/2702/setting-the-powershell-execution-policy/

4.⁠ ⁠Install the project requirements
    
    ```
    pip install -r requirements.txt
    ```
⁠     
     ⁠
5.⁠ ⁠Deactivating the environment when you're all done coding:
    
    ```
    deactivate
    ```
⁠     
     ⁠

## Usage

### Running VEER Locally

Pull the docker image for Qdrant and get it running using the following two commands

```
docker pull qdrant/qdrant

docker run -p 6333:6333 qdrant/qdrant

```

Run the synthetic_data_generation to create a bunch of entity pairs for entity resolution

Run the embeddings notebook next to create a vectorDB out of the entity attributes, which will be stored in the Qdrant server created
when the docker image is setup

Post that, run the demo notebook to run search queries on the vectorDB to return the most similar entities along with score (cosine similarity)

Can also test the matches by running the streamlit app (main.py)

```
streamlit run main.py
```

