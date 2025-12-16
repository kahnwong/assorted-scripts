import json

with open("Facebook Posts - posts.json.json", 'r') as f:
    data = json.loads(f.read())


with open('posts.html', 'w') as f:
    for i in data:

        content = i['text']
        content = content.replace('\n', '<br>')

        print(content)


        f.write(f"<p> {content} </p>\n")
        f.write('<p>------------------</p>\n')
