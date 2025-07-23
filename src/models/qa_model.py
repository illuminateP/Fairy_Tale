from transformers import AutoTokenizer, AutoModelForQuestionAnswering
import torch

MODEL_PATH = "src/models"
tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)
model = AutoModelForQuestionAnswering.from_pretrained(MODEL_PATH)
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

def qa_infer(question: str, context: str, max_len: int = 512) -> str:
    inputs = tokenizer(
        question, context,
        truncation="only_second", max_length=max_len,
        return_offsets_mapping=False, return_tensors="pt"
    ).to(device)
    with torch.no_grad():
        out = model(**inputs)
    s = int(torch.argmax(out.start_logits))
    e = int(torch.argmax(out.end_logits))
    if e < s: e = s
    answer_ids = inputs["input_ids"][0][s:e+1]
    return tokenizer.decode(answer_ids, skip_special_tokens=True).strip() 