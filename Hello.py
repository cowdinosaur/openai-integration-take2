# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import streamlit as st
import openai
openai.api_key = st.secrets["OPENAI_KEY"]
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)

def openai_completion(prompt):
    response = openai.Completion.create(
      model="text-davinci-003",
      prompt=prompt,
      max_tokens=150,
      temperature=0.5
    )
    return response['choices'][0]['text']

def openai_image(prompt):
    response = openai.Image.create(
      prompt=prompt,
      n=1,
      size="256x256"
    )
    image_url = response['data'][0]['url']
    return image_url

def run():
    st.set_page_config(
      page_title="OpenAI",
      page_icon="✨"
    )
    st.title("📄 GPT 🏜 Streamlit")

    input_text = st.text_area("Please enter text here... 🙋",height=50)
    chat_button = st.button("Do the Magic! ✨")

    if chat_button and input_text.strip() != "":
        with st.spinner("Loading...💫"):
            openai_answer = openai_completion(input_text)
            st.success(openai_answer)
    else:
        st.warning("Please enter something! ⚠")

if __name__ == "__main__":
    run()
