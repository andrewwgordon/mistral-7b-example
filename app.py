from langchain.llms import CTransformers
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

llm = CTransformers(model='./model/mistral-7b-v0.1.Q5_K_M.gguf')

prompt_template = "What is a good name for a company that makes {product}?"

llm_chain = LLMChain(
    llm=llm,
    prompt=PromptTemplate.from_template(prompt_template)
)
print(llm_chain("colorful socks"))



