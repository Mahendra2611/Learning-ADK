- in simple llm, we just make api request to data which is public and model is trained
- Agents : llm for specific uses
- we add an extra layer to these llm to give reponse as per instruction in extra layer
 - this layer has instruction (like how to fetch the data from db), tools , multi agents orchestration,  protection of sensitive data,


### Lite LLM 
- this is a platform that provide access to all the model like open ai, claude, gemini.
- we use open router, a common provider where we can buy the tokens common for all models .
- now we create instance of lite llm and specify the provider name along with model ,