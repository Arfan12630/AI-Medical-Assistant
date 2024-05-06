import streamlit as st 
import pathlib as Path 
import hashlib 
import google.generativeai as genai
from apikey import api_key
genai.configure(api_key=api_key)
generation_config = {
  "temperature": 0.4,
  "top_p": 1,
  "top_k": 32,
  "max_output_tokens": 4096,
}

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
]


model = genai.GenerativeModel(model_name="gemini-1.0-pro-vision-latest",
                              generation_config=generation_config,
                              safety_settings=safety_settings)

st.set_page_config(page_title="VitalImage Analytics", page_icon=":robot")

st.title("Vital Image Analytics")
st.subheader("An application that can help users to identify medical image")
uploaded_file = st.file_uploader("An application that can help users to identify medical images", type=["png", "jpg", "jpeg"])
if uploaded_file:
    st.image(uploaded_file, width=300, caption="Uploaded Medical Image")
submit_button = st.button("Generate the Analysis ")
uploaded_files = []
system_prompt = """
1. Detailed Analysis: Thoroughly analyze each image, focusing on identifying any abnormal findings.
2. Finding Report: Document all observed anomalies or signs of disease. Clearly articulate these findings in a structured format. 
3. Recommendations and Next Steps: Based on your analysis, suggest potential next steps, including further tests or treatments as applicable
4. Treatment Suggestions: If appropiate, recommend possible treatment options or inventions

Important Notes:
1. Scope of Response: Only respond if the image pertains to human health issues. 
2. Clarity of Image: In cases where the image quality impedes clear analysis, note that certain aspects are 'Unable to be determined based on the provided image.'
3. Disclaimer: Accompany your analysis with the disclaimer: "Consult with a Doctor before making any decisions." 

4. Your insights are invaluable in guiding clinical decisions. Please proceed with the analysis adhering to the structured approach outlined above
Please provide me an output response with these 4 headings Detailed Analysis, Finding Report, Recommendations and Next Steps, Treatment Suggestions, Disclaimer
"""
if submit_button:
    image_data = uploaded_file.getvalue()
    image_parts = [
       {
          "mime_type": "image/jpeg",
          "data":image_data
       }
    ]
    prompt_parts = [
      
 
  image_parts[0],
   system_prompt,
]
    # st.image(image_data, width=200)
    st.title("Here is the analysis based on your image: ")
    response = model.generate_content(prompt_parts)
    st.write(response.text)