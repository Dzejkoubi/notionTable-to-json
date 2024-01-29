import json

def process_input_to_json_with_hint_and_remove_brackets(input_text):
    lines = input_text.strip().split('\n')
    result = []
    for line in lines:
        czech, english = line.strip('|').strip().split('|')

        # Function to process each word: remove text in brackets and collect hints
        def process_word(word):
            start = word.find('(')
            end = word.find(')')
            if start != -1 and end != -1 and start < end:
                return word[:start].strip(), word[start+1:end].strip()
            return word.strip(), None

        czech_processed = []
        english_processed = []
        hints = []

        for word in czech.split('/'):
            processed_word, hint = process_word(word)
            if hint:
                hints.append(hint)
            czech_processed.append(processed_word)

        for word in english.split('/'):
            processed_word, hint = process_word(word)
            if hint:
                hints.append(hint)
            english_processed.append(processed_word)

        entry = {
            "czech": czech_processed,
            "english": english_processed
        }

        if hints:
            entry['hint'] = hints

        result.append(entry)
    return json.dumps(result, ensure_ascii=False, indent=2)

# Path to the input file
file_path = './input.txt'

# Reading the input file
with open(file_path, 'r', encoding='utf-8') as file:
    input_text = file.read()

# Process the input text and get the output in JSON format with hints and without brackets
output_json_with_hints_and_no_brackets = process_input_to_json_with_hint_and_remove_brackets(input_text)

# Path to the output file
output_file_path = './output.json'

# Writing the JSON output to a file
with open(output_file_path, 'w', encoding='utf-8') as file:
    file.write(output_json_with_hints_and_no_brackets)
