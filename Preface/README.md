# Preface

Artificial Intelligence (AI) has become incredibly popular in recent times, making headlines everywhere—from school discussions to debates in the US Senate. This fast-growing field is grabbing attention from both experts in machine learning and everyday people alike. While some worry about where AI is headed, others even suggest extreme actions, like destroying data centers. Even the White House is weighing in on the future of AI.

But rather than fearing AI's rise, we believe it's more productive to focus on how it can help us in our daily lives—whether through Siri or other AI-powered assistants. There are countless articles about AI, especially about Generative AI and large language models, aimed at readers with different levels of expertise. Unfortunately, most of these require some technical background to fully understand.

And there's no straightforward set of guidelines for learning everything about AI, which is why we wrote this book. It's designed to be a clear and easy-to-follow roadmap for beginners, guiding you through the complicated language and concepts. Don't worry, you won't need to be a machine learning expert to get the hang of it!

After weeks of research and planning, we've come up with a practical learning path for Generative AI, and we're excited to share it with you.

## The Generative AI Learning Path

The Generative AI learning path is structured into 7 interconnected stages:

### 1. Understand Generative AI Key Concepts

* **Artificial Intelligence**: Learn the basic principles of AI, including what it is and how it's applied.
* **Machine Learning**: Study the core concepts of machine learning, such as supervised and unsupervised learning, algorithms, and model training.
* **Deep Learning**: Dive into deep learning basics, focusing on neural networks and how they work, including popular architectures like CNNs and RNNs.
* **Natural Language Processing (NLP)**: Get familiar with NLP, which deals with the interaction between computers and human language.

These fundamentals are crucial for learning more advanced AI topics.

### 2. Setup Environment with Local LLMs

* **Run Local Models**: Experiment with running local models using tools like Ollama or other open-source implementations. Learn how to set up and use models on your local machine.
* Set up your local Python environment with Miniconda and JupyterLab to begin your journey into Generative AI.
* **Explore Model Sharing Platforms**: Use platforms like Hugging Face to access pre-trained models and datasets. This will allow you to experiment with a wide range of generative AI models.

### 3. Learn Frameworks

* **LangChain**: Start using LangChain to build applications that leverage language models. This will help you integrate generative AI into real-world applications.
* **LlmIndex**: Explore LlmIndex for indexing and searching through large language models.
* **Python**: Enhance your programming skills in Python, the most widely used language for AI development. Focus on libraries like TensorFlow, PyTorch, and Hugging Face's Transformers.

### 4. Fine-tuning/Enrich LLMs

* **Fine-Tuning Techniques**: Learn how to fine-tune pre-trained models to better suit specific tasks or datasets.
* **Enrichment Techniques**: Study methods like Retrieval-Augmented Generation (RAG) to improve the output quality of your models.

### 5. Build Projects and Agents

* **Small Projects**: Start with small projects, such as generating text, images, or other media, to reinforce your learning.
* **Agents**: Developing agents that can handle some of your daily routine tasks, such as searching the internet and generating quality text for blog writing on specific topics.

### 6. Stay Updated and Keep Learning

* **Follow AI Trends**: Stay updated with the latest advancements in AI by following relevant blogs, YouTube channels, and online courses.
* **Collaborate and Share**: Engage with online communities, participate in AI challenges, and share your projects on platforms like GitHub.

### 7. Advanced Topics

Once comfortable with the basics, dive into advanced topics like reinforcement learning, advanced model architectures, and cutting-edge AI research.

This path will give you a strong foundation in Generative AI, allowing you to progressively build your expertise and apply it to real-world scenarios.

## What This Book Covers

This book provides a comprehensive guide to leveraging Generative AI and Large Language Models (LLMs) in a local development environment. It is designed to take you from the basics of Generative AI to advanced techniques like fine-tuning models, enriching them with private datasets, and applying them in practical scenarios such as SQL querying, image processing, and developing Agents. Whether you're a product owners, developers, data scientists, and AI enthusiasts, this book will equip you with the knowledge and tools needed to effectively utilize AI in your projects.

### Chapter 1. Getting Started with Local LLM

Before diving into AI model implementation, it's essential to set up a robust local development environment. This chapter guides you through the process of configuring your machine for AI development, including installing necessary software, setting up Python environments, and choosing the right hardware (like GPUs) for optimal performance. The chapter also introduces tools like Jupyter notebooks which will help streamline your AI development workflow.

### Chapter 2. Deep Dive into the Theories of Generative AI

The journey begins with an introduction to Generative AI, explaining what it is, how it works, and why it is revolutionizing various fields. This chapter covers the fundamental concepts of AI, machine learning, and deep learning, laying the groundwork for understanding how LLMs generate content such as text, code, and images. You'll explore various types of generative models, including the Self-Attention mechanism, Encoder-Decoder architecture, and Transformers, along with their applications across different industries.

### Chapter 3: RAG, Enrich LLM Models with Private Datasets

This chapter explores the concept of Retrieval-Augmented Generation (RAG), an advanced technique that enhances LLMs by incorporating private datasets. You'll discover how to enrich your AI models with domain-specific knowledge, allowing them to generate more accurate and relevant outputs. The chapter outlines the technical steps for setting up RAG, including Vector DB, indexing private data, and configuring the model to retrieve and generate responses based on this enriched information.

### Chapter 4: Text-to-SQL, Enhance Your LLM Responses by Integrating Data from the Database

AI-driven automation in database interactions is increasingly valuable, and this chapter focuses on using LLMs for Text-to-SQL conversion. You'll learn how to use models that can translate natural language queries into SQL commands, specifically tailored for interactions with BigQuery. The chapter includes practical examples and code snippets, showing how to create systems that allow users to interact with databases without needing to know SQL, making data retrieval more accessible and efficient.

### Chapter 5: Fine Tuning LLM Model

This chapter takes a deep dive into the fine-tuning process, a crucial step in customizing LLMs to better suit your specific needs. You'll explore how to adapt pre-trained models to your data, improving their performance on tasks relevant to your domain. The chapter covers the technical aspects of fine-tuning, including data preparation, adjusting hyperparameters, and evaluating model performance. By the end of this chapter, you'll be able to refine models to achieve higher accuracy and relevance in your applications.

### Chapter 6: Image Processing & Generating with LLM

Generative AI is not limited to text; it also plays a significant role in image processing and generation. This chapter explores how LLMs can be used to create and manipulate images. The chapter provides practical examples and tools, including using models like LLaVa, OpenJourney, to help integrate image generation into your projects.

### Chapter 7: Developing and Utilizing AI Agents

The final chapter focuses on one of the most exciting applications of LLMs: developing AI Agents. You'll learn about the purpose and benefits of using AI Agents to automate daily tasks. The chapter explores the architecture of AI agents and their key components. Toward the end, we introduce a multi-agent framework that enables non-technical users to manage AI agents and tasks using intuitive, high-level abstractions.

## Code Samples

All code samples, scripts, and more in-depth examples can be found on the GitHub repository.

## Readership

The target audiences of this book are product owners, developers, data scientists, and AI enthusiasts with minimum programming knowledge. No excessive knowledge is required, though it would be good to be familiar with Python, Java and tools like Conda.

## Conventions

The following typographical conventions are used in this book:

1. *Italic* and **Bold** indicates new terms, important words, URL's, filenames, and file extensions.
2. A block code is set as follows:

```python
def process_image(image_file_path, prompt):
    print(f"\nProcessing {image_file_path} file \n")
    image = Image.open(image_file_path)
    display(image)
    
    with image as img:
        with BytesIO() as buffer:
            img.save(buffer, format='PNG')
            image_bytes = buffer.getvalue()
            
            # Generate a description of the image
            for response in generate(model='llava:34b',
                                  prompt=prompt,
                                  images=[image_bytes],
                                  stream=True):
                # Print the response to the console and add it to the full response
                print(response['response'], end='', flush=True)
```

3. Any command-line input or output is written as follows:

```bash
!pip install ollama
export OLLAMA_HOST="192.168.1.124"
Processing ./Text2SQL.png file
```
