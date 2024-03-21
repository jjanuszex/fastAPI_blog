Some info abot steps

1. Install python, vscode, create virtual env

python3.12 -m venv venv_blog
source venv/bin/activate
pip3.12 freeze # shows installed packages

2. Install FastAPI

pip3.12 install "fastapi[all]"

3. Dekorator to funkcja wyższego rzędu, która przyjmuje inną funkcję jako argument i zwraca jeszcze inną funkcję, dodając do niej dodatkową funkcjonalność. W Pythonie, dekoratory są zazwyczaj używane do modyfikowania zachowania funkcji lub klasy.

W podanym przez Ciebie fragmencie kodu, `@app.get("/")` jest dekoratorem. Dekorator ten jest dostarczany przez FastAPI i mówi aplikacji, że funkcja `root()` powinna być wywoływana, gdy użytkownik odwiedzi ścieżkę "/" (stronę główną) i wykonuje żądanie GET. FastAPI automatycznie przekształca zwracany słownik na format JSON.

Oto jak to działa:

```python
@app.get("/")  # Dekorator
async def root():  # Funkcja, która jest dekorowana
    return {"message": "Hello World"}  # Zwraca słownik, który FastAPI automatycznie przekształca na JSON
```

Dekoratory są potężnym narzędziem w Pythonie, które pozwala na modyfikowanie i rozszerzanie zachowania funkcji i klas w łatwy i czytelny sposób.