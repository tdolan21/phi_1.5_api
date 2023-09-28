from fastapi import FastAPI, Query, UploadFile, Depends
from transformers import AutoModelForCausalLM, AutoTokenizer
from fastapi.middleware.cors import CORSMiddleware
from PIL import Image
from dotenv import load_dotenv
import io
import transformers
import torch


# Load environment variables
load_dotenv()

# Initialize FastAPI app
app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Initialize model and tokenizer
device = torch.device('cuda')
model = AutoModelForCausalLM.from_pretrained("microsoft/phi-1_5", trust_remote_code=True, torch_dtype="auto").to(device)
tokenizer = AutoTokenizer.from_pretrained("microsoft/phi-1_5", trust_remote_code=True, torch_dtype="auto")



@app.get("/")
async def read_root():
    return {"message": "Welcome to phi-1.5 chatbot."}

@app.get("/phi/")
async def generate_text(user_input: str, max_length: int = Query(200, ge=10, le=500)):
    # Tokenize the input
    inputs = tokenizer(user_input, return_tensors="pt", return_attention_mask=False).to(device)
    
    outputs = model.generate(**inputs, max_length=max_length)
    
    text = tokenizer.batch_decode(outputs)[0]

    return {"phi_response": text}


