import torch
from transformers import AutoModel, AutoTokenizer
from sentence_transformers import SentenceTransformer
from tqdm import tqdm

DEVICE = "cuda" if torch.cuda.is_available() else "cpu"


def gen_batch(records, batch_size):
    batch_start = 0
    while batch_start < len(records):
        batch_end = batch_start + batch_size
        batch = records[batch_start: batch_end]
        batch_start = batch_end
        yield batch


class Embedder:
    def __init__(
        self,
        model_name,
        batch_size=64,
        max_length=128,
        device=DEVICE
    ):
        self.model_name = model_name
        #self.model = AutoModel.from_pretrained(model_name).to(device)
        self.model = SentenceTransformer(model_name, device)
        #self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        #self.device = device
        #self.batch_size = batch_size
        #self.max_length = max_length

    def __call__(self, texts):
        return self.model.encode(texts)

    def __call__2(self, texts):
        embeddings = torch.zeros((len(texts), self.model.config.hidden_size))
        for batch_num, batch in enumerate(tqdm(gen_batch(texts, self.batch_size))):
            inputs = self.tokenizer(
                batch,
                return_tensors="pt",
                padding=True,
                truncation=True,
                max_length=self.max_length
            ).to(self.model.device)
            with torch.no_grad():
                out = self.model(**inputs)
                batch_embeddings = out.pooler_output
                batch_embeddings = torch.nn.functional.normalize(batch_embeddings)
            start_index = batch_num * self.batch_size
            end_index = (batch_num + 1) * self.batch_size
            embeddings[start_index:end_index, :] = batch_embeddings
        return embeddings
