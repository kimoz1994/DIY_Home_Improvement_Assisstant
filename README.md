# DIY Home Improvement Assistant

A **Retrieval-Augmented Generation (RAG)** application that answers questions related to home renovation and DIY improvement topics.  
It combines search with a local LLM to provide accurate, context-based responses grounded in real instructional content and references.

Repository: [DIY Home Improvement Assistant](https://github.com/kimoz1994/DIY_Home_Improvement_Assisstant/tree/main)

---

## Main Features

The DIY Home Improvement Assistant features a **simple Streamlit user interface** that allows users to ask any home improvement–related question.  

**Workflow:**
1. **Retrieval:**  
   The system retrieves relevant context from a pre-indexed dataset containing DIY-related information.
2. **Answer Generation:**  
   The user’s question, along with the retrieved context, is sent to a **local large language model (LLM)** hosted via **LM Studio**.
3. **Response Output:**  
   The LLM generates a textual answer that provides clear, step-by-step instructions or descriptive guidance.
4. **Reference Integration:**  
   Below each generated answer, the application displays **five YouTube video links** that serve as visual references for the topic.

---

## Target Users & Use Cases

The app is designed to assist a wide range of users seeking guidance on home renovation and repair tasks, including:

- 🏡 **Homeowners** — want to fix or upgrade parts of their homes independently.  
- 🛠️ **Hobbyists and DIY enthusiasts** — enjoy hands-on improvement projects and want reliable guidance.  
- 🧰 **Beginners** — need step-by-step support for new home renovation tasks.  
- 👷 **Professionals** — may use the tool for quick reference or to find additional instructional resources.

**Topics covered:**  
- Basements, Toilets, Plumbing, Bathtubs, Showers, Electrical, Flooring, Windows and Doors, Power Tools, Mechanical, Lighting, Doors, Walls and Ceilings, Carpentry, Cleaning

---

## System Architecture & Workflow

The app integrates several key components to provide an intelligent, retrieval-augmented experience:

- 🧠 **Local LLM (LM Studio)** — generates textual answers from retrieved context.  
- 🔍 **MinSearch Index** — indexes and retrieves relevant sections from the dataset.  
- 💬 **Streamlit Interface** — allows users to submit questions easily.  
- 🐳 **Dockerized Application** — ensures consistent and portable setup across systems.

**Workflow overview:**
1. User enters a question through the Streamlit UI (e.g., “How to fix a leaking faucet?”).  
2. The question is used to query the **MinSearch** index for the most relevant context.  
3. The question and retrieved context are sent to the **local LLM**.  
4. The LLM generates an answer — textual instructions with **five reference YouTube links**.

---

## Dataset

The app relies on a curated dataset of **YouTube transcripts** focused on home improvement and renovation topics.

**Dataset details:**
- **Source:** Transcripts collected from YouTube videos on home improvement and renovation.  
- **Playlists Covered:** Basements, Toilets, Plumbing, Bathtubs, Showers, Electrical, Flooring, Windows and Doors, Power Tools, Mechanical, Lighting, Doors, Walls and Ceilings, Carpentry, Cleaning.  

**Data fields:**
- `start_time` — start time of a chapter in the YouTube video  
- `end_time` — end time of the chapter  
- `playlist_title` — title of the playlist the video belongs to  
- `playlist_id` — ID of the playlist  
- `video_title` — title of the YouTube video  
- `video_id` — ID of the video  
- `chapter_title` — title of the chapter inside the video  
- `chapter_id` — ID of the chapter  
- `content` — transcript text for the chapter  
- `clip_link` — YouTube link pointing to the chapter start  

Data set file here: [Dataset](https://github.com/kimoz1994/DIY_Home_Improvement_Assisstant/tree/main/diy-streamlit-app/DIY_dataset)


**Indexing:**  
- The dataset is pre-indexed using **MinSearch**, with `chapter_title` and `content` used for semantic search, enabling fast retrieval for user queries.

---

## Usage / Examples

**1. Install prerequisites:**  
- Docker  
- LM Studio

**2. Download and serve the LLM:**  
- Download `Llama-3.2-3B-Instruct`  
- Open LM Studio, load the model, and serve it locally  
- **Important:** Set context tokens ≥ 9000 to handle long context  

**3. Download the repository:**

- `git clone https://github.com/kimoz1994/DIY_Home_Improvement_Assisstant.git

**4. Build and run the Docker container**

Inside the my-streamlit-app folder -> Build image:

- `docker build -t my-streamlit-app .`

- `docker run -p 8501:8501 my-streamlit-app`

**5. Interact with the app**

- Open your browser: `http://localhost:8501`

- Enter a home improvement question (e.g., “How to install a toilet?”)


- The app will return:

- Textual answer with instructions

- References: up to five YouTube links

💡 You can click the reference links to watch the videos in a separate tab.


---

## Evaluation

### 📊 Retrieval and RAG Evaluation

- Retrieval evaluation dataset and notebook are [here](https://github.com/kimoz1994/DIY_Home_Improvement_Assisstant/tree/main/retrieval_evaluation)

**Without boosting:**
- `{'hit_rate': 0.5736821086261981, 'mrr': 0.347409145367411}`

**With boosting:**

- `{'hit_rate': 0.805111821086262, 'mrr': 0.5459778639890454}`

**Boosting values:**

`{
  'playlist_title': 3.4311350452088907,
  'video_title': 3.6054325902612927,
  'chapter_title': 1.3418523035711323,
  'content': 12.3649113626517
}`


**🧠 RAG Evaluation**

- For RAG evaluation, the LLM-as-a-judge method was used to assess answer quality and relevance.
- Rag evaluation Dataset and Notebook is [here](https://github.com/kimoz1994/DIY_Home_Improvement_Assisstant/tree/main/rag_evaluation)

- ![RAG Evaluation Chart](https://github.com/kimoz1994/DIY_Home_Improvement_Assisstant/blob/main/rag_evaluation/histogram.png?raw=true)


---

## 🎥 Demo

- click the picture to download the video

[![Watch the Demo](https://github.com/kimoz1994/DIY_Home_Improvement_Assisstant/blob/main/thumbnail.PNG)](https://github.com/kimoz1994/DIY_Home_Improvement_Assisstant/blob/main/Demo.mp4?raw=true)

