# Introduction
This is based loosely from the content in https://github.com/Azure-Samples/openai/tree/main/Basic_Samples/LangChain

# Prerequisites

There are only three prerequisites:

- Python
- Pip
- jupyter-lab



# Environments setup

IMPORTANT! _config.json_ is ignored in this project folder for security purposes since it will have your keys

Create a copy of _config.json.base_ and rename it _config.json_

In order to use the Open AI library or REST API with Microsoft Azure endpoints, you need to set DEPLOYMENT_NAME, OPENAI_API_BASE, OPENAI_API_VERSION and OPENAI_API_KEY in _config.json_ file. 

```js
{
    "DEPLOYMENT_NAME":"<Model Deployment Name>",
    "OPENAI_API_BASE":"https://<Your Azure Resource Name>.openai.azure.com",
    "OPENAI_API_VERSION":"<OpenAI API Version>",
    "OPENAI_API_KEY":"<Your API Key Value>"
}
``` 

