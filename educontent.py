import streamlit as st
import google.generativeai as genai

# Configure API key
genai.configure(api_key="AIzaSyDbw8KskjdwuMhNYUVyPwoT7H2lMyyJmRw")

def generate_content(topic, content_type="explanation"):
    """Generates educational content based on the topic and content type.

    Args:
        topic: The topic to generate content for.
        content_type: The type of content to generate (e.g., 'explanation', 'summary', 'quiz').

    Returns:
        A string containing the generated content, or None if an error occurs.
    """
    try:
       
        generation_config = {
            "temperature": 0.5,
            "top_p": 0.95,
            "top_k": 64,
            "max_output_tokens": 2048,
            "response_mime_type": "text/plain",
        }
        model = genai.GenerativeModel(
            model_name="gemini-1.5-flash",
            generation_config=generation_config,
            system_instruction=f"Create a detailed {content_type} about {topic}.",
        )

        
        prompt = f"Generate a {content_type} about {topic}."

        

        
        response = model.generate_content(prompt)
        content_text = response.text

        return content_text

    except Exception as e:
        st.error(f"An error occurred: {e}")
        return None

# Streamlit UI
st.title("Educational Content Generator")

# Input for topic
topic_input = st.text_input("Enter a topic for educational content:", "")

# Select content type
content_type = st.selectbox("Select content type:", ["explanation", "summary", "quiz"])

if st.button("Generate Content"):
    if topic_input:
        content = generate_content(topic_input, content_type)
        if content:
            st.subheader(f"Generated {content_type.capitalize()}:")
            st.write(content)
        else:
            st.error(f"Failed to generate {content_type}.")
    else:
        st.warning("Please enter a topic to generate content.")
