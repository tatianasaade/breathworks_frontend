import os
from agent.utils import persona_description, breathworks_description, lda_keywords, topic_insights
from gradientai import Gradient
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

GRADIENT_ACCESS_TOKEN = os.getenv('GRADIENT_ACCESS_TOKEN')
GRADIENT_WORKSPACE_ID = os.getenv('GRADIENT_WORKSPACE_ID')

class ModelHandler:
    def __init__(self):
        """
        Initialises the ModelHandler.
        """
        self.gradient = Gradient()
        self.base_model_slug = "nous-hermes2"
        self.adapter = None
        self.role = persona_description
        self.context = breathworks_description
        self.lda_keywords = lda_keywords
        self.topic_insights = topic_insights

    def create_model_adapter(self, name):
        """
        Creates a model adapter for the base model.
        """
        try:
            base = self.gradient.get_base_model(base_model_slug=self.base_model_slug)
            self.adapter = base.create_model_adapter(name=name)
            print("Models adapter created")
        except Exception as e:
            print(f"Error creating model adapter: {e}")

    def delete_adapter(self):
        """
        Deletes the model adapter if it exists.
        """
        if self.adapter:
            try:
                self.adapter.delete()
                print("Adapter deleted successfully.")
            except Exception as e:
                print(f"Error deleting adapter: {e}")

    def generate_response(self, query, max_tokens=150, use_lda_insights=True):
        """
        Generates a response from the model based on the hardcoded role and context, the provided query,
        and optionally insights from relevant LDA topics.

        :param query: The query to ask the model.
        :param max_tokens: The maximum number of tokens to generate.
        :param use_lda_insights: Whether to incorporate LDA topic insights into the response.
        :return: The generated response from the model.
        """
        if not self.adapter:
            print("No adapter created. Please create an adapter first.")
            return

        templated_query = f"### Your Role:\n{self.role}\n\n### Context:\n{self.context}"

        # Incorporate LDA topic insights if requested
        if use_lda_insights:
            templated_query += f"\n### Insights:\n{self.topic_insights}\n"
            templated_query += f"\n\n### Query:\n{query}\n\n"
            templated_query += f"\n### Topic Names:\n{self.lda_keywords['topic_names']}\n"
            templated_query += f"\n### Key Words for Topics:\n{self.lda_keywords['Keywords_with_topics']}\n"
            templated_query += "\n### Response:\n"
        # print(f'This is the template being fed into the LLM {templated_query}')

        try:
            response = self.adapter.complete(query=templated_query, max_generated_token_count=max_tokens)
            print("We got a reponse")
            return response.generated_output
        except Exception as e:
            print(f"Error generating response: {e}")



# if __name__ == "__main__":
#     handler = ModelHandler()
#     handler.list_models()
#     handler.create_model_adapter(name="TestAdapter")

#     # # Generate and print the original response without using LDA topics
#     # original_response = handler.generate_response(
#     #     query="What did you most like about Breathworks?",
#     #     use_lda_insights=False  # Original answer without LDA topics
#     # )
#     # print(f"> Original Response (without LDA insights):\n{original_response}\n")

#     # # Generate and print the enhanced response using LDA topics
#     # enhanced_response = handler.generate_response(
#     #     query="What did you most like about Breathworks?",
#     #     use_lda_insights=True  # Enhanced answer with LDA topics
#     # )
#     # print(f"> Enhanced Response (with LDA insights):\n{enhanced_response}\n")

