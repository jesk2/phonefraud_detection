import json
from torch.utils.data import Dataset
import os

class TeleAntiFraudDataset(Dataset):
    def __init__(self, json_path, audio_root):
        self.audio_root = audio_root
        with open(json_path, "r") as f:
            # If it's JSONL (one JSON per line)
            self.data = [json.loads(line) for line in f]

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        item = self.data[idx]
        audio_path = os.path.join(self.audio_root, item["audio"])
        text = item.get("asr_text") or item.get("text")
        label = item.get("label")
        reasoning = item.get("reasoning", None)

        return {
            "audio_path": audio_path,
            "text": text,
            "label": label,
            "reasoning": reasoning,
        }

dataset = TeleAntiFraudDataset(
    json_path="data/teleantifraud.jsonl",
    audio_root="data/audio"
)

print(len(dataset))
print(dataset[0])