from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from youtube_transcript_api import YouTubeTranscriptApi


app = FastAPI()

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/')
async def hello_world():
  return{
    "hello":"world"
  }

@app.get('/get-transcript/{id}')
async def get_transcript(id):
  try:
    list_transcript = YouTubeTranscriptApi.list_transcripts(id)
    transcript = list_transcript.find_transcript(['vi']).fetch()
    text = ' '.join([item['text'] for item in transcript])
    text = ' '.join(text.split()[:4096])
    return {'transcript': text}
  except:
    return {'transcript': 'transcript not available'}
