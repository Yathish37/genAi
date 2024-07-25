import streamlit as st
import google.generativeai as genai

def generate_story(words):
    """Generates a story based on given words.

    Args:
        words: A list of words to be included in the story.

    Returns:
        A string containing the story, or None if an error occurs.
    """
    try:
        # Configure API key
        genai.configure(api_key="AIzaSyDbw8KskjdwuMhNYUVyPwoT7H2lMyyJmRw")

        # Create the model
        generation_config = {
            "temperature": 0.5,
            "top_p": 0.95,
            "top_k": 64,
            "max_output_tokens": 8192,
            "response_mime_type": "text/plain",
        }
        model = genai.GenerativeModel(
            model_name="gemini-1.5-flash",
            generation_config=generation_config,
            system_instruction="You are a creative writer. Create captivating and coherent stories based on given words.",
        )

        # Construct the prompt
        prompt = f"Create a story that includes the following words: {', '.join(words)}. Ensure the story is engaging and flows naturally."

        # Generate the story
        response = model.generate_content(prompt)
        story_text = response.text

        return story_text

    except Exception as e:
        st.error(f"An error occurred: {e}")
        return None

# Streamlit UI
st.title("Story Generator")

# Input for words
words_input = st.text_input("Enter words separated by commas:", "")

if st.button("Generate Story"):
    if words_input:
        words = [word.strip() for word in words_input.split(",")]
        story = generate_story(words)
        if story:
            st.subheader("Generated Story:")
            st.write(story)
        else:
            st.error("Failed to generate story.")
    else:
        st.warning("Please enter some words to generate a story.")