with open('message.txt', 'r', encoding='utf-8') as msg_file:
    message = msg_file.read()

with open('template.html', 'r', encoding='utf-8') as template_file:
    template = template_file.read()

output = template.replace('{{ message }}', message)

with open('index.html', 'w', encoding='utf-8') as output_file:
    output_file.write(output)