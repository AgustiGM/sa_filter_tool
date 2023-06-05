class BaseModel:
    def __init__(self, path, model_name):
        self.path = path
        self.model_name = model_name
        self.tokenizer = None
        self.model = None

    def load(self):
        """Load in model for inferencing."""
        pass

    def predict(self, data):
        """Make predictions about data"""
        pass

    def unload(self):
        """Unload model"""
        self.model = None
        self.tokenizer= None

    def prepare_data(self, data):
        tokenized_data = self.tokenizer.tokenize(data)
        return tokenized_data
