## Sentiment analysis filtering tool

### Overview
This tool accepts textual data as input and filters it based on polarity and/or subjectivity.

## Example input

```json
{
    "data": [
        {"id": 1, "text": "This is a positive review."},
        {"id": 2, "text": "This is a negative review."}
    ],
    "include": [1, 2]
}
```

### Folder structure
- custom_tokenizers
  - BaseTokenizer: Base class for all custom tokenizers
  - RobertaTokenizer: Concrete class that implements tokenization for RoBERTa-based models
- models
  - BaseModel.py: Base class for models.
  - RobertaModel.py: Parent class for RoBERTa-based models
  - RobertaPolarityModel.py: Concrete class for polarity detection
  - RobertaSubjectivityModel.py: Concrete class for subjectivity detection
- Service
  - PredictionService: Service that implements filtering logic
- test: tests for 
- utils
  - Review.py: Data container for review data.
  - ReviewFactory.py: Class that instantiates Review objects and provides other utility functions
- Controller.py: entrypoint of the service
- config.ini: file with configurations

### How to execute
To run the tool:
1. Clone the repository.
2. Add the models in the project’s root folder.
3. Install requirements.txt.
4. Run the Controller.py.

Alternatively:
1. Make sure Docker is installed in your system.
2. Build the image defined in the Dockerfile.
3. Run the container. Remember to attach Docker volumes with the models to the container.

