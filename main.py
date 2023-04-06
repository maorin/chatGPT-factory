import os
import openai
import re

def save_to_file(content, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(content)



def parse_and_save_code_segments(text):
    # Define a list of supported languages and their file extensions
    languages = {
        'python': '.py',
        'javascript': '.js',
        'java': '.java',
        'c++': '.cpp',
        'c': '.c',
        'c#': '.cs',
    }

    # Regular expression to identify code segments and languages
    code_regex = re.compile(r'\n\n([\s\S]*?)(?=\s#)\s# ([\w]+)', re.MULTILINE)

    # Find all code segments and languages in the text
    matches = code_regex.finditer(text)

    # Save each code segment as a file
    for i, match in enumerate(matches):
        code = match.group(1)
        language = match.group(2).lower()
        print(code)
        print(language)

        file_extension = languages.get(language)
        if file_extension:
            filename = f'code_segment_{i + 1}{file_extension}'
            save_to_file(code.strip(), filename)
            print(f'Saved code segment {i + 1} as {filename}')
        else:
            print(f'Unsupported language "{language}" for code segment {i + 1}')


            
# Load your API key from an environment variable or secret management service
openai.api_key = os.getenv("OPENAI_API_KEY")

response = openai.Completion.create(model="text-davinci-003",  prompt="Use python hello world 标注是python代码", temperature=0, max_tokens=10)


print(response)
print("-----------------------")
print(response.choices[0].text)
parse_and_save_code_segments(response.choices[0].text)


