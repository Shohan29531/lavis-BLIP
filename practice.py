from lavis.models import model_zoo
import torch
from PIL import Image

from lavis.models import load_model_and_preprocess






device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

raw_image = Image.open("input/ex.jpeg").convert("RGB")

model, vis_processors, txt_processors = load_model_and_preprocess(name="blip_vqa", model_type="vqav2", is_eval=True, device=device)
# ask a random question.
question = "Is there a white cane in the scene?"

# question = "What is the color of the hat?"

image = vis_processors["eval"](raw_image).unsqueeze(0).to(device)
question = txt_processors["eval"](question)
answer = model.predict_answers(samples={"image": image, "text_input": question}, inference_method="generate")[0]


print(question)
print(answer)
# ['singapore']