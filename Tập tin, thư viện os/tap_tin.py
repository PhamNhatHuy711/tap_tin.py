def save_text(text, file):
    with open(file, 'w', encoding='utf-8') as f:
        f.write(text)
def main():
    text = str(input())
    file = str(input())
    save_text(text, file)
    print("ádasd")
if __name__=="__main__":
    main()