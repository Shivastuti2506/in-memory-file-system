import requests

url = 'http://127.0.0.1:5000'

def get_response(response):
    print(response.json())

def main():
    while 1:
        print("\nAvailable commands:")
        print("1. mkdir")
        print("2. ls")
        print("3. cd")
        print("4. mv")
        print("5. cp")
        print("6. rm")
        print("7. cat")
        print("8. touch")
        print("9. echo")
        print("10. exit")
        print("11. grep")

        task = input("Enter the command (e.g., mkdir, ls, cd, mv, cp, rm, cat, touch, echo, exit, grep): ").strip()

        if task== 'exit':
            break

        if task== 'mkdir':
            directory_name = input("Enter the directory name: ").strip()
            response = requests.post(f'{url}/mkdir', json={'directory_name': directory_name})
            get_response(response)

        elif task == 'ls':
            directory_name = input("Enter the directory name (default is current directory): ").strip()
            response = requests.get(f'{url}/ls', params={'directory_name': directory_name})
            get_response(response)

        elif task == 'cd':
            directory_name = input("Enter the directory name or path: ").strip()
            response = requests.post(f'{url}/cd', json={'directory_name': directory_name})
            get_response(response)

        elif task == 'mv':
            source = input("Enter the source path: ").strip()
            destination = input("Enter the destination path: ").strip()
            response = requests.post(f'{url}/mv', json={'source': source, 'destination': destination})
            get_response(response)

        elif task== 'cp':
            source = input("Enter the source path: ").strip()
            destination = input("Enter the destination path: ").strip()
            response = requests.post(f'{url}/cp', json={'source': source, 'destination': destination})
            get_response(response)

        elif task== 'rm':
            target = input("Enter the target path: ").strip()
            response = requests.post(f'{url}/rm', json={'target': target})
            get_response(response)

        elif task == 'cat':
            file_path = input("Enter the file path: ").strip()
            response = requests.get(f'{url}/cat', params={'file_path': file_path})
            get_response(response)

        elif task == 'touch':
            file_path = input("Enter the file path: ").strip()
            response = requests.post(f'{url}/touch', json={'file_path': file_path})
            get_response(response)

        elif task == 'echo':
            file_path = input("Enter the file path: ").strip()
            content = input("Enter the content: ")
            response = requests.post(f'{url}/echo', json={'file_path': file_path, 'content': content})
            get_response(response)

        elif task == 'grep':
            file_path = input("Enter the file path: ").strip()
            pattern = input("Enter the pattern to search: ").strip()
            response = requests.get(f'{url}/grep', params={'file_path': file_path, 'pattern': pattern})
            get_response(response)


        else:
            print("Sorry! No such command exists.")

if __name__ == '__main__':
    main()
